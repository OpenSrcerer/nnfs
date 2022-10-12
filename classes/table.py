from prettytable import PrettyTable
import datetime

from utils.time_utils import parse_average_time, time_string_to_millis


class Table:
    _racer_avg_lap_dict = {}
    _headings = []
    _rows = []

    def __init__(self, file):
        for i, line in enumerate(file):
            split_line = list(map(lambda token: token.replace("_", " "), line.strip().split(',')))  # Remove underscores
            self._parse_headings_rows(i, split_line)

    def stringify(self, simple):
        x = PrettyTable()
        x.field_names = self._headings[:len(self._headings) - 1] if simple else self._headings
        x.add_rows(list(map(lambda row: row[:len(row) - 1], self._rows)) if simple else self._rows)
        return x.get_string()

    def _parse_headings_rows(self, i, split_line):
        if i == 0:  # Make the first rows heading rows
            self._headings = split_line
            self._headings.append("AVERAGE LAP TIME")  # Heading for Average Lap Time
        else:
            average_racer_time = parse_average_time(split_line)
            self._parse_racer_avg_time(split_line[2], time_string_to_millis(split_line[len(split_line) - 1]))
            split_line.append(average_racer_time)  # Add custom header
            self._rows.append(split_line)  # Add all rows

    def _parse_racer_avg_time(self, racer_name, average_racer_time):
        if not self._racer_avg_lap_dict.__contains__(racer_name):
            self._racer_avg_lap_dict[racer_name] = []
        self._racer_avg_lap_dict[racer_name].append(average_racer_time)

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
