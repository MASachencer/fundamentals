from array import Array


class Grid:
    def __init__(self, rows, columns, fill_value):
        self._data = Array(rows)
        for row in range(rows):
            self._data[row] = Array(columns, fill_value)

    def get_height(self):
        return len(self._data)

    def get_width(self):
        return len(self._data[0])

    def __getitem__(self, index):
        return self._data[index]

    def __str__(self):
        for row in range(self.get_height()):
            for col in range(self.get_width()):
                result += str(self._data[row][col]) + ' '
            result += '\n'
        return result
