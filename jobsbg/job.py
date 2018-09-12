def changeTitle(title):
    if len(title) > 50:
        return title[:50]
    else:
        return title


class Job:
    def __init__(self, title, location, date, salary, currency):
        self.title = title
        self.location = location
        self.date = date
        self.salary = salary
        self.currency = currency

    def __str__(self):
        return '{0} Date: {2} in {3} ---> [ {1} {4} ]'\
            .format(changeTitle(self.title), self.salary, self.date, self.location, self.currency)
