import hashlib
import getpass

password_manager = {}

#The code behind creating the user account
def create_account():
    username = input("Enter your desired username: ")
    password = getpass.getpass("Enter your desired password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    password_manager[username] = hashed_password
    print("Account created Successfully!")
    
#The code behind saving the user data and allow the user to relogin again to the system
def login():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if username in password_manager.keys() and password_manager[username] == hashed_password:
        print("Login Successful!")
    else:
        print("Invalid Credentials! Please try again.")
        
def main():
    #while loop
    while True:
        choice = input("Enter 1 to create an account, 2 to login, or 0 to EXIT SYSTEM: ")#
        
    #if statment selection
        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

#loop back the whole code            
if __name__ == "__main__":
    main()