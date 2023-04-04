from flask_sqlalchemy import SQLAlchemy
import datetime

sql_alchemy = SQLAlchemy()

class Students(sql_alchemy.Model):
    __tablename__ = 'students'
    id = sql_alchemy.Column(sql_alchemy.Integer, primary_key=True)
    name = sql_alchemy.Column(sql_alchemy.String(50), nullable=False)
    last_name = sql_alchemy.Column(sql_alchemy.String(50), nullable=False)
    age = sql_alchemy.Column(sql_alchemy.Integer, nullable=False)
    birthday = sql_alchemy.Column(sql_alchemy.Date, nullable=False)
    email = sql_alchemy.Column(sql_alchemy.String(50), unique=True)
    creation_date = sql_alchemy.Column(sql_alchemy.DateTime, default=datetime.datetime.now)
