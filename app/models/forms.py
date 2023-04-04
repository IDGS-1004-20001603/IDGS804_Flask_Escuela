from wtforms import Form, StringField, IntegerField, DateField, EmailField, SelectField, validators

class StudentForm(Form):
    id = IntegerField('id')
    name = StringField('name', [
        validators.DataRequired(message='You need to write something')
    ])
    last_name = StringField('last_name', [
        validators.DataRequired(message='You need to write something')
    ])
    age = IntegerField('age', [
        validators.number_range(min=1, max=100, message='You must write sany value in the range to 1 to 100')
    ])
    birthday = DateField('birthday', [
        validators.DataRequired(message='You need to write something')
    ])
    email = EmailField('email', [
        validators.DataRequired(message='You need to write something'),
        validators.Email('You must enter a valid email')
    ])

class TeacherForm(Form):
    id = IntegerField('id')
    name = StringField('name', [
        validators.DataRequired(message='You need to write something')
    ])
    last_name = StringField('last_name', [
        validators.DataRequired(message='You need to write something')
    ])
    gender = SelectField('gender', [
        validators.DataRequired(message='You must select a option')
    ], choices=[('H', 'Hombre'), ('M', 'Mujer'), ('O', 'Otro')])
    curp = StringField('curp', [
        validators.DataRequired(message='You need to write something')
    ])
    rfc = StringField('rfc',  [
        validators.DataRequired(message='You need to write something')
    ])