def fizzbuzz(start, end):
    for i in range(start, end):
        if i%5 == 0 and i%3 ==0:
            print("fizzbuzz")
        elif i%5 == 0:
            print("buzz")
        elif i%3 == 0:
             print("fizz")
        else:
            print(i)


# Don't Touch Below This Line


def main():
    test(1, 100)
    test(5, 30)
    test(1, 15)


def test(start, end):
    print("Starting test")
    fizzbuzz(start, end)
    print("======================")


main()