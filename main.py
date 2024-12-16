from ecdsa import SigningKey, SECP256k1



private_key = SigningKey.generate(SECP256k1)
public_key = private_key.get_verifying_key()

print("private key: ", private_key.to_pem())
print("public key: ", public_key.to_pem())
