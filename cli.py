import sys 
import base64
from crypto_utils import SymmetricEncryption

def main():
    print("--- Symmetrische Encryptie Applicatie ---")
    print("Algoritme AES-256 GCM")
    print("Volgt Kerckhoffs principe: algoritme is publiek, sleutel is geheim\n")
    
    while True:
        print("\n1. Genereer nieuwe sleutel")
        print("2. Versleutel tekst")
        print("3. Ontsleutel tekst")
        print("4. Exit")
        
        choice = input("\nKies optie: ")
        
        if choice == "1":
            generate_key()
        elif choice == "2":
            encrypt_text()
        elif choice == "3":
            decrypt_text()
        elif choice == "4":
            break
        else:
            print("ongeldige keuze!")
            
            
def generate_key():
    """Genereer een nieuwe random key."""
    crypto = SymmetricEncryption()
    key_b64 = crypto.get_key_base64()
    
    print("\n=== Nieuwe sleutel gegenereerd ===")
    print(f"Key (base64): {key_b64}")
    print("\nBELANGRIJK: Bewaar deze sleutel veilig!")
    print("Iedereen met deze sleutel kan je berichten ontsleutelen!")
    
    # Optioneel: save to file
    save = input("\nOpslaan naar bestand? (j/n): ")
    if save.lower() == 'j':
        filename = input("Bestandsnaam: ")
        with open(filename, 'w') as f:
            f.write(key_b64)
        print(f"✓ Sleutel opgeslagen in {filename}")

def encrypt_text():
    """Versleutel tekst."""
    print("\n=== Tekst Versleutelen ===")
    
    # Krijg key
    key_source = input("Key invoeren (1) of laden van bestand (2)? ")
    
    if key_source == "1":
        key_b64 = input("Voer key in (base64): ")
        key = base64.b64decode(key_b64)
    elif key_source == "2":
        filename = input("Key bestand: ")
        with open(filename, 'r') as f:
            key_b64 = f.read().strip()
        key = base64.b64decode(key_b64)
    else:
        print("Ongeldige keuze!")
        return
    
    crypto = SymmetricEncryption(key)
    
    # Krijg plaintext
    plaintext = input("\nVoer tekst om te versleutelen: ")
    
    # Encrypt
    result = crypto.encrypt(plaintext)
    
    print("\n=== Versleuteld ===")
    print(f"Nonce: {result['nonce']}")
    print(f"Ciphertext: {result['ciphertext']}")
    
    # Optioneel save
    save = input("\nOpslaan naar bestand? (j/n): ")
    if save.lower() == 'j':
        filename = input("Bestandsnaam: ")
        with open(filename, 'w') as f:
            f.write(f"{result['nonce']}\n{result['ciphertext']}")
        print(f"✓ Opgeslagen in {filename}")

def decrypt_text():
    """Ontsleutel tekst."""
    print("\n=== Tekst Ontsleutelen ===")
    
    # Krijg key
    key_source = input("Key invoeren (1) of laden van bestand (2)? ")
    
    if key_source == "1":
        key_b64 = input("Voer key in (base64): ")
        key = base64.b64decode(key_b64)
    elif key_source == "2":
        filename = input("Key bestand: ")
        with open(filename, 'r') as f:
            key_b64 = f.read().strip()
        key = base64.b64decode(key_b64)
    else:
        print("Ongeldige keuze!")
        return
    
    crypto = SymmetricEncryption(key)
    
    # Krijg encrypted data
    data_source = input("Encrypted data invoeren (1) of laden van bestand (2)? ")
    
    if data_source == "1":
        nonce = input("Nonce: ")
        ciphertext = input("Ciphertext: ")
    elif data_source == "2":
        filename = input("Data bestand: ")
        with open(filename, 'r') as f:
            lines = f.readlines()
            nonce = lines[0].strip()
            ciphertext = lines[1].strip()
    else:
        print("Ongeldige keuze!")
        return
    
    # Decrypt
    try:
        plaintext = crypto.decrypt(nonce, ciphertext)
        print("\n=== Ontsleuteld ===")
        print(f"Plaintext: {plaintext}")
    except Exception as e:
        print(f"\nFout bij ontsleutelen: {e}")
        print("Mogelijke oorzaken:")
        print("- Verkeerde key")
        print("- Corrupt ciphertext")
        print("- Data is aangepast (authenticatie gefaald)")

if __name__ == "__main__":
    main()
        