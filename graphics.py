import random
import string
from utilities import *
from utilities import generate_random_string_otp


def loading4fun(duration=3):
    """Loading for fun"""
    sym = ['.', '..', '...', '....', '.....', '......', '.......', '........', '.........', '..........', '...........']
    i = 0
    start_time = time.time()

    while True:
        elapsed_time = time.time() - start_time

        # Break out of the loop after the specified duration
        if elapsed_time > duration:
            print('\r\033[KDecryption Completed!', flush=True, end='')
            break
        i = (i + 1) % len(sym)
        print('\r\033[KDecrypt Plaintexts...%s' % sym[i], flush=True, end='')
        time.sleep(0.2)
        i += 1

def quest():
    while True:
        print(" _____________________________________________________________________________________________________")
        print("|                                           QUEST                                                     |")
        print("|-----------------------------------------------------------------------------------------------------|")
        print("|                                       MANNY TIME PAD                                                |")
        print("|-----------------------------------------------------------------------------------------------------|")
        print("|* Quest   1        --->   (1)    * STRING PLAINTEXTS WITH KNOWN PLAINTEXT 1                          |")
        print("|* Quest   2        --->   (2)    * DECIMICAL PLAINTEXTS WITH UNKNOWN PLAINTEXT                       |")
        print("|* Quest   3        --->   (3)    * STRING PLAINTEXTS WITH UNKNOWN PLAINTEXT (BONUS)                  |")
        print("|-----------------------------------------------------------------------------------------------------|")
        print("|                                        ONE TIME PAD                                                 |")
        print("|-----------------------------------------------------------------------------------------------------|")
        print("|* Quest   4        --->   (4)    * UNBREAKABLE METHOD (BONUS)                                        |")
        print("|_____________________________________________________________________________________________________|")
        choice = input("Your Choice Is : ")
        print("")
        if choice == "1":
            return "1"
        elif choice == "2":
            return "2"
        elif choice == "3":
            return "3"
        elif choice == "4":
            return "4"
        else:
            print("Invalid choice. Please try again.")

def sizes():
    while True:
        print(" _____________________________________________________________________________________________________")
        print("|                                           LENGTH                                                    |")
        print("|-----------------------------------------------------------------------------------------------------|")
        print("|* CHOOSE   1        --->   (1)   * INDENTICAL LENGTHS PLAINTEXTS (>5)                                |")
        print("|* CHOOSE   2        --->   (2)   * RANDOM LENGTHS PLAINTEXTS                                         |")
        print("|_____________________________________________________________________________________________________|")
        choice = int(input("Your Choice Is : "))
        print("")
        if choice == 1 :
            while True:
                try:
                    number = int(input("Please Give The Lenght Of The Plaintexts : "))
                    if number >= 5:
                        print("------------------------------------------------------------------------------------------------------\n")
                        return number
                    else:
                        print("Invalid Plaintext Length. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.\n")
        elif choice == 2 :
            return choice
        else:
            print("Invalid choice. Please try again.")

def resultio():
    while True:
        print(" _____________________________________________________________________________________________________")
        print("|                                       BORING OR NOT ?                                               |")
        print("|-----------------------------------------------------------------------------------------------------|")
        print("|* AUTO            --->    (1)    * AUTOMATED METHOD (RANDOM INPUTS)                                  |")
        print("|* MANUAL          --->    (2)    * MANUAL METHOD    (MANUAL INPUTS)                                  |")
        print("|_____________________________________________________________________________________________________|")
        choice = input("Your Choice Is : ")
        print("")
        if choice == "1":
            return "1"
        elif choice == "2":
            return "2"
        else:
            print("Invalid choice. Please try again.")

def plaintexts():
    while True:
        print(" _____________________________________________________________________________________________________")
        print("|                                     HOW MANNY PLAINTEXT                                             |")
        print("|-----------------------------------------------------------------------------------------------------|")
        print("|                                   Tip : Choose 2 or more                                            |")
        print("|_____________________________________________________________________________________________________|\n")
        print("------------------------------------------------------------------------------------------------------")
        while True:
            try:
                number = input("Enter The Number Of Plaintexts : ")
                number = int(number)  # Convert input to int
                # Check if the number is 2 or more
                if number >= 2:
                    break  # If the input is valid, exit the loop
                else:
                    print("Number must be 2 or more. Please try again.\n")
            except ValueError:
                print("Invalid input. Please enter a valid number.\n")
        print("------------------------------------------------------------------------------------------------------\n")
        return number


def otpad():
    while True:
        print(" _____________________________________________________________________________________________________ ")
        print("|                                        ONE TIME PAD                                                 |")
        print("|-----------------------------------------------------------------------------------------------------|")
        print("|* Random OTP       --->  (1)                                                                         |")
        print("|* Non Random OTP   --->  (2)                                                                         |")
        print("|_____________________________________________________________________________________________________|")
        choice = input(" Your Choice Is : ")
        print("")

        if choice == "1":
            print(" ----------------------------------------------------------------------------------------------------- ")
            while True:
                try:
                    lenghtnum = input(" Enter The Lenght Of OTP: ")
                    number = int(lenghtnum)  # Convert input to int
                    print(" ----------------------------------------------------------------------------------------------------- ")

                    break                    # If conversion is successful, exit the loop
                except ValueError:
                    print("Invalid input. Please enter a valid number.\n")
            secret_key = generate_random_string_otp(number)
            return secret_key

        elif choice == "2":
            secret_key = input(" Enter the OTP  : ")
            print(" ____________________________________________________________________________________________________")

            return secret_key

        else:
            print("Invalid choice. Please try again.")
