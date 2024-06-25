import hashlib
import base64
import os
from cryptography.fernet import Fernet
from getpass import getpass
import random 
import string

#Function to generate a strong password
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

#Function to write a key
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

#Function to load a key
def load_key():
    with open("key.key", "rb") as key_file:
        key = key_file.read()
    return key

#Function to hash a password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

#Function to check if the master password file exists
def master_password_exists():
    return os.path.exists("master_pwd.txt")

#Function to set the master password
def set_master_password():
    master_pwd = getpass("Set your master password: ")
    master_pwd_confirm = getpass("Confirm your master password: ")
    if master_pwd != master_pwd_confirm:
        print("Passwords do not match. Try again.")
        return set_master_password()
    with open("master_pwd_txt", "w") as f:
        f.write(hash_password(master_pwd))
    print("Master password set successfully.")

#Function to verify the master password
def verify_master_password():
    master_pwd = getpass("Enter your master password: ")
    with open("master_pwd.txt", "r") as f:
        stored_pwd_hash = f.read()
    return stored_pwd_hash == hash_password(master_pwd), master_pwd

#Ensure the key file exists
try:
    key = load_key()
except FileNotFoundError:
    write_key()
    key = load_key()

#Check if the master password is set
if not master_password_exists():
    set_master_password()

#Verify the master password
is_verified, master_pwd = verify_master_password()
if not is_verified:
    print("Wrong password. Exiting.  ")
    exit()

#Combine the key and the master password using SHA-256 to ensure it is 32 bytes
combined_key = hashlib.sha256(key + master_pwd.encode()).digest()

#Base64 encode the combined key to make it a valid Fernet key
fernet_key = base64.urlsafe_b64encode(combined_key)

#Initialize the Fernet object
fer = Fernet(fernet_key)

#Function to view all the stored passwords
def view():
    try:
        with open("password.txt", "r") as f:
            for line in f.readlines():
                data = line.rstrip()
                category, user, passw = data.split("|")
                decrypted_passw = fer.decrypt(passw.encode()).decode() #Decrypt the password 
                print(f"Category: {category} | Account: {user} | Password: {decrypted_passw}")
    except FileNotFoundError:
        print("No passwords stored yet.")
    except Exception as e:
        print(f"An error occured: {e}")


# Function to view passwords by category
def view_by_category():
    category_to_view = input("Enter the category you want to view: ").strip()
    found = False
    try:
        with open("password.txt", "r") as f:
            for line in f.readlines():
                data = line.rstrip()
                category, user, passw = data.split("|")
                if category == category_to_view:
                    decrypted_passw = fer.decrypt(passw.encode()).decode()
                    print(f"Account: {user} | Password: {decrypted_passw}")
                    found = True
        if not found:
            print(f"No passwords found under the category '{category_to_view}'.")
    except FileNotFoundError:
        print("No passwords stored yet.")
    except Exception as e:
        print(f"An error occurred: {e}")

#Function to add  a new password
def add():
    category = input("Category: ")
    name = input("Account name: ")
    pwd = getpass("Password: ")
    encrypted_pwd = fer.encrypt(pwd.encode()).decode() # Encrypt the password
    with open("password.txt", "a") as f:
         f.write(f"{category}|{name}|{encrypted_pwd}\n")
    print(f"Password for {name} stored successfully under category {category}.")
    

#Function to generate and add a new password
def generate_and_add():
    category = input("Category: ")
    name = input("Account name: ")
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            break
        except ValueError:
            print("Please enter a valid number.")
    pwd = generate_password(length)
    print(f"Generated password: {pwd}")
    encrypted_pwd = fer.encrypt(pwd.encode()).decode() #Encrypt the password
    with open("password.txt", "a") as f:
        f.write(f"{category}|{name}|{encrypted_pwd}\n")
    print(f"Password for {name} stored successfully under category {category}.")
    

#Main Loop
while True:
    print("Welcome to Password Manager: ")
    print("Would you like to: ")
    print("1.Generate and add a new password\n2.Add a new password\n3.View stored passwords\n4.View passwords by category\n5.Quit")
    mode = input("Choose an option (1/2/3/4/5): ").strip()

    if mode == "5":
        print("Bye")
        break
    elif mode == "4":
        view_by_category()
    elif mode == "3":
        view()
    elif mode == "2":
        add()
    elif mode == "1":
        generate_and_add()
    else:
        print("Invalid option") 