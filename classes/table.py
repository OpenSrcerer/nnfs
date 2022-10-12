from prettytable import PrettyTable
import datetime

from utils.time_utils import time_string_to_millis, millis_to_time_string


class Table:
    _headings = []
    _rows = []

    def __init__(self, file):
        for i, line in enumerate(file):
            split_line = list(map(lambda token: token.replace("_", " "), line.strip().split(',')))  # Remove underscores
            if i == 0:  # Make the first rows heading rows
                self._headings = split_line
                self._headings.append("AVERAGE LAP TIME")  # Heading for Average Lap Time
            else:
                split_line.append(self._parse_average_time(split_line))  # Add custom header
                self._rows.append(split_line)  # Add all rows

    def __str__(self):
        x = PrettyTable()
        x.field_names = self._headings
        x.add_rows(self._rows)
        return x.get_string()

    def _parse_average_time(self, split_line):
        time_ms = time_string_to_millis(split_line[len(split_line) - 1])
        num_laps = int(split_line[len(split_line) - 2])
        return millis_to_time_string(time_ms / num_laps)

    def sort_by_column(self, column, descending):
        comparison_lambda = lambda left, right: left < right if descending else left > right

        for i in range(len(self._rows)):
            for j in range(0, len(self._rows) - i - 1):
                if column == 1:
                    date_left = datetime.datetime.strptime(self._rows[j][column], "%d-%b-%y")
                    date_right = datetime.datetime.strptime(self._rows[j + 1][column], "%d-%b-%y")
                    if comparison_lambda(date_left, date_right):
                        self._rows[j], self._rows[j + 1] = self._rows[j + 1], self._rows[j]
                else:
                    if comparison_lambda(self._rows[j][column], self._rows[j + 1][column]):
                        self._rows[j], self._rows[j + 1] = self._rows[j + 1], self._rows[j]
