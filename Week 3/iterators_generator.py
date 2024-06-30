class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if self.current < 1:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value
def fibonacci_generator(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b
def random_number_generator(start, end, count):
    import random
    for _ in range(count):
        yield random.randint(start, end)
def main():
    # Create a Countdown iterator that counts down from 7 to 1
    countdown = Countdown(7)
    print("Countdown:")
    for num in countdown:
        print(num)
    # Check if the limit is a positive number for fibonacci_generator
    limit = 100
    if limit > 0:
        print("\nFibonacci numbers up to", limit, ":")
        for num in fibonacci_generator(limit):
            print(num)
    else:
        print("Invalid limit for fibonacci_generator. Please enter a positive number.")
    # Check if the range is valid for random_number_generator
    start = 1
    end = 5
    count = 5
    if start <= end:
        print("\nRandom numbers between", start, "and", end, ":")
        for num in random_number_generator(start, end, count):
            print(num)
    else:
        print("Invalid range for random_number_generator. Please enter a valid range.")


if __name__ == "__main__":
    main()