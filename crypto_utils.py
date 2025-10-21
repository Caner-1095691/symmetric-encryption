import os
import base64
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

class SymmetricEncryption:
    """AES 256 GCM implementatie volgens Kerckhoffs principe"""
    
    def __init__(self, key: bytes = None):
        """Hier initialiseer ik met een 256 bit key"""
        
        if key is None:
            key = AESGCM.generate_key(bit_length=256)
        elif len(key) != 32:
            raise ValueError("Key moet 32bytes zijn")
        
        self.key = key 
        self.aesgcm = AESGCM(key)
        
    def encrypt(self, plaintext: str) -> dict:
        #convert string naar bytes
        plaintext_bytes = plaintext.encode('utf-8')
        
        nonce = os.urandom(12)
        ciphertext = self.aesgcm.encrypt(nonce, plaintext_bytes, None)
        
        return {
            'nonce': base64.b64encode(nonce).decode('utf-8'),
            'ciphertext': base64.b64encode(ciphertext).decode('utf-8')
        }
        
    def decrypt(self, nonce: str, ciphertext: str) -> str:
        
        nonce_bytes = base64.b64decode(nonce)
        ciphertext_bytes = base64.b64decode(ciphertext)
        
        plaintext_bytes = self.aesgcm.decrypt(nonce_bytes, ciphertext_bytes, None)
        
        return plaintext_bytes.decode('utf-8')
    
    def get_key_base64(self) -> str:
        return base64.b64encode(self.key).decode('utf-8')
    
    @classmethod
    def from_password(cls, password: str, salt: bytes = None):
        
        if salt is None:
            salt = os.urandom(16)
            
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=600000,
        )
        
        key = kdf.derive(password.encode())
        
        return cls(key), salt
        