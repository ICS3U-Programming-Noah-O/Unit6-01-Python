#!/usr/bin/env python3
# Created By: Noah Ouellette
# Date: Jan. 27, 2022
# This program generates a list of random numbers
# and then calculates the average of all of those numbers

import random
import time


def main():
    list_of_int = []
    total = 0

    for counter in range(10):
        # Generate random number and add it to the list
        rand_num = random.randint(0, 99)
        total = total + rand_num
        list_of_int.append(rand_num)
        # print(list_of_int)
        print("{} added to the list at position {}.".format(
            rand_num, counter + 1))
    total = total / 10
    # Print the total
    print(" ")
    print("The average is {}.".format(total))


if __name__ == "__main__":
    main()
