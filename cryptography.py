def encrypt_password(password):
    #1. Write the variable encrypted password and set it equal to ""
    encrypted_password = ""
    #2. Write a for loop for char in password
    for char in password:
        if char.isalpha():
            #3. Write the variable ascii_val and set it equal to ord(char)
            ascii_val = ord(char)
            shifted_val = (ascii_val - 97 + 3) % 26 + 97
            #4. Write the variable encrypted_password set it plus and equal to chr open and close parentheses with shifted_val inside
            encrypted_password += chr(shifted_val)
        #5. Write an else statement starting with else
        else:
            #6. Write the variable encrypted_password and set it to plus and equal to char
            encrypted_password += char
    #7. Write return and the variable used in number 6
    return encrypted_password
def decrypt_password(password):
    #8. Write the variable decrypted_password and set it equal to ""
    decrypted_password = ""
    #9. Write a for loop for char in password
    for char in password:
        if char.isalpha():
            ascii_val = ord(char)
            shifted_val = (ascii_val - 97 -3) % 26 + 97
            decrypted_password += chr(shifted_val)
        # 10. Write an else statement starting with else
        else:
            #11. Write the variable decrypted_password and set it to plus and equal to char
            decrypted_password += char
    # 12. Write return and the variable used in number 6
    return decrypted_password
def main():
      
    #13. Create an input variable that says "Please enter a password: "
    password = input("Please enter a password:\t")
    # 14. Write a print statement that says "Please choose the following options"
    print("Please choose from the following:")
    # 15. Write a print statement that says "1 = Encrypt"
    print("1 = Encrypt")
    # 16. Write a print statement that says "2 = Decrypt the password"
    print("2 = Decrypt the password")
    choice = int(input())

    if choice == 1:
        encrypted_password = encrypt_password(password.lower())
        print("Encrypted Password: ", encrypted_password)
    elif choice == 2:
        decrypted_password = decrypt_password(password.lower())
        print("Decrypted Password:", decrypted_password)
    else:
        print("Error: Invalid Choice")

if __name__ == "__main__":
    main()
        


