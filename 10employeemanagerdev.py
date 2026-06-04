class Employee:
    def emp(self):
        print("Employee")

class Manager(Employee):
    def manage(self):
        print("Managing")

class Developer(Employee):
    def code(self):
        print("Coding")

class TeamLead(Manager, Developer):
    def lead(self):
        print("Leading Team")

t = TeamLead()
t.emp()
t.manage()
t.code()
t.lead()