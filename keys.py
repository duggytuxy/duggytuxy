import time
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def generate_rsa_keys():
    keys = []
    
    for _ in range(5):  
        key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=4096
        )
        private_key = key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )
        public_key = key.public_key().public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        keys.append((private_key, public_key))
    return keys

def reveal_id():
    encoded_id = "VEhNe1kwVV9DUjRDS0VEX1RIM19TQ1IxUFR9"
    id_str = base64.b64decode(encoded_id).decode()
    print(id_str)

def main():
    minute_counter = 0
    while True:
        print(f"--- Minute {minute_counter} ---")
        keys = generate_rsa_keys()
        for i, (priv, pub) in enumerate(keys, 1):
            print(f"Key Pair {i} generated.")
        
        if len(keys) == 6:
            reveal_id()
        minute_counter += 1
        time.sleep(60)

main()
