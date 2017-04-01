import os
from random import randrange
from fractions import gcd

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

class PolyPrime:
    def __init__(self, degree, m):
        # Degree of the polynomial.
        self.degree = degree

        # Report if generate at least m primes.
        self.m = m

        # Cache filename
        self.cache_filename = "results/cache-{}-{}".format(self.degree, self.m)

        # Output filename
        self.output_filename = "results/output-{}-{}".format(self.degree, self.m)
        
        # Read from cache
        self.readFromCache()
        
    def readFromCache(self):
        self.n = 3
        
        if os.path.exists(self.cache_filename):
            cache_coef = open(self.cache_filename, "r")
            self.n = int(cache_coef.read())
            cache_coef.close()
        
    
    # Generate the most near prime.
    def get_next_prime(self):
        self.n = self.n + 2
        while not self.is_prime(self.n):
            self.n = self.n + 2
        return self.n

    # Check if prime or not
    def is_prime(self, n):
        small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31] # etc.    
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

    def findPolynomial(self):
        io_output = open(self.output_filename, "a")
        cache_coef = open(self.cache_filename, "w")

        while 1 == 1:
            coef = self.get_next_prime()

            coef_list = []
            coef_list.append(coef)
            
            for i in range(0, self.degree):
                coef_list.append(0)

            for i in range(0, coef_list[0] ** self.degree):
                for j in range(0, self.degree):
                    coef_list[j + 1] = i / coef_list[0] ** j % coef_list[0]

                if coef_list[self.degree] != 0:
                    primes = 0

                    # Definition.
                    for k in range(0, coef_list[0]):
                        evaluate = 0
                        for j in range(0, self.degree + 1):
                            evaluate = evaluate + coef_list[j] * k ** j
                        if self.is_prime(evaluate):
                            primes = primes + 1
                        else:
                            break

                    if primes > self.m:
                        polynomial_form = "p(x)="
                            
                        for i in range(0, self.degree+1):
                            if i > 0:
                                polynomial_form = polynomial_form + "+"
                                polynomial_form = polynomial_form + str(coef_list[i]) + "x^{}".format(i)
                            else:
                                polynomial_form = polynomial_form + str(coef_list[i])

                        if(DEBUG):
                            print "Saving ", polynomial_form
                        io_output.write(str(primes) + "|" + polynomial_form + "\n")
                        io_output.flush()

            cache_coef.seek(0)
            
            cache_coef.write(str(coef))
            cache_coef.flush()
            
        cache_coef.close()
        io_output.close()
            


pp = PolyPrime(1, 8)
pp.findPolynomial()
