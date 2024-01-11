
import ceaser_print

print(ceaser_print.logo)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def ceaser_chiper(text, shift, direction):           

    if direction == 'encode':

        encoded_txt = ''
        
        for char in text:
            if char in alphabet:
                position = alphabet.index(char)
                encoded_position = position + shift
                encoded_txt += alphabet[encoded_position]
            else:
                encoded_txt += char
        print(f'The encoded text is {encoded_txt}')

    elif direction == 'decode':

        decode_txt = ''

        for char in text:
            if char in alphabet:
                # finding position in alphabet
                position = alphabet.index(char)
                # shiftin from that position backwards and saving as decode position
                decode_position = position - shift
                # adding the decoded letter at alphabet position to decode_txt
                decode_txt += alphabet[decode_position]
            else:
                decode_txt += char


        print(f'The decoded text is {decode_txt}')


run = True
while run:
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26
    
    ceaser_chiper(text, shift, direction)


    run_again = input('Do you want to run again? Y or N? ')
    if run_again == 'N':
        run = False
        print('Program ended')
           

        



    

