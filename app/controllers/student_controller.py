from ..models.Student import sql_alchemy, Students


def setStudent(id, create_form):
    student = sql_alchemy.session.query(
        Students).filter(Students.id == id).first()
    create_form.id.data = student.id
    create_form.name.data = student.name
    create_form.last_name.data = student.last_name
    create_form.age.data = student.age
    create_form.birthday.data = student.birthday 
    create_form.email.data = student.email

    return create_form


def updateStudent(id, create_form):
    student = sql_alchemy.session.query(
        Students).filter(Students.id == id).first()
    student.name = create_form.name.data
    student.last_name = create_form.last_name.data
    student.age = create_form.age.data
    student.birthday = create_form.birthday.data
    student.email = create_form.email.data
    sql_alchemy.session.add(student)
    sql_alchemy.session.commit()


def deleteStudent(id, create_form):
    student = sql_alchemy.session.query(
        Students).filter(Students.id == id).first()
    student.name = create_form.name.data
    student.last_name = create_form.last_name.data
    student.age = create_form.age.data
    student.birthday = create_form.birthday.data
    student.email = create_form.email.data
    sql_alchemy.session.delete(student)
    sql_alchemy.session.commit()


def insertStudent(create_form):
    student = Students(name=create_form.name.data, last_name=create_form.last_name.data,
                       age=create_form.age.data, birthday=create_form.birthday.data, email=create_form.email.data)
    sql_alchemy.session.add(student)
    sql_alchemy.session.commit()
