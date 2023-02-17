value = 0
choice = 0


def take_input():
    while True:
        try:
            global value
            value = float(input("Enter the value to convert: "))
            break
        except(RuntimeError, TypeError, NameError, ValueError):
            print("Something went wrong.")


def make_convert_choice():
    text = """Enter the number 1, if you want to convert to Celsius
or number 2 if you want to convert to Fahrenheit. """
    global choice
    choice = int(input(text))


def print_result():
    match choice:
        case 1:
            print("The temperature is %.2f Celsius." % convert_to_celsius(value))
        case 2:
            print("The temperature is %.2f Fahrenheit." % convert_to_fahrenheit(value))
        case _:
            print("No valid number given.")


def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0 / 9.0


def convert_to_fahrenheit(celsius):
    return celsius * 9.0 / 5.0 + 32


if __name__ == "__main__":
    print("Welcome to Celsius-Fahrenheit Converter")
    take_input()
    make_convert_choice()
    print_result()
