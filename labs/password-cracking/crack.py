from itertools import product
from string import ascii_letters, digits, punctuation

# for i in digits:
#     for j in digits:
#         for k in digits:
#             for l in digits:
#                 print(i, j, k, l)


# for i in ascii_letters:
#     for j in ascii_letters:
#         for k in ascii_letters:
#             for l in ascii_letters:
#                 print(i, j, k, l)


for combination in product(digits + ascii_letters + punctuation, repeat=4):
    print("".join(combination))