import unittest
from playfair import encrypt_playfair, decrypt_playfair, prepare_bigrams

class TestPlayfairCipher(unittest.TestCase):

    def test_bigrams_insert_x_on_repeat(self):
        # Должен вставить X между LL
        bigrams = prepare_bigrams("BALLOON")
        self.assertIn(("L", "X"), bigrams)

    def test_padding_for_odd_length(self):
        bigrams = prepare_bigrams("CAT")
        self.assertEqual(len(bigrams) % 2, 0)

    def test_encrypt_decrypt_cycle(self):
        text = "HIDETHEGOLD"
        key = "PLAYFAIREXAMPLE"
        encrypted = encrypt_playfair(text, key)
        decrypted = decrypt_playfair(encrypted, key)
        self.assertEqual(decrypted[:len(text.replace('J', 'I'))], text.replace('J', 'I'))

    def test_same_row_rule(self):
        # Символы в одной строке
        encrypted = encrypt_playfair("AR", "MONARCHY")
        decrypted = decrypt_playfair(encrypted, "MONARCHY")
        self.assertEqual(decrypted, "AR")

    def test_same_column_rule(self):
        encrypted = encrypt_playfair("MV", "MONARCHY")
        decrypted = decrypt_playfair(encrypted, "MONARCHY")
        self.assertEqual(decrypted, "MV")

    def test_rectangle_rule(self):
        encrypted = encrypt_playfair("HE", "MONARCHY")
        decrypted = decrypt_playfair(encrypted, "MONARCHY")
        self.assertEqual(decrypted, "HE")

    def test_q_is_excluded(self):
        encrypted = encrypt_playfair("FAQ", "MONARCHY")
        self.assertNotIn("Q", encrypted)

    def test_j_is_converted_to_i(self):
        encrypted_i = encrypt_playfair("IN", "MONARCHY")
        encrypted_j = encrypt_playfair("JN", "MONARCHY")
        self.assertEqual(encrypted_i, encrypted_j)

    def test_key_duplicates_ignored(self):
        e1 = encrypt_playfair("HELLO", "BALLOON")
        e2 = encrypt_playfair("HELLO", "BALON")
        self.assertEqual(e1, e2)

    def test_matrix_is_deterministic(self):
        e1 = encrypt_playfair("SECRET", "KEYWORD")
        e2 = encrypt_playfair("SECRET", "KEYWORD")
        self.assertEqual(e1, e2)

    def test_known_pair(self):
        # Проверка, что "HIDE" шифруется корректно
        self.assertEqual(encrypt_playfair("HIDE", "PLAYFAIREXAMPLE"), "BMOD")

    def test_known_decryption(self):
        self.assertEqual(decrypt_playfair("BMOD", "PLAYFAIREXAMPLE"), "HIDE")

if __name__ == '__main__':
    unittest.main()
