
import random
import string


def encrypt_text(txt):
    encrypted_txt = ''

    if len(txt) == 3:
        prefix = ''.join(random.choices(string.ascii_letters + string.digits, k=3))
        suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=3))
        encrypted_txt = prefix + txt + suffix
        return encrypted_txt

    elif len(txt) == 2:
        encrypted_txt = txt[1] + txt[0]
        return encrypted_txt

    else:
     print("Not enough text characters (minimum 2 required)")


def decrypt_text(encrypted_txt):

    if len(encrypted_txt) == 9:

         return encrypted_txt[3:6]
    elif len(encrypted_txt) == 2:
        return encrypted_txt[1] + encrypted_txt[0]
    else:
      print("Not enough text characters (minimum 2 required)")


# Take input from user
user_input = input("Enter the text (at least 2 characters): ")

enc_text=encrypt_text(user_input)
print("The encrypted text is:",enc_text)


dec_text=decrypt_text(enc_text)

print("The decrypted text is:",dec_text)





