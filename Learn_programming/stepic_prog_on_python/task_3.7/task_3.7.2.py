from typing import List


def get_input() -> List[str]:
    list_input = []
    try:
        for _ in range(4):
            str_input = str(input()).strip()
            if not str_input:
                raise ValueError
            list_input.append(str_input)

        # list_input = ['abcd',
        #               '*d%#',
        #               'abacabadaba',
        #               '#*%*d*%']

        # list_input = ['dcba',
        #               'badc',
        #               'dcba',
        #               'badc']
        return list_input
    except ValueError:
        print('wrong input')


def parse_input(list_input: List[str]) -> tuple:
    alph = list(list_input[0])
    cypher = list(list_input[1])
    cypher_key = dict(zip(alph, cypher))
    encrypt = list_input[2]
    decrypt = list_input[3]

    return cypher_key, encrypt, decrypt


def replace_text(text: str, cypher_key: dict):
    return ''.join([cypher_key[ch] for ch in text])


def encrypt_text(text: str, cypher_key: dict) -> str:
    return replace_text(text, cypher_key)


def decrypt_text(text: str, cypher_key: dict) -> str:
    temp_cypher_key = {v: k for k, v in cypher_key.items()}
    return replace_text(text, temp_cypher_key)


def main():
    list_input = get_input()
    cypher_key, encrypt, decrypt = parse_input(list_input)
    print(encrypt_text(encrypt, cypher_key))
    print(decrypt_text(decrypt, cypher_key))


main()
