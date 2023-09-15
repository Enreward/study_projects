import os
import sys
import simplecrypt

ROOT_PATH = os.path.dirname(sys.argv[0])
DATA_PATH = os.path.join(ROOT_PATH, 'data_for_task_2.2.2')


if __name__ == '__main__':
    # пароли
    with open(os.path.join(DATA_PATH, 'passwords.txt'), 'r') as inp:
        passwords = map(str.strip, inp.readlines())
    # зашифрованный файл
    with open(os.path.join(DATA_PATH, 'encrypted.bin'), 'rb') as inp:
        encrypted_text = inp.read()

    decrypted_text = ''
    for password in passwords:
        if password:
            # decrypted_text = simplecrypt.decrypt(password, encrypted_text)
            try:
                decrypted_text = simplecrypt.decrypt(password, encrypted_text)
                print(f'Correct password: {password}')
                break
            except simplecrypt.DecryptionException:
                print(f'Wrong password: {password}')
                continue

    print(decrypted_text)
