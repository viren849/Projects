import tkinter.messagebox
import aes

def encrypt(c,file_name,key,filepath):
    fi=open(file_name,'rb')
    image=fi.read()
    fi.close()
    print(" key is: ", key)
    image=bytearray(image)
    for index,values in enumerate(image):
        image[index]=values^int(key)

    if c == 1 :
        aes.aes_encrypt(c,key, filepath, file_name,image)
    else:
        enc_file = open(filepath + "/encrypted1.jpg", "wb")
        enc_file.write(image)
        enc_file.close()
        tkinter.messagebox.showinfo("Encryption Alert",
                                    "Encryption ended successfully. File stored as: encrypted1.jpg")

def decrypt(c,file_name,key,filepath,image):
    if c == 0:
        fi = open(file_name, 'rb')
        image = fi.read()
        fi.close()
    print("Encoding key is: ", key)
    image=bytearray(image)
    for index,values in enumerate(image):
        image[index]=values^int(key)
    enc_file = open(filepath + "/decrypted1.jpg", "wb")
    enc_file.write(image)
    enc_file.close()
    tkinter.messagebox.showinfo("Decryption Alert", "Encryption ended successfully. File stored as: decrypted1.jpg")