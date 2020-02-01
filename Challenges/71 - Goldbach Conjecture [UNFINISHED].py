def goldbach_conj(number):
    x, y = 0, 0
    result = 0
    if not number % 2:
        prime_list = list_of_primes(number)
        while result != number:
            for i in range(len(prime_list)):
                x = prime_list[i]
                if result == number: break
                for j in range(len(prime_list)):
                    y = prime_list[j]
                    result = x + y
                    print("Adding {} and {}.".format(x, y))
                    print("Result is {}".format(result))
                    if result == number: break
    return x, y 




def is_prime(number):
    if number % 2:
        # equivalent to if number % 2 != 0 because if number is
        # divisible by 2 it will return 0, evaluating as 'False'.
        for num in range(3, int(math.sqrt(number)) + 1, 2):
            if number % num == 0:
               return False
        return True
    else:
        return False



def list_of_primes(number):
    prime_list = []
    for x in range(2, number + 1):
            if is_prime(x):
                prime_list.append(x)
    return prime_list



def main():
    while True:
        usr_in = eval(input("Please enter a positive number"
                            " greater than 1: "))
        if usr_in > 1: break
        else:
            print("Number not valid.")

    prime_list = goldbach_conj(usr_in)
    print(prime_list)
    # prime_list = list_of_primes(usr_in)
    # for x in prime_list:
    #     print(x)


if __name__ == '__main__':
    main()
