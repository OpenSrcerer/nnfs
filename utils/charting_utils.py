from datetime import datetime, timedelta

import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, SecondLocator


def display_chart(table) -> None:
    """
    Display a pretty chart regarding the average lap time for every racer
    summed up by Grand Prix.

    :param table:
    :return: None
    """
    racer_names = []
    racer_times = []

    for name, avg_time in table.yield_summed_lap_times():
        racer_names.append(name.replace(' ', '\n'))
        racer_times.append(datetime.utcfromtimestamp(avg_time // 1000))

    plt.bar(list(range(0, len(racer_names))),
            racer_times,
            tick_label=racer_names,
            width=0.6,
            color=['#FF4E00', '#8EA604', '#650D1B', '#EC9F05', '#3F7CAC'],
            edgecolor=['black'])
    plt.title("Average Lap Times By Driver")
    plt.ylabel('Average Lap Time')
    plt.xticks(rotation=45)

    ax = plt.subplot()
    ax.yaxis.set_major_locator(SecondLocator(bysecond=range(0, 60, 5)))
    ax.yaxis.set_major_formatter(DateFormatter('%H:%M:%S'))
    ax.set_ylim([
        racer_times[0] - timedelta(seconds=10),
        racer_times[-1] + timedelta(seconds=10)
    ])

    plt.tight_layout()
    plt.show()


def num_list_average(number_list: list[int]) -> float:
    """
    :param number_list: List of integers.
    :return: Average of the list.
    """
    avg = 0
    for num in number_list:
        avg += num
    return avg / len(number_list)
