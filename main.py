
aplphabets = 'abcdefghijklmnopqrstuvwxyz'
num_letters = len(aplphabets)

print("******************************")
print('=======CAESAR CIPHER==========')
print('******************************')

print('For Encryption Enter "E" And For Decryption Enter "D"')


def encrypt_decrypt(input_text, mode, input_key):
    result = ''
    if mode == 'd':
       input_key = -input_key
    for letter in input_text:
        letter = letter.lower()
        if not letter == '':
               index = aplphabets.find(letter)
               if index == -1:
                   result += letter
               else:
                    new_index = index + input_key
                    if new_index >= num_letters:
                       new_index -= num_letters
                    elif new_index < 0:
                         new_index += num_letters
                    result += aplphabets[new_index]
    return result


user_input = input('SELECT MODE E/D:').lower()

if user_input == 'e':
   print('ENCRYPTION MODE SELECTED')
   print()
   key = int(input('Enter the key (1 through 26):'))
   text = input('Enter the text to encrypt: ')
   ciphertext = encrypt_decrypt(text, user_input, key)
   print(f'CIPHERTEXT: {ciphertext}')
elif user_input == 'd':
    print('DECRYPTION MODE SELECTED')
    print()
    key = int(input('Enter the key (1 through 26):'))
    text = input('Enter the text to decrypt: ')
    plaintext = encrypt_decrypt(text, user_input, key)
    print(f'PLAINTEXT: {plaintext}')
