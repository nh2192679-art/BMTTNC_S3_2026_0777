from cipher.caesar import ALPHABET

class CaesarCipher:

    def __init__(self):
        self.alphabet = ALPHABET

    def encrypt_text(self, text: str, key: int) -> str:

        alphabet_len = len(self.alphabet)
        text = text.upper()
        encrypted = []

        for letter in text:
            if letter not in self.alphabet:
                encrypted.append(letter)
                continue

            index = self.alphabet.index(letter)
            output_index = (index + key) % alphabet_len
            encrypted.append(self.alphabet[output_index])

        return "".join(encrypted)

    def decrypt_text(self, text: str, key: int) -> str:

        alphabet_len = len(self.alphabet)
        text = text.upper()
        decrypted = []

        for letter in text:
            if letter not in self.alphabet:
                decrypted.append(letter)
                continue

            index = self.alphabet.index(letter)
            output_index = (index - key) % alphabet_len
            decrypted.append(self.alphabet[output_index])

        return "".join(decrypted)
