def cross_join(employees, departments):
    for itemFromOne in employees:
        for itemFromTwo in departments:
            yield (itemFromOne,itemFromTwo)
