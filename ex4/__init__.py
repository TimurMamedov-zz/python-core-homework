def cross_join(employees, departments):
    for employee in employees:
        for department in departments:
            yield employee, department
