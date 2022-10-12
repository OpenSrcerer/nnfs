from datetime import timedelta

def time_string_to_millis(stringified_time):
    time = stringified_time.split(':')
    h, m = (time[0], time[1])
    s, sss = time[2].split('.')
    return int(h) * 3_600_000 + int(m) * 60_000 + int(s) * 1000 + int(sss)


def millis_to_time_string(millis):
    time_parsed = str(timedelta(milliseconds=millis))
    return f"0{time_parsed[:len(time_parsed) - 3]}"
