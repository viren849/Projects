import hashlib
import tkinter.messagebox
from Crypto.Cipher import AES
import simple_xor as simp

def enc_image(input_data, key, iv, filepath):
    cfb_cipher = AES.new(key, AES.MODE_CFB, iv)
    enc_data = cfb_cipher.encrypt(input_data)

    enc_file = open(filepath + "/encrypted2.jpg", "wb")
    enc_file.write(enc_data)
    enc_file.close()


def dec_image(c,input_data, key, iv, filepath,filename,enc_pass):
    cfb_decipher = AES.new(key, AES.MODE_CFB, iv)
    plain_data = cfb_decipher.decrypt(input_data)
    if c == 1:
       #key value should be reverse
       key=enc_pass
       simp.decrypt(c,filename,key,filepath,plain_data)
    else:
        output_file = open(filepath + "/decrypted2.jpg", "wb")
        output_file.write(plain_data)
        output_file.close()


def aes_encrypt(c,enc_pass,file_path_e,filename,input_data):
        #GENERATE KEY & INITIALIZATION VECTOR
        hash=hashlib.sha256(enc_pass.encode())
        p = hash.digest()
        key = p
        iv = p.ljust(16)[:16]
        print("Encoding key is: ",key)

        if c == 0:
            input_file = open(filename, 'rb')
            input_data = input_file.read()
            input_file.close()

        enc_image(input_data,key,iv,file_path_e)
        tkinter.messagebox.showinfo("Encryption Alert","Encryption ended successfully. File stored as: encrypted2.jpg")

def aes_decrypt(c,enc_pass,file_path_e,filename):
        hash=hashlib.sha256(enc_pass.encode())
        p = hash.digest()
        key = p
        iv = p.ljust(16)[:16]
        input_file = open(filename,'rb')
        input_data = input_file.read()
        input_file.close()
        dec_image(c,input_data,key,iv,file_path_e,filename,enc_pass)
        if c == 0:
           tkinter.messagebox.showinfo("Decryption Alert","Decryption ended successfully File Stored as: decrypted2.jpg")
