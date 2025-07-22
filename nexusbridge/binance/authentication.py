import base64
import hmac
import hashlib
from base64 import b64encode
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15
from cryptography.hazmat.primitives.serialization import load_pem_private_key


def hmac_hashing(secret, payload):
    m = hmac.new(secret.encode("utf-8"), payload.encode("utf-8"), hashlib.sha256)
    return m.hexdigest()


def rsa_signature(private_key, payload, private_key_pass=None):
    private_key = RSA.import_key(private_key, passphrase=private_key_pass)
    h = SHA256.new(payload.encode("utf-8"))
    signature = pkcs1_15.new(private_key).sign(h)
    return b64encode(signature).decode("utf-8")


def ed_25519(private_key: str, payload, private_key_pass: str = None):
    key = load_pem_private_key(
        private_key.encode("utf-8"), password=private_key_pass.encode("utf-8")
    )
    return base64.b64encode(key.sign(payload.encode("ASCII"))).decode("utf-8")
