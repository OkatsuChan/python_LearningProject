
credit_number = "1234-5678-9012-3456"


# print(credit_number[4])
# print(credit_number[:4])
# print(credit_number[5:])
# print(credit_number[-2])
# print(credit_number[::3])

credit_number = credit_number[::-1]
print(f"{credit_number}")
last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")