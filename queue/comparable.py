class Comparable:
    def __init__(self, data):
        self.data = data
        self.priority = 1

    def __str__(self):
        return str(self.data)

    def __eq__(self, other):
        if self.data is other:
            return True
        if type(self) != type(other):
            return False
        if self.priority == other.priority:
            return True
        else:
            return False

    def __lt__(self, other):
        return self.priority < other.priority

    def __le__(self, other):
        return self.priority <= other.priority

    def get_data(self):
        return self.data

    def get_priority(self):
        return self.priority
