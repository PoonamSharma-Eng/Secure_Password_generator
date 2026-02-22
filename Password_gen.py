import random
import string

def password_generator():
    print("--- 🔐 Non-Stop Secure Password Generator ---")
    print("Type 'exit' to stop the program")

    while True:
        user_input = input("\nEnter password length (or type 'exit'): ").lower()

        if user_input == 'exit':
            print("Shutting down. Stay safe! 👋")
            break  

        try:
            length = int(user_input)
            
            if length < 4:
                print("Error: Minimum 4 characters required for security!")
                continue # Nayi cycle shuru karega

          
            letters = string.ascii_letters 
            digits = string.digits
            safe_symbols = "@#$!%&*?" 
            all_chars = letters + digits + safe_symbols
            
            # Random logic
            password = "".join(random.choice(all_chars) for i in range(length))
            
            print(f"Generated Password: {password}")
            print("-" * 30)
            
        except ValueError:
            print("Invalid input! Please enter a number or type 'exit'.")

password_generator()
