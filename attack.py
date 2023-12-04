from graphics import *
from utilities import *
from onetimepad import encrypt, decrypt
def cryptanalysis_attack(table, otp, ergasia):
    """Perform the cryptanalysis attack."""
    template = ergasia
    binary_ciphertexts = []


    if template == "1" :
        """
        STRING PLAINTEXTS WITH KNOWN PLAINTEXT 2
        """
        # Convert Strings To Binary
        binary_plaintexts = [string_to_ascii_binary(plaintext) for plaintext in table]
        key = string_to_ascii_binary(otp[0])
        # XORing For Result Ciphertext
        for plaintext in binary_plaintexts:
            current_result = xor_2strings(plaintext,key)
            binary_ciphertexts.append(current_result)
        """
        That will accept for the attack ... the Ciphertexts in Binary
        with exposed plaintext2
        """
        binary_exp_ciphertexts=[]
        # We XOR the exposed plaintext2 with the ciphertext2 and we expose the key
        justhekey = xor_2strings(binary_plaintexts[1], binary_ciphertexts[1])
        for plaintext in binary_ciphertexts:
            current_result = xor_2strings(plaintext,justhekey)
            binary_exp_ciphertexts.append(current_result)

        # # Xor all the pairs in binary form
        # otp_exposed = [xor_strings(elem1, elem2) for elem1, elem2 in zip(binary_plaintexts, binary_ciphertexts)]
        # #Xor all the plaintexts with the plaintext 1 exposed key
        # binary_exposed_plaintexts = [xor_strings(plaintextexpose, otp_exposed[0]) for plaintextexpose in binary_ciphertexts]
        # # Convert all the decrypted binary plaintexts to string
        plaintexts = [binary_2_ascii(convertedpt) for convertedpt in binary_exp_ciphertexts]
        return plaintexts
    elif template == "2":
        """
        DECIMICAL PLAINTEXTS WITH UNKNOWN PLAINTEXTS
        """
        binary_int_plaintexts = [string_to_ascii_binary(plaintexts) for plaintexts in table]
        # Manny time OTP = 1 KEY (otp[0])
        key = string_to_ascii_binary(otp[0])
        # for i, value in enumerate(binary_int_plaintexts, 1):
        #     print(f"{i}. {value}")
        # print("KEY IS : ",key,"\n")

        # Chaining XOR encrypt an array of ASCII binary plaintexts using a key.
        # :plaintexts: List of ASCII binary plaintexts
        # :key: ASCII binary key
        # :return: List of ASCII binary ciphertexts

        for plaintext in binary_int_plaintexts:
            current_result = xor_binary_strings(plaintext,key)
            binary_ciphertexts.append(current_result)

        # That will accept for the attack ... the Ciphertexts in Binary
        result_array = []

        # Iterate over all possible pairs
        for i in range(len(binary_ciphertexts)):
            for j in range(i + 1, len(binary_ciphertexts)):
                # XOR the binary sequences
                xor_result = xor_binary_strings(binary_ciphertexts[i], binary_ciphertexts[j])
                # Add zeros to make the length a multiple of 8
                xor_result += '0' * (8 - len(xor_result) % 8)
                # Add the XOR result to the result array
                result_array.append(xor_result)

        # # # Iterate over all possible triplets and more
        # for i in range(len(binary_ciphertexts)):
        #     for j in range(i + 1, len(binary_ciphertexts)):
        #         for k in range(j + 1, len(binary_ciphertexts)):
        #             # XOR the binary sequences
        #             xor_result = ''.join(str(int(x) ^ int(y) ^ int(z)) for x, y, z in
        #                                  zip(binary_ciphertexts[i], binary_ciphertexts[j], binary_ciphertexts[k]))
        #             # Add zeros to make the length a multiple of 8
        #             xor_result += '0' * (8 - len(xor_result) % 8)
        #             # Add the XOR result to the result array
        #             result_array.append(xor_result)
        # for i, value in enumerate(result_array, 1):
        #     print(f"{i}. {value}")

        # # Convert decrypted binary to decimal
        plaintexts = [binary_2_ascii(binaries) for binaries in result_array]
        # for i, value in enumerate(plaintexts, 1):
        #     print(f"{i}. {value}")
        # print("")
        # scrap the values
        numberplaintexts = process_ascii_array(plaintexts)

        return numberplaintexts
    elif ergasia =="3":
        """
        STRING PLAINTEXTS WITH UNKNOWN PLAINTEXT (BONUS)
        """
        binary_plaintexts = [string_to_ascii_binary(plaintexts) for plaintexts in table]
        # Manny time OTP = 1 KEY (otp[0])
        key = string_to_ascii_binary(otp[0])


        for plaintext in binary_plaintexts:
            current_result = xor_2strings(plaintext, key)
            binary_ciphertexts.append(current_result)

        """
        That will accept for the attack ... the Ciphertexts in Binary
        """
        result_array = []

        # Iterate over all possible pairs
        for i in range(len(binary_ciphertexts)):
            for j in range(i + 1, len(binary_ciphertexts)):
                # XOR the binary sequences
                xor_result = xor_2strings(binary_ciphertexts[i], binary_ciphertexts[j])
                # Add zeros to make the length a multiple of 8
                xor_result += '0' * (8 - len(xor_result) % 8)
                # Add the XOR result to the result array
                result_array.append(xor_result)

        # # # Iterate over all possible triplets and more
        for i in range(len(binary_ciphertexts)):
            for j in range(i + 1, len(binary_ciphertexts)):
                for k in range(j + 1, len(binary_ciphertexts)):
                    # XOR the binary sequences
                    xor_result = xor_2strings(binary_ciphertexts[i], binary_ciphertexts[j])
                    xor_result = xor_2strings(xor_result, binary_ciphertexts[k])
                    # Add zeros to make the length a multiple of 8
                    # xor_result += '0' * (8 - len(xor_result) % 8)
                    # Add the XOR result to the result array
                    result_array.append(xor_result)
        # for i, value in enumerate(result_array, 1):
        #     print(f"{i}. {value}")

        # # Convert decrypted binary to decimal
        plaintexts = [binary_to_ascii(binaries) for binaries in result_array]
        # for i, value in enumerate(plaintexts, 1):
        #     print(f"{i}. {value}")
        # print("")
        # scrap the values
        numberplaintexts = process_ascii_array(plaintexts)

        return numberplaintexts
    else:
        """
        UNBREAKABLE METHOD (BONUS) 
        """
        # using the onetimepad import encrypt, decrypt library
        ciphertexts=[]
        # XOR for every corresponding pair in two arrays
        for message, key in zip (table, otp):
            ciphertext = encrypt(message,key)
            ciphertexts.append(ciphertext)
        # uncomment for decrypt
        # for i, cipher in enumerate(ciphertexts, start=1):
        #     print(f"The Encrypted Plaintext {i}     :  {cipher}")
        # print("")
        # plaintexts = [decrypt(message, key) for message, key in zip(ciphertexts, otp)]
        return ciphertexts

