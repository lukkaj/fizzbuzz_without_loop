# Implementing fizzbuzz without loops or if else structure
# Just for fun

def elegant_fizzbuzz(n):
    res = "Fizz" * (n % 3 == 0) + "Buzz" * (n % 5 == 0)
    return res or n


def main():
    fizzbuzzlist = (range(1, 101))
    print(list(map(elegant_fizzbuzz, fizzbuzzlist)))


if __name__ == '__main__':
    main()
