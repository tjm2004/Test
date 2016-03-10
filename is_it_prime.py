import sys


maybe_prime = float(int(sys.argv[1]))

lowest_common_denominators = []

def cp(integer):
    x = float(2)
    # integer = float(int(integer,base=10))
    while x < integer:
        if (integer / x).is_integer():
            print '{} is divisible by {}'.format(integer, x)
            lowest_common_denominators.append(x)
            break
        else:
            x = x + 1
            if x == (integer - 1):
                print '{} is PRIME'.format(integer)



if __name__ == "__main__":
    # print "Gonna check if {} is a prime number".format(sys.argv[1])
    # test = cp(sys.argv[1])

    print 'hello'
    def all_primes(integer2):
        # integer2 = int(integer2, base=10)
        print type(integer2)
        while integer2 > 0:
            cp(integer2)
            integer2 = integer2 -1

    test = all_primes(maybe_prime)

    print max(lowest_common_denominators)
