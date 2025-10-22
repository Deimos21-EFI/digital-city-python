#################################
# Les opérateurs
#################################
"""
# Arithmétiques
- + aaddition
- - soustraction
- / division
- // division entière
- % module
- ** exposant
"""
a = 64 + 64
b = 2 - 1
c = 3 / 2
d = 27 // 2
e = 27 % 2
f = 2 ** 4
g = 0 ^ 1  # (bitwise XOR)

print(a, b, c, d, e, f, g)


def compare(v1, v2):
    """

    :param v1:
    :param v2:
    :return:
    """
    print(f"Comparing {v1} and {v2}")
    if (v1 == v2): print(f"{v1} is equal to {v2}")
    if (v1 != v2): print(f"{v1} is not equal to {v2}")
    if (v1 > v2): print(f"{v1} is greater than {v2}")
    if (v1 < v2): print(f"{v1} is lower than {v2}")
    if (v1 <= v2): print(f"{v1} is lower or equal to {v2}")
    if (v1 >= v2): print(f"{v1} is greater or equal to {v2}")
x = 10
y = 20
# égalité
compare(x, y)
compare(10, 10)

print(True + False + True)

value_int = "10"
# check if value_int is a number
if (isinstance(value_int, int )):
    print(f"{value_int} is a number")
    value_int = int(value_int)
else:
    print(f"{value_int} is NOT a number and cannot be converted to int")

