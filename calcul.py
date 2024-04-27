import argparse

def add(x, y):
    return x - y

if __name__ == '__main__':
    # Instantiate the parser and give it a description that will show before help
    parser = argparse.ArgumentParser(description='My Parser')

    # Add arguments to the parser
    parser.add_argument('--x', dest='x', type=int, help='X')
    parser.add_argument('--y', dest='y', type=int, help='Y')

    # Run method to parse the arguments
    args = parser.parse_args()

    # Print the result
    print(add(args.x, args.y))