import random
import time
import matplotlib.pyplot as plt


def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)


def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)


def measure_time(sort_function, arr, repetitions=5):
    total_time = 0
    for _ in range(repetitions):
        array_copy = arr.copy()
        start_time = time.perf_counter()
        sort_function(array_copy)
        total_time += time.perf_counter() - start_time
    return total_time / repetitions


if __name__ == "__main__":
    sizes = [10000, 50000, 100000, 500000]
    random_quick_times = []
    deterministic_quick_times = []

    for size in sizes:
        data = [random.randint(0, 1000000) for _ in range(size)]

        rand_time = measure_time(randomized_quick_sort, data)
        det_time = measure_time(deterministic_quick_sort, data)

        random_quick_times.append(rand_time)
        deterministic_quick_times.append(det_time)

        print(f"Розмір масиву: {size}")
        print(f"   Рандомізований QuickSort: {rand_time:.4f} секунд")
        print(f"   Детермінований QuickSort: {det_time:.4f} секунд\n")

    plt.plot(sizes, random_quick_times, label="Рандомізований QuickSort")
    plt.plot(sizes, deterministic_quick_times, label="Детермінований QuickSort")
    plt.xlabel("Розмір масиву")
    plt.ylabel("Середній час виконання (секунди)")
    plt.title("Порівняння рандомізованого та детермінованого QuickSort")
    plt.legend()
    plt.grid(True)
    plt.show()
