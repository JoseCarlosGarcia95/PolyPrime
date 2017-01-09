import sys
from random import randrange
"""
* Copyright (C) 2016 josec
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

"""
    Generate a polynomial that generate an amount of primes.
"""

DEBUG = True

current_num = 3

def get_next_prime():
    global current_num
    current_num = current_num + 2
    while not is_prime(current_num):
        current_num = current_num + 2
    return current_num
    

small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31] # etc.
def is_prime(n):
    """Return True if n passes k rounds of the Miller-Rabin primality
    test (and is probably prime). Return False if n is proved to be
    composite.

    """
    k = 5
    if n < 2: return False
    for p in small_primes:
        if n < p * p: return True
        if n % p == 0: return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def find_polynomial(degree, interestingafter, filename):
    """
        Find a polynomial of degree that generate at least interestingAfter from 2 to maxPrime.
    """
    f = open(filename, "w")
    while 1 == 1:
        coef = get_next_prime()
        coef_list = []
        coef_list.append(coef)

        for i in range(0, degree):
            coef_list.append(0)

        for i in range(0, coef_list[0] ** degree):
            for j in range(0, degree):
                coef_list[j + 1] = i / coef_list[0] ** j % coef_list[0]
            if coef_list[degree] != 0:
                primes = 0
                for k in range(0, coef_list[0]):
                    evaluate = 0
                    for j in range(0, degree + 1):
                        evaluate = evaluate + coef_list[j] * k ** j
                    if is_prime(evaluate):
                        primes = primes + 1
                    else:
                        break

                if primes > interestingafter:

                    if DEBUG:
                        print 'N:', primes, ' coefs:', coef_list
                    f.write('N:' +  str(primes) + ' coefs:' +  str(coef_list) + "\n")
                    f.flush()

if __name__ == "__main__":
    if sys.argv.count < 4:
        print "Invalid arguments"
        exit(-1)

    degree = int(sys.argv[1])
    logafter = int(sys.argv[2])
    filename = sys.argv[3]

    find_polynomial(degree, logafter, filename)
