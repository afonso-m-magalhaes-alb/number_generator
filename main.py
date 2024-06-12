import random
import sys

def generate(args):
    print(random.randint(1, args[0]))

if __name__ == '__main__':
    generate(sys.argv[1:])
