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


def generate_primes(num):
    """
        Generate a list of prime number less than num.
    """
    plist = []
    pdict = set()

    for i in range(2, num + 1):
        if i not in pdict:
            plist.append(i)
            pdict.update(range(i * i, num + 1, i))

    return plist


def find_polynomial(degree, maxprime, interestingafter):
    """
        Find a polynomial of degree that generate at least interestingAfter from 2 to maxPrime.
    """
    plist = generate_primes(maxprime)
    solution = []
    for coef in plist:
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
                    if evaluate in plist:
                        primes = primes + 1
                    else:
                        break

                if primes > interestingafter:
                    if DEBUG:
                        print 'N:', primes, ' coefs:', coef_list
                    solution.append('N:' +  str(primes) + ' coefs:' + str(coef_list))

    return solution


print find_polynomial(2, 1000, 10)
