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
