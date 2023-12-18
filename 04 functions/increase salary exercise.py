employees = []


def addEmployee(email, salary):
    e = {"email": email, "salary": salary}
    employees.append(e)


addEmployee("ala@email.com", 6000)
addEmployee("ela@email.com", 8000)
addEmployee("ola@email.com", 10000)


def increaseSalary(employees, pctIncrease):
    pctIncrease *= 0.01
    for e in employees:
        e["salary"] *= 1 + pctIncrease


increaseSalary(employees, 20)
print(employees)
