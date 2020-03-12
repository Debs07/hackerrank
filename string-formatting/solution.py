def print_formatted(number):
    space = len(f"{number+0:b}")
    for i in range(1,number+1):
        print(f"{i+0:{space}d} {i+0:{space}o} {i+0:{space}X} {i+0:{space}b}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
