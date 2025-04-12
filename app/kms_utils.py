import boto3
import base64
import os

kms_client = boto3.client('kms')
key_id = os.environ['KMS_KEY_ID']

def encrypt_password(plain_text):
    response = kms_client.encrypt(KeyId=key_id, Plaintext=plain_text.encode())
    return base64.b64encode(response['CiphertextBlob']).decode()

def decrypt_password(cipher_text):
    decoded = base64.b64decode(cipher_text)
    response = kms_client.decrypt(CiphertextBlob=decoded)
    return response['Plaintext'].decode()