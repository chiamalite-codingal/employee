class person(object):
    def __init__(self,name,idnumber):
        self.name = name
        self.number = idnumber
    def display(self):
        print("Name is:",self.name)
        print("id id:",self.idnumber)
class employee(person):
    def __init__(self,name,idnumber,salary,post):
            self.salary = salary #new detail
            self.post = post #new detail
            person.__init__(self,name,idnumber)
#obj
p1 = employee("Mark",345,"500k","Mentor")
print("Employee name is:",p1.name)