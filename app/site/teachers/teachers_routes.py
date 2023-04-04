from flask import Blueprint, render_template, request, redirect, url_for
from ...controllers.teacher_controller import getTeachers, getTeacherById, insertTeacher, updateTeacher, deleteTeacher
from ...models.Teacher import Teacher
from ...models.forms import TeacherForm

teacher = Blueprint('teacher', __name__, url_prefix='/teachers')

@teacher.route('/index-teacher')
def index_teachers():
    create_form = TeacherForm(request.form)
    teachers = getTeachers()

    return render_template('index_teacher.html', teachers=teachers, form=create_form)


@teacher.route('/insert-teacher', methods=['GET', 'POST'])
def insert_teacher():
    create_form = TeacherForm(request.form)

    if (request.method == 'POST'):
        teacher = Teacher(0, create_form.name.data, create_form.last_name.data,
                          create_form.gender.data, create_form.curp.data, create_form.rfc.data)
        insertTeacher(teacher)
        return redirect(url_for('teacher.index_teachers'))

    return render_template('insert_teacher.html', form=create_form)


@teacher.route('/update-teacher', methods=['GET', 'POST'])
def update_teacher():
    create_form = TeacherForm(request.form)

    if (request.method == 'GET'):
        id = request.args.get('id')
        response = getTeacherById(id, create_form)

    if (request.method == 'POST'):
        id = str(create_form.id.data)
        teacher = Teacher(id, create_form.name.data, create_form.last_name.data,
                          create_form.gender.data, create_form.curp.data, create_form.rfc.data)
        updateTeacher(teacher)
        return redirect(url_for('teacher.index_teachers'))

    return render_template('update_teacher.html', form=response)


@teacher.route('/delete-teacher', methods=['GET', 'POST'])
def delete_teacher():
    create_form = TeacherForm(request.form)
    
    if(request.method == 'GET'):
        id = request.args.get('id')
        response = getTeacherById(id, create_form)
    
    if(request.method == 'POST'):
        id = str(create_form.id.data)
        deleteTeacher(id)
        return redirect(url_for('teacher.index_teachers'))

    return render_template('delete_teacher.html', form=response)
