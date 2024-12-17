import unittest
from ecdsa import SigningKey, SECP256k1

from project.keyGeneration import keyGeneration



class TestKeyGeneration(unittest.TestCase):
    def test_key_generation(self):
        # Arrange
        key_gen = keyGeneration()
        
        # Act
        private_key = key_gen.generate_private_key()
        
        # Assert
        self.assertIsInstance(private_key, SigningKey, 
                              "The generated key should be an instance of SigningKey")
        
        self.assertEqual(private_key.curve, SECP256k1, 
                         "The private key should use SECP256k1 curve")
        
        self.assertIsNotNone(private_key, "Private key should not be None")



if __name__ == '__main__':
    unittest.main()