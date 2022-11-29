#implemets the game called "little professor," a basic algebra game. 
import random
import sys


def main():
    counter = 0
    attempt = 0
    level = get_level()
    while True:
        x = (generate_integer(level))
        mistake = 0
        try:
            while True:
                attempt += 1
                print(x[0], "+", x[1], "= ", end="")
                y = int(input())
                if y == (x[0] + x[1]):
                    counter += 1
                    if attempt < 10:
                        break
                    else:
                        print("Score: ", counter)
                        sys.exit()
                else:
                    print("EEE")
                    mistake += 1
                    if mistake > 2:
                        print(x[0], "+" , x[1], "=", (x[0] + x[1]))
                        attempt -= 2
                        break
        except ValueError:
            print("EEE")