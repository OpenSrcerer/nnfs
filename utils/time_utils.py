from datetime import timedelta


def parse_average_time(file_row) -> str:
    """
    Given split_line, extracts the TIME and LAPS fields,
    then returns a time string for TIME / LAPS.

    :param file_row: A split line in the format
    [GRAND PRIX, DATE, WINNER, CAR, LAPS, TIME]
    :return:
    """
    time_ms = time_string_to_millis(file_row[len(file_row) - 1])
    num_laps = int(file_row[len(file_row) - 2])
    return millis_to_time_string(time_ms / num_laps)


def time_string_to_millis(stringified_time) -> int:
    """
    :param stringified_time: Time string in the format HH:MM:SS.sss
    :return: The total time of stringified_time in millis.
    """
    time = stringified_time.split(':')
    h, m = (time[0], time[1])
    s, sss = time[2].split('.')
    return int(h) * 3_600_000 + int(m) * 60_000 + int(s) * 1000 + int(sss)


def millis_to_time_string(millis):
    """
    :param millis: A time value expressed in millis.
    :return: A time value expressed in HH:MM:SS:.sss
    """
    time_parsed = str(timedelta(milliseconds=millis))
    return f"0{time_parsed[:len(time_parsed) - 3]}"
