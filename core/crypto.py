# -*- coding: utf-8 -*-
import os
from binascii import b2a_hex, a2b_hex
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from Crypto.Hash import SHA256


SECRET_CODE = 'JFSLJIHJOH5F4FS5'
CODING = 'utf-8'
PAD_SIZE = 16


def export_key(path='.', pub=True, passphrase=SECRET_CODE):
    '''
    Generate public key and private key
    '''
    key = RSA.generate(2048)
    if pub:
        public_key = key.publickey().export_key(passphrase=passphrase, pkcs=8, protection="scryptAndAES128-CBC")
        with open(os.path.join(path, 'rsa_key.pub'), 'wb') as wf:
            wf.write(public_key)
    else:
        private_key = key.export_key(passphrase=passphrase, pkcs=8, protection="scryptAndAES128-CBC")
        with open(os.path.join(path, 'rsa_key'), 'wb') as wf:
            wf.write(private_key)
    return public_key if pub else private_key


def encrypt(data, key_path, passphrase=SECRET_CODE):
    '''
    Encrypt data with RSA
    '''
    recipient_key = RSA.import_key(open(key_path).read(), passphrase=passphrase)
    session_key = get_random_bytes(16)
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    enc_session_key = cipher_rsa.encrypt(session_key)
    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(data)
    return b2a_hex(enc_session_key + cipher_aes.nonce + tag + ciphertext)


def decrypt(data, key_path, passphrase=SECRET_CODE):
    '''
    Decrypt data with RSA
    '''
    data = a2b_hex(data)
    private_key = RSA.import_key(open(key_path).read(), passphrase=passphrase)
    k_size = private_key.size_in_bytes()
    enc_session_key, nonce, tag, ciphertext = data[0:k_size], data[k_size:k_size + 16], data[k_size + 16:k_size + 32], data[k_size + 32:]
    cipher_rsa = PKCS1_OAEP.new(private_key)
    session_key = cipher_rsa.decrypt(enc_session_key)
    cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
    rs = cipher_aes.decrypt_and_verify(ciphertext, tag)
    return rs.decode(CODING)


def aes_encode(plaintext, key):
    '''
    Encrypt data with AES
    '''
    p_key = pad(key.encode(CODING), PAD_SIZE)
    cipher = AES.new(p_key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext.encode(CODING), PAD_SIZE))
    return b2a_hex(ciphertext).decode(CODING)


def aes_decode(ciphertext, key):
    '''
    Decrypt data with AES
    '''
    p_key = pad(key.encode(CODING), PAD_SIZE)
    cipher = AES.new(p_key, AES.MODE_ECB)
    return unpad(cipher.decrypt(a2b_hex(ciphertext)), PAD_SIZE).decode(CODING)


def sha256(data):
    return SHA256.new(data.encode('utf-8')).hexdigest().upper()
