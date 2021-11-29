import cryptography
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

##### generate new keys
private_key = rsa.generate_private_key(public_exponent=65537,key_size=2048,backend=default_backend())
public_key = private_key.public_key()


############# save PrivateKey ######################################
pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

with open('private_key.pem', 'wb') as f:
    f.write(pem)
####################################################################




############# save PublicKey ######################################

pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

with open('public_key.pem', 'wb') as f:
    f.write(pem)
####################################################################




#####################read a saved privateKey#########################################
with open("private_key.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()
    )

#####################read a saved PublicKey#########################################
with open("public_key.pem", "rb") as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read(),
        backend=default_backend()
    )





##############################Encrypt using public key###############################################################
message=b'encrypt me!'

encrypted = public_key.encrypt(message, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))


##############################Decrypt using private key###############################################################
original_message = private_key.decrypt(encrypted, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))

print("before encryption : "+str(message))
print("encrypted message : "+str(encrypted))
print("decypted message  : "+str(original_message))
