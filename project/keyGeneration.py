from ecdsa import SigningKey, SECP256k1

class keyGeneration:

    def generate_private_key(self):
        private_key = SigningKey.generate(SECP256k1)
        return private_key
    
    def generate_public_key(self, private_key):
        public_key = private_key.get_verifying_key()
        return public_key
    



