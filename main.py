# password encrypter using hashes - by BENJAMIN SARAVIA
# NOTE: IT IS POSSIBLE THAT ONE OR SOME OF THE LIBRARIES IMPORTED IN THIS PROGRAM
# MAY NOT IMPORT PROPERLY ON DIFFERENT COMPILERS/INTERPRETERS. THIS MAY CAUSE ERRORS
# WHEN RUNNING THE CODE OR FLAWS.

import hashlib
import getpass
import time

# needed lists and variables
line = "****************************************"
hash_methods = ["1. MD5",
                "2. SHA1",
                "3. SHA256",
                "4. SHA384",
                "5. SHA512",
                "6. BLAKE 2B",
                "7. BLAKE 2S"]

salt_menu = ["1. Yes",
             "2. No"]

# this is for later salt use
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
            "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", 
            "u", "v", "w", "x", "y", "z"]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ["!", "@", "#", "%", "^", "&", "*", "(", ")",
           "-", "_", "{", "}"] 

# salt boolean is set to false and is either changed or remains the same later 
# depending on the user's input
salt_exists = False

# function that encrypts the password_value using MD5
def MD5_encryption(password_value, salt_value, salt_bool):
    
    encrypted_password = hashlib.md5(password_value.encode()).hexdigest()
    
    # checks if the user had a salt to concat or not
    # if the salt boolean is False
    if salt_bool == False:
        
        print("\nEncrypting password...")
        time.sleep(1.5)
    
        print("\nYour encrypted password is: ")
        print(str(encrypted_password))
        
    # if the salt boolean is True
    elif salt_bool == True:
        
        # salted hash
        salted_password = str(salt_value) + str(encrypted_password)
        
        print("\nEncrypting password...")
        time.sleep(1.5)
        
        print("\nYour encrypted password is: ")
        print(str(salted_password))

# function that encrypts the password_value using SHA1
def SHA1_encryption(password_value, salt_value, salt_bool):
    
    encrypted_password = hashlib.sha1(password_value.encode()).hexdigest()   
    
    if salt_bool == False:
        
        print("\nEncrypting password...")
        time.sleep(1.5)
    
        print("\nYour encrypted password is: ")
        print(str(encrypted_password))
        
    # if the salt boolean is True
    elif salt_bool == True:
        
        # salted hash
        salted_password = str(salt_value) + str(encrypted_password)
        
        print("\nEncrypting password...")
        time.sleep(1.5)
        
        print("\nYour encrypted password is: ")
        print(str(salted_password))

# function that encrypts the password_value using SHA 256
def SHA256_encryption(password_value, salt_value, salt_bool):
    
    encrypted_password = hashlib.sha256(password_value.encode()).hexdigest()   
    
    if salt_bool == False:
        
        print("\nEncrypting password...")
        time.sleep(1.5)
    
        print("\nYour encrypted password is: ")
        print(str(encrypted_password))
        
    # if the salt boolean is True
    elif salt_bool == True:
        
        # salted hash
        salted_password = str(salt_value) + str(encrypted_password)
        
        print("\nEncrypting password...")
        time.sleep(1.5)
        
        print("\nYour encrypted password is: ")
        print(str(salted_password))

# function that encrypts the password_value using SHA 384
def SHA384_encryption(password_value, salt_value, salt_bool):
    
    encrypted_password = hashlib.sha384(password_value.encode()).hexdigest()   
    
    if salt_bool == False:
        
        print("\nEncrypting password...")
        time.sleep(1.5)
    
        print("\nYour encrypted password is: ")
        print(str(encrypted_password))
        
    # if the salt boolean is True
    elif salt_bool == True:
        
        # salted hash
        salted_password = str(salt_value) + str(encrypted_password)
        
        print("\nEncrypting password...")
        time.sleep(1.5)
        
        print("\nYour encrypted password is: ")
        print(str(salted_password))

# function that encrypts the password_value using SHA 512
def SHA512_encryption(password_value, salt_value, salt_bool):
    
    encrypted_password = hashlib.sha512(password_value.encode()).hexdigest() 
    
    if salt_bool == False:
        
        print("\nEncrypting password...")
        time.sleep(1.5)
    
        print("\nYour encrypted password is: ")
        print(str(encrypted_password))
        
    # if the salt boolean is True
    elif salt_bool == True:
        
        # salted hash
        salted_password = str(salt_value) + str(encrypted_password)
        
        print("\nEncrypting password...")
        time.sleep(1.5)
        
        print("\nYour encrypted password is: ")
        print(str(salted_password))
    
# function that encrypts the password_value using BLAKE 2B (64 bit)
def BLAKE2B_encryption(password_value, salt_value, salt_bool):
    
    encrypted_password = hashlib.blake2b(password_value.encode()).hexdigest() 
    
    if salt_bool == False:
        
        print("\nEncrypting password...")
        time.sleep(1.5)
    
        print("\nYour encrypted password is: ")
        print(str(encrypted_password))
        
    # if the salt boolean is True
    elif salt_bool == True:
        
        # salted hash
        salted_password = str(salt_value) + str(encrypted_password)
        
        print("\nEncrypting password...")
        time.sleep(1.5)
        
        print("\nYour encrypted password is: ")
        print(str(salted_password))
    
