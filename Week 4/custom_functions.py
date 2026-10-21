# Defined the requested function
from urllib import response


def listen_function():

    # Prompt user for what sound he heard
    print("What sound did you hear?")
    sound = input()
    print(f"That was a loud {sound} !")


# Call the function
listen_function()


def identify():
# Ask user for what he sees ahead
    print("What do you see ahead ?")
    response = input()


# Display message
    if response.lower() == "a large boulder":
        print("It's time to run!")
    else:
        print("We will be fine.")

# Call to function
identify()