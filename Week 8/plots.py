import matplotlib.pyplot as plt

def display_line(x_values, z_values):
    plt.xlabel("x values")
    plt.ylabel("y values")
    plt.plot(x_values, z_values)
    plt.show()

def run_task1():
    x = [1, 2, 3, 4, 5]
    z = [1, 4, 9, 16, 25]
    display_line(x, z)

run_task1()
