import datetime

from prettytable import PrettyTable

from part_1.utils.charting_utils import num_list_average
from part_1.utils.time_utils import avg_time_per_lap, millis_to_time_string


class Table:
    """
    A table with one row of headings and multiple data rows.
    """

    def __init__(self, file):
        """
        Reads a CSV file in the format

        :param file: File to construct table from.
        """
        self._racer_avg_race_times: dict = {}
        self._summed_racer_avg_lap_times: list[tuple] = []
        self._headings: list = []
        self._rows: list[list] = []

        for i, line in enumerate(file):
            file_row = list(map(lambda token: token.replace("_", " "), line.strip().split(',')))  # Remove underscores
            self._parse_headings_rows(i, file_row)
        self._sum_average_lap_time_driver()

    def stringify(self, simple, predicate=lambda row: True):
        """
        :param simple: Print the 6-column version of this table.
        :param predicate: Filtering predicate to show specific rows or not.
        :return: A string representation of this table.
        """
        x = PrettyTable()
        x.clear()

        # Filter rows on condition
        local_rows = list(filter(
            predicate,
            list(map(lambda row: row[:len(row) - 1], self._rows)) if simple else self._rows
        ))

        if len(local_rows) == 0:
            x.field_names = ["Empty Table"]
            x.add_row(["No Data"])
            return x.get_string()

        x.field_names = self._headings[:len(self._headings) - 1] if simple else self._headings
        x.add_rows(local_rows)
        return x.get_string()

    def sort_by_column(self, column, descending) -> None:
        """
        Sort this table by a given column.

        :param column: Column to sort by.
        :param descending: Sort in descending order. Ascending if false.
        :return: None
        """
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

    def yield_summed_lap_times(self) -> tuple[str, int]:
        """
        Generator function.

        :return: A tuple with the average lap time date for a racer.
        """
        for tup in self._summed_racer_avg_lap_times:
            yield tup

    def _parse_headings_rows(self, i, file_row) -> None:
        """
        Parse headings and rows for a file.

        :param i: The current line in the file.
        :param file_row: The current row.
        :return: None
        """
        if i == 0:  # Make the first rows heading rows
            self._headings = file_row
            self._headings.append("AVERAGE LAP TIME")  # Heading for Average Lap Time
        else:
            average_lap_time_millis = avg_time_per_lap(file_row)
            self._parse_racer_avg_time(file_row[2], average_lap_time_millis)
            file_row.append(millis_to_time_string(average_lap_time_millis))  # Add average racer time to end of row
            self._rows.append(file_row)  # Add all rows

    def _sum_average_lap_time_driver(self) -> None:
        """
        Find the average lap time for a driver on all Grands Prix.

        :return: None
        """
        for racer, avg_list in self._racer_avg_race_times.items():
            if len(avg_list) == 0:
                continue
            else:
                self._summed_racer_avg_lap_times.append((racer, num_list_average(avg_list)))
        self._summed_racer_avg_lap_times.sort(key=lambda tup: tup[1])

    def _parse_racer_avg_time(self, racer_name, average_lap_time_millis) -> None:
        """
        :param racer_name: Racer name to add to a dictionary.
        :param average_lap_time_millis: Average lap time (in milliseconds) for the racer.
        :return: None
        """
        if not self._racer_avg_race_times.__contains__(racer_name):
            self._racer_avg_race_times[racer_name] = []
        self._racer_avg_race_times[racer_name].append(average_lap_time_millis)
