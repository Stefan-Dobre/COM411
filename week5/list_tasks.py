def directions():
    steps = ["Move forward", "Move backward", "Turn left", "Turn right"]
    return steps

def run_task1():
    print(directions())

if __name__ == "__main__":
    run_task1()
# task 1 simple list


def movements():
    path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path

def run_task2():
    print("Moving...")
    path = movements()
    print(f"{path[0]} for {path[1]} steps")
    print(f"{path[2]} for {path[3]} steps")
    print(f"{path[4]} for {path[5]} steps")
    print(f"{path[6]} for {path[7]} steps")
if __name__ == "__main__":
    run_task2()


def directions():
    steps = ["Move Forward", "Move Backward", "Turn Left" "Turn Right"]
    return steps

def menu():
    print("Please select an option")
    dirs = directions()
    for index in range(len(dirs)):
        print(f"{index}: {dirs[index]}")

def run_task3():
    menu()
