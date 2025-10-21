import unittest
from crypto_utils import SymmetricEncryption

class TestSymmetricEncryption(unittest.TestCase):
    
    def test_encrypt_decrypt(self):
        """Test basis encrypt/decrypt cycle."""
        crypto = SymmetricEncryption()
        plaintext = "Test bericht 123!"
        
        encrypted = crypto.encrypt(plaintext)
        decrypted = crypto.decrypt(encrypted['nonce'], encrypted['ciphertext'])
        
        self.assertEqual(plaintext, decrypted)
    
    def test_different_nonce_different_ciphertext(self):
        """Test dat dezelfde plaintext verschillende ciphertext geeft."""
        crypto = SymmetricEncryption()
        plaintext = "Same message"
        
        enc1 = crypto.encrypt(plaintext)
        enc2 = crypto.encrypt(plaintext)
        
        # Nonces moeten verschillen
        self.assertNotEqual(enc1['nonce'], enc2['nonce'])
        # Ciphertexts moeten verschillen
        self.assertNotEqual(enc1['ciphertext'], enc2['ciphertext'])
    
    def test_wrong_key_fails(self):
        """Test dat verkeerde key niet kan decrypten."""
        crypto1 = SymmetricEncryption()
        crypto2 = SymmetricEncryption()  # Andere key
        
        encrypted = crypto1.encrypt("Secret")
        
        with self.assertRaises(Exception):
            crypto2.decrypt(encrypted['nonce'], encrypted['ciphertext'])
    
    def test_password_derivation(self):
        """Test key derivation van password."""
        password = "mijn_wachtwoord"
        crypto1, salt = SymmetricEncryption.from_password(password)
        crypto2, _ = SymmetricEncryption.from_password(password, salt)
        
        # Beide moeten dezelfde key hebben
        self.assertEqual(crypto1.key, crypto2.key)

if __name__ == '__main__':
    unittest.main()