import sys

flag = "ENIT{Eas!_py_Ja!L}"

def restricted_exit():
    print("Exiting the jail... Here's your flag: " + flag)
    sys.exit(0)

def main():
    print("Welcome to the Python jail challenge!")
    print("You need to escape the jail")

    while True:
        try:
            command = input("Enter a command: ")
            if command.strip().lower() == 'exit()':
                restricted_exit()
            else:
                print("Command not allowed.")
        except EOFError:
            print("Exiting the jail... Here's your flag: " + flag)
            sys.exit(0)

if __name__ == "__main__":
    main()
