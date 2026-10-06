from itertools import product
from string import ascii_letters, digits

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


for combination in product(digits, repeat=4):
    print("".join(combination))

for combination in product(ascii_letters, repeat=4):
    print("".join(combination))