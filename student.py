from datetime import date, timedelta


class Student:
    """ A Student class as a base for method testing """
    def __init__(self, first_name, last_name):
        # the underscore tells other developers the bariable is read only
        self._first_name  = first_name
        self._last_name = last_name
        self._start_date = date.today()
        # this date doesn't include leap years, as an fyi
        self.end_date = date.today() + timedelta(days=365)
        self.naughty_list = False

    # this decorator is used as a method which gets data
    @property
    # this gets the full name of the student
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    @property
    def email(self):
        return f'{self._first_name.lower()}.{self._last_name.lower()}@email.com'

    def alert_santa(self):
        self.naughty_list = True

    def apply_extension(self, days):
        self.end_date = self.end_date + timedelta(days=days)