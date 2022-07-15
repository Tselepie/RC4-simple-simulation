
from xml.etree.ElementTree import tostring
from pyparsing import alphanums


alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
            'W', 'X', 'Y', 'Z', '.', '!', '?', '(', ')', '-']

converted = ['00000', '00001', '00010', '00011', '00100', '00101',
             '00110', '00111', '01000', '01001', '01010', '01011',
             '01100', '01101', '01110', '01111', '10000', '10001',
             '10010', '10011', '10100', '10101', '10110', '10111',
             '11000', '11001', '11010', '11011', '11100', '11101',
             '11110', '11111']


def xor(b1, b2):
    result = []

    for i in range(len(b1)):
        result.append(int(b1[i]) ^ int(b2[i]))

    return result


def list_to_string(list):
    to_string = ""

    return to_string.join(list)


def convert(letter):
    i = 0

    while(alphabet[i] != letter):
        i += 1

    return converted[i]


def re_convert(binary):
    i = 0
    to_str = ""

    for b in binary:
        to_str += str(b)

    while(converted[i] != to_str):
        i += 1

    return alphabet[i]


def pos(letter):
    i = 0

    while(alphabet[i] != letter):
        i += 1

    return i


def prga(s, n_of_iterations, message_length):
    i = 0
    j = 0
    counter = 0
    k = []

    while(counter < message_length):
        i = (i + 1) % n_of_iterations
        j = (j + s[i]) % n_of_iterations
        temp = s[i]
        s[i] = s[j]
        s[j] = temp
        t = (s[i] + s[j]) % n_of_iterations
        k.append(s[t])
        counter += 1

    return k


def encrypt(message, key):
    binary = []
    c = []

    for i in range(len(message)):
        binary.append(convert(message[i]))
        c.append(xor(binary[i], converted[key[i % len(key)]]))
        c[i] = re_convert(c[i])

    return c


def decrypt(cmessage, key):
    binary = []
    message = []

    for i in range(len(cmessage)):
        binary.append(convert(cmessage[i]))
        message.append(xor(binary[i], converted[key[i % len(key)]]))
        message[i] = re_convert(message[i])

    return message


message = open("Plaintext.txt", "r")

j = 0
s = []
t = []
key = ['H', 'O', 'U', 'S', 'E']
data = message.read()
data = data.replace(" ", "")

for i in range(32):
    s.append(pos(alphabet[i]))
    t.append(pos(key[i % len(key)]))

for i in range(32):
    j = (j + s[i] + t[i]) % 32
    temp = s[i]
    s[i] = s[j]
    s[j] = temp

new_key = prga(s, len(key), len(data))
c = encrypt(data, new_key)
print("c = " + list_to_string(c))
m = decrypt(c, new_key)
print("m = " + list_to_string(m))

message.close()
