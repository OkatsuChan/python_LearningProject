

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
checker_continue ="yes"

def caesar(direction,text,shift):

    def encrypt(original_text,shift_amount):
        cypher_text =""
        for letter in original_text:
            if letter not in alphabet:
                cypher_text += letter
            else:
                shift_pos = alphabet.index(letter) + shift_amount
                cypher_text += alphabet[shift_pos % len(alphabet)]

        print(f"Here is the encoded result: {cypher_text}")

    def decrypt(original_text,shift_amount):
        cypher_text = ""
        for letter in original_text:
            if letter not in alphabet:
                cypher_text += letter
            else:
                shift_pos = alphabet.index(letter) - shift_amount
                cypher_text += alphabet[shift_pos % len(alphabet)]
        print(f"Here is the encoded result: {cypher_text}")

    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)
    else:
        print("Invalid Input pls try Again")

while checker_continue.lower() == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction,text,shift)
    checker_continue = input("Type 'yes' if you want to go again. Otherwise, type 'no': ")
