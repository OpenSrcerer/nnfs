import matplotlib.pyplot as plt


def display_chart(table):
    racer_names = []
    racer_times = []

    for name, avg_time in table.yield_summed_lap_times():
        racer_names.append(name)
        racer_times.append(avg_time)

    left_coordinates = [1, 2, 3, 4, 5]
    plt.bar(left_coordinates, racer_times, tick_label=racer_names, width=0.6, color=['red', 'black'])
    plt.xlabel('Racers')
    plt.ylabel('Average Lap Time')
    plt.title("A simple bar graph")
    plt.show()


def num_list_average(number_list: list[int]):
    avg = 0
    for num in number_list:
        avg += num
    return avg / len(number_list)
