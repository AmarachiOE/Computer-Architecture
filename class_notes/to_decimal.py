str = "1010"

def to_decimal(num_string, base):
    digit_list = list(num_string)
    digit_list.reverse()
    value = 0

    for i in range (len(digit_list)):
        print(f"+ {int(digit_list[i])} * {base ** i}")
        value+= int(digit_list[i] * (base ** i))
    return value

to_decimal(str, 2)

# Truthiness
for A in [True, False]:
    for B in [True, False]:
        print(f"{A} - {B} -- {A and B}")