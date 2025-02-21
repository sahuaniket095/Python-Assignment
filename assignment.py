# Python Course Assignment 1

def encrypt(message, key):
    """Encrypting the message by shifting ASCII values by the key:
    - Using a generator expression to iterate over each character in the message, 
    - Applying the ASCII shift, & joining the results into a single string. """
    return ''.join(chr((ord(char) + key - 32) % 95 + 32) for char in message)

def decrypt(encrypted_message, key):
    """Decrypting the message by shifting ASCII values backward by the key:
    - Using a generator expression to iterate over each character in the encrypted message, 
    - Applying the reverse ASCII shift, & joining the results into a single string. """
    return ''.join(chr((ord(char) - key - 32) % 95 + 32) for char in encrypted_message)

def main():
    # Taking user input for message, key, and mode
    message = input("Enter the message: ")  # Asking the user to enter the message to encrypt or decrypt
    key = int(input("Enter the key (an integer): "))  # Asking the user to enter a numeric key for encryption or decryption
    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()  # Asking the user to choose between encrypt or decrypt & converting to lowercase for consistency

    if mode == "encrypt":  # If the user selects the 'encrypt' mode
        result = encrypt(message, key)  # Calling the encrypt function with the message & key
        print("Encrypted message:", result)  # Printing the encrypted result
    elif mode == "decrypt":  # If the user selects the 'decrypt' mode
        result = decrypt(message, key)  # Calling the decrypt function with the encrypted message & key
        print("Decrypted message:", result)  # Printing the decrypted result
    else:  # If the user enters an invalid mode
        print("Invalid mode selected. Please choose 'encrypt' or 'decrypt'.")  # Informing the user of the invalid input

# This checks if the script is being run directly (not imported as a module).
# If true, it calls the main function to start the program.
if __name__ == "__main__":
    main()  # Calling the main function to execute the program
