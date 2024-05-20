import matplotlib.pyplot as plt


def manchester_encode(data):
    encoded_data = []
    for bit in data:
        if bit == 0:
            encoded_data.extend([1, -1])
        else:
            encoded_data.extend([-1, 1])
    return encoded_data


def ami_encode(data):
    encoded_data = []
    last_bit = 1  # Начинаем с положительного импульса
    for bit in data:
        if bit == 0:
            encoded_data.extend([0, 0])  # Нулевой бит кодируется нулевым уровнем напряжения
        else:
            encoded_data.extend([last_bit, last_bit])
            last_bit = -last_bit  # Смена знака для каждой единицы
    return encoded_data


def rz_encode(data):
    encoded_data = []
    for bit in data:
        if bit == 0:
            encoded_data.extend([-1, 0])  # Нулевой бит кодируется двумя нулевыми уровнями
        else:
            encoded_data.extend([1, 0])  # Единица кодируется положительным и отрицательным импульсом
    return encoded_data


def nrz_encode(data):
    encoded_data = []
    for bit in data:
        if bit == 0:
            encoded_data.extend([-1, -1])  # Нулевой бит кодируется двумя нулевыми уровнями
        else:
            encoded_data.extend([1, 1])  # Единица кодируется положительным и отрицательным импульсом
    return encoded_data


def dif_m2_encode(data):
    encoded_data = []
    previous_bit = 1
    for bit in data:
        if bit == 0:
            encoded_data.extend([1 if previous_bit == 0 else -1, -1 if previous_bit == 0 else 1])
        else:
            encoded_data.extend([-1 if previous_bit == 0 else 1, 1 if previous_bit == 0 else -1])
            previous_bit = 1 if previous_bit == 0 else 0
    return encoded_data


def plot(data):
    methods = [manchester_encode, ami_encode, rz_encode, nrz_encode, dif_m2_encode]
    fig, axes = plt.subplots(5, 1, sharey=True)

    for method, ax in enumerate(axes):
        encoded_data = methods[method](data)
        for i in range(len(data)):
            if data[i] == 1:
                ax.bar(i * 4 + 2, height=2, width=4, bottom=-1, color=(0.1, 0.5, 1, 0.5))
            else:
                ax.bar(i * 4 + 2, height=2, width=4, bottom=-1, color=(1, 0.3, 0.1, 0.5))

        for i in range(len(data)):
            ax.text(i * 4 + 2, 1.4, str(data[i]), fontsize=12, verticalalignment='center', horizontalalignment='center')

        ax.step(range(0, len(encoded_data) * 2, 2), encoded_data, color="black", where='post', linewidth=2)

        plt.ylim(-1.5, 2)

        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        ax.grid(True)

    plt.show()


def scrambling(data, use_last=[]):
    new_data = []

    for i in range(len(data)):
        v = data[i]

        for last in use_last:
            if i >= last:
                v += new_data[i - last]
        new_data.append(v % 2)

    return new_data


data = [1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
data = [1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1]
plot(data)

exit(0)

scrams = [[5, 7]]
for scram in scrams:
    scramed = scrambling(data, scram)
    begin_pt = 0
    end_pt = 0
    max_len = 0
    last = scramed[0]
    for i in range(len(data)):
        if last == scramed[i]:
            end_pt = i
        else:
            last = scramed[i]
            max_len = max(max_len, end_pt - begin_pt)
            begin_pt = i

    print(scramed)
    print("Max len = {}, scram = {}".format(max_len, scram))

