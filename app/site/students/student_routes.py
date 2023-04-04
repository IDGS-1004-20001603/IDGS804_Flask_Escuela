from ...controllers.student_controller import setStudent, updateStudent, deleteStudent, insertStudent
from ...models.Student import Students
from ...models.forms import StudentForm
from flask import Blueprint, render_template, request, redirect, url_for

student = Blueprint('student', __name__, url_prefix='/students')

@student.route('/index-student')
def index_students():
    create_form = StudentForm(request.form)
    students = Students.query.all()

    return render_template('index_student.html', form=create_form, students=students)


@student.route('/insert-student', methods=['GET', 'POST'])
def insert_student():
    create_form = StudentForm(request.form)

    if (request.method == 'POST'):
        insertStudent(create_form)
        return redirect(url_for('student.index_students'))

    return render_template('insert_student.html', form=create_form)


@student.route('/update-student', methods=['GET', 'POST'])
def update_student():
    create_form = StudentForm(request.form)

    if (request.method == 'GET'):
        id = request.args.get('id')
        response = setStudent(id, create_form)

    if (request.method == 'POST'):
        updateStudent(create_form.id.data, create_form)
        return redirect(url_for('student.index_students'))

    return render_template('update_student.html', form=response)


@student.route('/delete-student', methods=['GET', 'POST'])
def delete_student():
    create_form = StudentForm(request.form)

    if (request.method == 'GET'):
        id = request.args.get('id')
        response = setStudent(id, create_form)

    if (request.method == 'POST'):
        deleteStudent(create_form.id.data, create_form)
        return redirect(url_for('student.index_students'))

    return render_template('delete_student.html', form=response)