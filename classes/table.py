from prettytable import PrettyTable


class Table:
    _headings = []
    _rows = []

    def __init__(self, file):
        for i, line in enumerate(file):
            split_line = line.strip().split(',')
            if i == 0:  # Make the first rows heading rows
                self._headings = split_line
            else:
                self._rows.append(split_line)

    def __str__(self):
        x = PrettyTable()
        x.field_names = self._headings
        x.add_rows(self._rows)
        return x.get_string()

    # TODO: Bubble Sort - Improve
    # TODO: Add ASC/DESC
    # TODO: Add Special handling for Date column
    def sort_by_column(self, column):
        for i in range(len(self._rows)):
            for j in range(0, len(self._rows) - i - 1):
                if self._rows[j][column] > self._rows[j + 1][column]:
                    self._rows[j], self._rows[j + 1] = self._rows[j + 1], self._rows[j]
