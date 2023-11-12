#!/usr/bin/env python3
# Created by: Santiago Hewett
# Created on: Nov 8, 2023
# This program will ask the user
# for a integer and it will tell them the factorial
# of the number with try catch


def main():
    # Get the user num as a string and display message about program

    print("This program will ask the user for a integer and it will ")
    print("tell them the factorial of that number")
    user_num_string = input("Enter your integer: ")

    # initialize variables
    counter = 1
    factorial = 1

    # Catch if the user num is something wrong

    try:
        # Convert user int as a string to int
        user_num_int = int(user_num_string)

        # Check if user num is negative
        if user_num_int < 0:
            print(
                "{} is a negative number, please enter a positive number".format(
                    user_num_int
                )
            )

        # loop for factorial of user_num_int

        else:
            while True:
                # calculate factorial
                factorial = factorial * counter
                # display how many time it went through the loop

                print("{} time through the loop".format(counter))
                # increment counter

                counter = counter + 1
                if counter > user_num_int:
                    break

            # display factorial to user
            print("{} is the factorial of {}".format(factorial, user_num_int))

    # Display a message to the user if they entered something that is not valid

    except Exception:
        # Message for invalid user input
        print("\n{} is not a valid integer.".format(user_num_string))


if __name__ == "__main__":
    main()
