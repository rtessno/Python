import unittest
from unittest import TestCase
from encryption import *

class TestEncryption(TestCase):
### Test encrypt
    def test_encrypt_for_empty_string(self):
        self.assertEquals(Encryption.encrypt(''),'')

    def test_encypt_for_encryption(self):
        self.assertEquals(Encryption.encrypt('a'),'d')

    def test_encrypt_for_numbers(self):
        self.assertRaises(ValueError,Encryption.encrypt, '1')
### Test decrypt
    def test_decrypt_for_decryption(self):
        self.assertEquals(Encryption.decrypt('d'),'a')

    def test_decrypt_for_empty_string(self):
        self.assertRaises(ValueError,Encryption.decrypt,'')

    def test_decrypt_for_numbers(self):
        self.assertRaises(ValueError,Encryption.decrypt, '1')
###Test Key
    def test_Encryption_key(self):
        self.assertEquals(len(key), 26)
        self.assertEqual(key.islower(),True)
        self.assertEqual(key.isalpha(),True)
        self.assertEquals(key,'abcdefghijklmnopqrstuvwxyz')



if __name__ == '__main__':
    unittest.main()