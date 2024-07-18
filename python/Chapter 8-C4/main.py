def is_prime(number):
    k = 0

    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0 and number != i:
            k += 1

    if k != 0:
        return False
    else:
        return True