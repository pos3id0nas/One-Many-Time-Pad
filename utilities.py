import random
import string
import time
from graphics import *
from itertools import combinations

def binary_2_ascii(binary_str):
    """Convert binary string to ASCII string."""
    cleaned_binary_str = binary_str.replace('\x00', '')  # Remove null bytes
    ascii_str = ''.join(chr(int(cleaned_binary_str[i:i + 8], 2)) for i in range(0, len(cleaned_binary_str), 8))
    readable_ascii_str = ''.join(char for char in ascii_str if char.isprintable())
    return readable_ascii_str
def binary_to_ascii(binary_str):
    """Convert binary string to ASCII string."""
    # Remove non-binary characters from the binary string
    cleaned_binary_str = ''.join(bit for bit in binary_str if bit in ('0', '1'))

    # Ensure the length of the cleaned binary string is a multiple of 8
    cleaned_len = len(cleaned_binary_str)
    extra_bits = cleaned_len % 8
    if extra_bits != 0:
        cleaned_binary_str = cleaned_binary_str[:cleaned_len - extra_bits]

    # Convert cleaned binary string to ASCII string
    ascii_str = ''.join(chr(int(cleaned_binary_str[i:i + 8], 2)) for i in range(0, len(cleaned_binary_str), 8))

    # Remove non-printable characters from the ASCII string
    readable_ascii_str = ''.join(char for char in ascii_str if char.isprintable())

    return readable_ascii_str
def string_to_ascii_binary(digits_string):
    binary_list = [bin(int(ord(char)))[2:].rjust(8, '0') for char in str(digits_string)]
    binary_string = ''.join(binary_list)
    return binary_string
def random_mixed_strings(s):
    """ Generate a random mixed (a-w, A-W, 0-9) string with the same length as the original string (s.len == plaintext.len )"""
    mixed_string = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(len(s)))
    return mixed_string
def generate_random_string_otp(length):
    """Random Generator For The String Key == length."""
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string
def generate_random_string_pt():
    """ # Generate a random string with the specified length (10 - 100) for Random String Length Plaintexts"""
    string_length = random.randint(10, 100)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=string_length))
def generate_random_decimal_pt(length):
    """Random Generator For The Decimal Key == length for Indentical Decimals Length Plaintexts"""
    return int(''.join(str(random.randint(0, 9)) for _ in range(length)))
def generate_random_length_dec():
    """Random Generator For The String Key length (10 -100) for # Random Decimals Length Plaintexts"""
    length = random.randint(10, 100)
    return int(''.join(str(random.randint(0, 9)) for _ in range(length)))
# This is for the Integers in order to fill with zeros
def xor_binary_strings(str1, str2):
    # Check if either string is None
    if str1 is None or str2 is None:
        raise ValueError("Input strings cannot be None.")
    # Determine the maximum length of the input strings
    max_len = max(len(str1), len(str2))
    # Pad both strings with zeros to the maximum length
    str1 = str1.rjust(max_len, '0')
    str2 = str2.rjust(max_len, '0')
    # XOR the binary strings
    xor_result = ''.join(str(int(x) ^ int(y)) for x, y in zip(str1, str2))
    return  xor_result
# This is for the Strings in order to fill with ASCII <<zeros>>
def xor_2strings(s1, s2):
    """Perform XOR operation on two strings, padding the shorter string with zeros."""
    len_s1, len_s2 = len(s1), len(s2)

    # Find the maximum length
    max_len = max(len_s1, len_s2)

    # Pad the shorter string with zeros
    s1 = s1.ljust(max_len, '\x00')
    s2 = s2.ljust(max_len, '\x00')

    # Perform XOR operation on the padded strings
    result = ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2))

    return result

# def binary_to_string(binary):
#     """Convert binary string to ASCII string."""
#     return ''.join(chr(int(binary[i:i + 8], 2)) for i in range(0, len(binary), 8))
def string_to_binary(string):
    """Convert ASCII string to binary string."""
    return ''.join(format(ord(c), '08b') for c in string)
# def decimal_to_binary(decimal_num):
#     """Convert ASCII Decimal to binary strin fill with zero(not nessesary, anyway)"""
#     binary_str = bin(decimal_num)[2:]
#     # Calculate the number of zeros needed for padding
#     padding_zeros = (8 - len(binary_str) % 8) % 8
#     # Add leading zeros for padding
#     binary_str = '0' * padding_zeros + binary_str
#     return binary_str

def process_ascii_array(input_array):
        inarray = input_array
        result_array = []
        longest = max(inarray, key=len)  # Initialize longest outside the loop

        while longest != "0":
            # Start from the zero position in the array and check every position while the array is filled with zeros
            for i in range(len(inarray)):
                for j in range(len(inarray)): # for every pair
                    if inarray[i] in longest:  # Compare the values if it is in the longest
                        inarray[i] = "0"  # Fill that position with zero
                    else:  # If the inarray[i] is not in the longest
                        continue
            result_array.append(longest)
            longest = max(inarray, key=len)  # Find the new longest after updating the array

        return result_array
