logo = """
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88
            88             88
           ""             88
                          88
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8
8b         88 88       d8 88       88 8PP""""""" 88
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88
              88
              88
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
shift = int(input("Type the shift number:\n"))
if shift>=26:
        shift=shift%26
text = input("Type your input_text:\n").lower()
def ceaser(input_text,shifted,text_direction):
    output_text=''
    if direction=='decode':  # encode is not specified as for encode shift is by default + and for decode, we specified it as negative
        shifted=-shift
    for letter in text:
        if letter not in alphabet:
            output_text+=letter
        elif letter in alphabet:
            pos=alphabet.index(letter)
            new_pos=pos+shifted
            if new_pos>=26:
                new_pos-=26
            shift_letter=alphabet[new_pos]
            output_text+=shift_letter
    print(f"Here is the encoded result:{output_text}")
    proceed=True
ceaser(input_text=text,shifted=shift,text_direction=direction)
go=True
while go:
    choice=input("Do you want to encode/decode more? y/n")
    if choice=='n':
        go=False
        print("Good Bye..")
    else:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        shift = int(input("Type the shift number:\n"))
        if shift>=26:
            shift=shift%26
        text = input("Type your input_text:\n").lower()
        ceaser(input_text=text,shifted=shift,text_direction=direction)
