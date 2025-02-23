import numpy as np
import matplotlib.pyplot as plt
from timeit import timeit

def np_pixel_grid(point_a, point_b, res_b, point_c, res_c):

    vec_b = point_b - point_a
    vec_c = point_c - point_a

    shift_b = vec_b / (res_b-1)
    shift_c = vec_c / (res_c-1)
    vectors = np.array([shift_b, shift_c])
    index_array = np.indices((res_b, res_c)).transpose(1, 2, 0)
    array = point_a + np.sum((index_array[..., np.newaxis] * vectors), axis=-2)

    return np.array(array)

def py_pixel_grid(point_a, point_b, res_b, point_c, res_c):

    vec_b = point_b - point_a
    vec_c = point_c - point_a

    shift_b = vec_b / (res_b-1)
    shift_c = vec_c / (res_c-1)
    points = []
    for i in range(0, res_b):
        row = []
        row_first = point_a + (shift_b * i)
        for j in range(0, res_c):
            row.append(row_first + (shift_c * j))

        points.append(row)

    return np.array(points)

def raster():
    a = np.array([-20, -5, 20])
    b = np.array([-20, -5, -20])
    c = np.array([20, -5, 20])

    number = 10
    py_times = []
    np_times = []
    resolutions = []
    skalar = 100
    for i in range(1, 21):
        resolution = i * skalar
        resolutions.append(resolution*resolution)
        py_time = timeit(lambda: py_pixel_grid(a, b, resolution, c, resolution), number=number)/number
        py_times.append(py_time)

        np_time = timeit(lambda: np_pixel_grid(a, b, resolution, c, resolution), number=number)/number
        np_times.append(np_time)

    plt.plot(resolutions, py_times, label = "python")
    plt.plot(resolutions, np_times, label = "numpy")
    plt.xlabel("Insgesamte Anzahl an Pixel")
    # plt.xticks(range(0, max(resolutions)+1, skalar))
    plt.ylabel("Zeit in s")
    plt.ylim(bottom=0)
    plt.xlim(left=(skalar*skalar))
    plt.xscale("log")
    plt.grid()
    plt.legend()
    plt.show()

if __name__ == "__main__":
    raster()