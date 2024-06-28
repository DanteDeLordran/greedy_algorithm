import numpy as np
import time

data = np.genfromtxt('data.csv', delimiter=',', skip_header=1)
W = np.genfromtxt('data.csv', delimiter=',', max_rows=1)

vi = data[:, 0]
wi = data[:, 1]
v = len(vi)


def sort_data(by: int, ascending: bool = False) -> np.ndarray:
    sorted_indices = np.argsort(data[:, by])
    if not ascending:
        sorted_indices = sorted_indices[::-1]
    return data[sorted_indices]


def greedy(local_data: np.ndarray, W):
    T = []
    total_w = 0
    total_v = 0
    for row in local_data:
        if total_w + row[1] <= W:
            T.append(row)
            total_w += row[1]
            total_v += row[0]

    print(f"Total value : {total_v}")
    print(f"Total weight : {total_w}")


def greedy_by_vw(local_data: np.ndarray, W):
    vw_ratio = local_data[:, 0] / local_data[:, 1]
    sorted_indices = np.argsort(vw_ratio)[::-1]
    sorted_data = local_data[sorted_indices]

    T = []
    total_w = 0
    total_v = 0

    for row in sorted_data:
        if total_w + row[1] <= W:
            T.append(row)
            total_w += row[1]
            total_v += row[0]

    print(f"Total value : {total_v}")
    print(f"Total weight : {total_w}")


def main():
    print("Greedy by : ")
    print("1-Highest value")
    print("2-Lowest weight")
    print("3-Highest value by weight")
    option = int(input())

    exec_start = time.process_time()

    match option:
        case 1:
            greedy(sort_data(0, ascending=False), W)
        case 2:
            greedy(sort_data(1, ascending=True), W)
        case 3:
            greedy_by_vw(data, W)
        case _:
            print("Invalid option")
            main()

    exec_end = time.process_time()
    print("Processing time finished at : ", exec_end - exec_start)
    print("Run again ?")
    print("1-Yes")
    print("2-No")
    option2 = int(input())
    if option2 == 1:
        main()


if __name__ == "__main__":
    main()
