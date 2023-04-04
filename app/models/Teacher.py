class Teacher: 
    id = ''
    name = ''
    last_name = ''
    gender = ''
    curp = ''
    rfc = ''

    def __init__(self, id, name, last_name, gender, curp, rfc):
        self.id = id
        self.name = name
        self.last_name = last_name
        self.gender = gender
        self.curp = curp
        self.rfc = rfc