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




def small():
    x = [3, 3, 4, 4, 3]
    y = [3,4, 4, 3, 3]
    plt.plot(x, y, 'ro--')



def medium():
    x = [2, 2, 5, 5, 2]
    y = [2, 5, 5, 2, 2]
    plt.plot(x, y, 'g--s')

def large():
    x = [1, 1, 6, 6, 1]
    y = [1, 6, 6, 1, 1]
    plt.plot(x, y, 'b-p')

def task_3():
     small()
     medium()
     large()
     plt.show()

task_3()
