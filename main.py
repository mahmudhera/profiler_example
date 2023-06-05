import time
import argparse

@profile
def slow_function(x):
    x = x + 1
    time.sleep(1)
    x = x**2
    return x

def fast_function(x):
    x = x + 1
    x = x**2
    return x

def main():
    parser = argparse.ArgumentParser(description='Takes an integer as CLA, finds its f(), and prints it.')
    parser.add_argument('number', type=int, help='The argument.')

    args = parser.parse_args()
    x = args.number

    for i in range(5):
        print(slow_function(x))
        print(fast_function(x))

if __name__ == '__main__':
    main()
