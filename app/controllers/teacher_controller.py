from ..db.db import get_connection


def getTeachers():
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL getTeachers()')
            return cursor.fetchall()
    except Exception as ex:
        return ex


def getTeacherById(id, create_form):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL getTeacher(%s)', (id))
            result_set = cursor.fetchall()
            create_form.id.data = result_set[0][0]
            create_form.name.data = result_set[0][1]
            create_form.last_name.data = result_set[0][2]
            create_form.gender.data = result_set[0][3]
            create_form.curp.data = result_set[0][4]
            create_form.rfc.data = result_set[0][5]

            return create_form
    except Exception as ex:
        return ex


def insertTeacher(teacher):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL insertTeacher(%s, %s, %s, %s, %s)', (teacher.name,
                           teacher.last_name, teacher.gender, teacher.curp, teacher.rfc))
        connection.commit()
        connection.close()
    except Exception as ex:
        return ex


def updateTeacher(teacher):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL updateTeacher(%s, %s, %s, %s, %s, %s)', (teacher.id,
                           teacher.name, teacher.last_name, teacher.gender, teacher.curp, teacher.rfc))
        connection.commit()
        connection.close()
    except Exception as ex:
        return ex


def deleteTeacher(id):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL deleteTeacher(%s)', (id))
        connection.commit()
        connection.close()
    except Exception as ex:
        return ex