# function that encrypts the password_value using BLAKE 2S (1 to 32 bit)
def BLAKE2S_encryption(password_value, salt_value, salt_bool):
    
    encrypted_password = hashlib.blake2s(password_value.encode()).hexdigest() 
    
    if salt_bool == False:
        
        print("\nEncrypting password...")
        time.sleep(1.5)
    
        print("\nYour encrypted password is: ")
        print(str(encrypted_password))
        
    # if the salt boolean is True
    elif salt_bool == True:
        
        # salted hash
        salted_password = str(salt_value) + str(encrypted_password)
        
        print("\nEncrypting password...")
        time.sleep(1.5)
        
        print("\nYour encrypted password is: ")
        print(str(salted_password))

# main function where the user chooses what encryption to use
def main():
    
    # try loop declared for error handling
    try:
        
        while True:
    
            print(line)
            print("   🔒 JIRACHI'S PASSWORD ENCRYPTER🔒 ")
            print(line)
    
            # having the user decide whether or not they would like to add a salt to their hash
            time.sleep(2)
            print("\nFirstly, would you like to add salt to your hash? 🧂")
            for choice in salt_menu:
                
                print(choice)
                
            salt_choice = int(input('Choose here: >'))
            
            # if the user chooses to make a salt
            if salt_choice == 1:
                
                # the salt_exists bool is set to True
                salt_exists = True
                salt = input("\nType your custom salt here (cannot exceed 32 characters): ")
                # an if statement to check if the salt length exceeds 32 characters or
                # is less than 0 characters
                if len(salt) > 32 or len(salt) < 0:
                    
                    print("\nSYSTEM: Salt cannot exceed 32 characters nor can it be 0 characters. Please try again.\n")
                    continue
                
                else:
                    
                    # concatenating the salt $s to the salt to make it clear that it is a salt
                    salt = "$" + str(salt) + "$"
                    time.sleep(1.2)
                    print("\nSYSTEM: Salt created!")
            
            # if the user chooses not to make a salt    
            elif salt_choice == 2:
                
                # the salt_exists bool is set to False
                salt_exists = False
                salt = ""
                time.sleep(1.2)
                print("\nSYSTEM: No salt chosen.")
                
            else:
                
                print("\nSYSTEM: That is not a valid input. Please try again.\n")
                time.sleep(1.5)
                continue
                
            time.sleep(1.5)
            print("\nChoose an encryption method for your password here: ")
    
            for hash in hash_methods:
        
                print(hash)
                
            hash_choice = int(input("\nType in the corresponding number here: "))
    
            # error handling the hash method the user chose
            # if the user chose a value not 1 to 5
            if hash_choice not in range(1, 8):
        
                print("\nSYSTEM ERROR: Please choose a number from 1 to 6.\n")
                time.sleep(1.5)
                continue
     
            # if the user chose a hash method from 1 to 6 
            else:
        
                # starting a new loop that is more personal and tells the user what methods
                # they chose
                if hash_choice == 1:
            
                    print("\nENCRYPTION METHOD: MD5")
                    password = getpass.getpass("Type or copy and paste your password here "
                                            "(it will appear hidden): ")
                
                    MD5_encryption(password, salt, salt_exists)
                    break
            
                elif hash_choice == 2:
            
                    print("\nENCRYPTION METHOD: SHA1")
                    password = getpass.getpass("Type or copy and paste your password here "
                                            "(it will appear hidden): ")
                
                    SHA1_encryption(password, salt, salt_exists)
                    break
            
                elif hash_choice == 3:
            
                    print("\nENCRYPTION METHOD: SHA256")
                    password = getpass.getpass("Type or copy and paste your password here "
                                            "(it will appear hidden): ")
                
                    SHA256_encryption(password, salt, salt_exists)
                    break
            
                elif hash_choice == 4:
            
                    print("\nENCRYPTION METHOD: SHA384")
                    password = getpass.getpass("Type or copy and paste your password here "
                                            "(it will appear hidden): ")
                
                    SHA384_encryption(password, salt, salt_exists)
                    break
            
                elif hash_choice == 5:
            
                    print("\nENCRYPTION METHOD: SHA512")
                    password = getpass.getpass("Type or copy and paste your password here "
                                           "(it will appear hidden): ")
                
                    SHA512_encryption(password, salt, salt_exists)
                    break
                
                elif hash_choice == 6:
            
                    print("\nENCRYPTION METHOD: BLAKE 2B")
                    password = getpass.getpass("Type or copy and paste your password here "
                                           "(it will appear hidden): ")
                
                    BLAKE2B_encryption(password, salt, salt_exists)
                    break
                    
                elif hash_choice == 7:
            
                    print("\nENCRYPTION METHOD: BLAKE 2S")
                    password = getpass.getpass("Type or copy and paste your password here "
                                           "(it will appear hidden): ")
                
                    BLAKE2S_encryption(password, salt, salt_exists)
                    break
    
    # if the user inputs something invalid        
    except ValueError:
        
        print("Please enter a valid input.")
        main()
    
    # if the user prompts CTRL + C   
    except KeyboardInterrupt:
        
        print("\n")
        print("SYSTEM: CTRL + C detected.")
        error_resolve = input("Was this intentional? (Y / N): >")
        
        if error_resolve.upper() == "Y":
            
            print("\nClosing the password encrypter...")
            
        else:
            
            print("\nRe-opening the password encrypter...")
            print("\n")
            time.sleep(1.5)
            main()
            
main()
