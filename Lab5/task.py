class Task:
    """Represents a task in a task list
    
    Attributes:
        - description: string description of the task
        - date: due date of the task
        - time – time the task is due
    """

    def __init__(self, desc, date, time):
        """Sets the tasks description, date, and time"""
        self.description = desc
        self.date = date
        self.time = time

    def get_description(self):
        """Returns the task's description"""
        return self.description
    
    def __str__(self):
        """Returns the task as a string"""
        return self.description + " - Due: " + self.date + " at " + self.time
    
    def __repr__(self):
        """Returns the task as a string to be represented in a file"""
        return self.description + "," + self.date + "," + self.time
    
    def __lt__(self, other):
        """Returns true if the self task is sooner than the other task"""
        # Splits date into month, day, and year
        self_month, self_day, self_year = self.date.split('/')
        other_month, other_day, other_year = other.date.split('/')
        # Splits time into hours and minutes
        self_hour, self_minute = self.time.split(':')
        other_hour, other_minute = other.time.split(':')

        if self_year < other_year:
            return True
        elif self_year > other_year:
            return False
        elif self_month < other_month:
            return True
        elif self_month > other_month:
            return False
        elif self_day < other_day:
            return True
        elif self_day > other_day:
            return False
        elif self_hour < other_hour:
            return True
        elif self_hour > other_hour:
            return False
        elif self_minute < other_minute:
            return True
        elif self_minute > other_minute:
            return False
        else:
            return self.description < other.description
        