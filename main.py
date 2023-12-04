from graphics import *
from utilities import *
from attack import *

def main():
    ergasia = quest()
    resultIO = resultio()
    plaintextsnumber = plaintexts()

    secret_keys = []
    plaintextable = []
    # Input Output Of Plaintexts
    if resultIO == "1":
        ptsize = sizes() # Length Size Indentical Or Random
        # String Random
        if ergasia == "1" or ergasia == "3" or ergasia == "4":
            if ptsize == 2:    # Random String Length Plaintexts
                for _ in range(plaintextsnumber):
                    random_str = generate_random_string_pt()
                    plaintextable.append(random_str)
            elif ptsize >= 5 : # Indentical String Length Plaintexts
                for _ in range(plaintextsnumber):
                    random_str = generate_random_string_otp(ptsize)     # Size of Plaintexts
                    plaintextable.append(random_str)
        # Decimal Random
        else :
            if ptsize == 2 :     # Random Decimals Length Plaintexts
                for _ in range(plaintextsnumber):
                    plaintextable.append(generate_random_length_dec())
            elif ptsize >= 5:  # Indentical Decimals Length Plaintexts
                plaintextable = [generate_random_decimal_pt(ptsize) for _ in range(plaintextsnumber)]
    else:
    # Decimicals or Strings
        # Keyboard Decimals
        if ergasia == "2":
            for i in range(plaintextsnumber):
                while True:
                    try:
                        plaintext = int(input(f"Enter Decimal Plaintext {i + 1}      :  "))
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid decimal number.\n")
                plaintextable.append(plaintext)
        # Keyboard Strings
        elif ergasia == "1" or ergasia == "3" or ergasia == "4":
            plaintextable = [input(f"Enter Plaintext {i + 1}            : ") for i in range(plaintextsnumber)]

    print("------------------------------------------------------------------------------------------------------ ")
    # Generate and print OTP(s)
    if ergasia == "4": #4unbreakable
        for plaintext in plaintextable:
            secret_key = random_mixed_strings(plaintext)  # Remove the extra list
            secret_keys.append(secret_key)
        for i, secretkey in enumerate(secret_keys, start=1):# start=1 for the print prupose of the arrays
            print(f"The Secret Key {i}               :  {secretkey}")
    else:
        secret_keys=[otpad()]
        # Print the OTP
        print("\nThe OTP For The Encryption is  : ", secret_keys[0], "")
    #Print Plaintexts
    print(" ")
    for i, plaintext in enumerate(plaintextable, start=1):# start=1 for the print prupose of the arrays
        print(f"The Plaintext {i}                :  {plaintext}")
    # Call attack function
    result_ptexts = cryptanalysis_attack(plaintextable,secret_keys,ergasia)
    print("\n")
    loading4fun()
    print("\n")
    if ergasia =="4":
        for i, decryptedpt in enumerate(result_ptexts, start=1):# start=1 for the print prupose of the arrays
            print(f"The Encrypted Plaintext {i}      :  {decryptedpt}")
    elif ergasia == "2" or ergasia == "3":
        for i, decryptedpt in enumerate(result_ptexts):
            print(f"The Possible Plaintexts        :  {decryptedpt}")
    else:
        for i, decryptedpt in enumerate(result_ptexts, start=1):# start=1 for the print prupose of the arrays
            print(f"The Decrypted Plaintexts {i}     :  {decryptedpt}")

if __name__ == "__main__":
    main()