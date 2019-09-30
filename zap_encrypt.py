from cryptography.fernet import Fernet
import getpass

input_pass = (getpass.getpass()).encode()
encpass = Fernet('RvivOR8btMLOCM0T8G4w8c3PuLniLmmXz1dsVOoXC8M=').encrypt(input_pass)
print(encpass.decode())
