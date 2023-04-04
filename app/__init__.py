import os
from flask import Flask
from .models.Student import sql_alchemy
from .db.config import DevelopmentConfig
from flask_wtf.csrf import CSRFProtect
from .site.routes import app as routes_app
from .site.students.student_routes import student as student_app
from .site.teachers.teachers_routes import teacher as teacher_app

csrf = CSRFProtect()


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    csrf.init_app(app)

    sql_alchemy.init_app(app)

    with app.app_context():
        sql_alchemy.create_all()

    app.register_blueprint(routes_app)
    app.register_blueprint(student_app)
    app.register_blueprint(teacher_app)

    return app
