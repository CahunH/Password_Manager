from app.manager import generate_key, save_key, load_key, add_password, retrieve_password, list_passwords
import os

def main():
    key_file = '/usr/src/app/data/key.key'
    password_file = '/usr/src/app/data/passwords.json'

    os.makedirs(os.path.dirname(key_file), exist_ok=True)

    if not os.path.exists(key_file):
        key = generate_key()
        save_key(key, key_file)
    else:
        key = load_key(key_file)

    while True:
        print("1. Add a new password")
        print("2. Retrieve a password")
        print("3. List all stored passwords")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            site = input("Enter the site name: ")
            password = input("Enter the password: ")
            add_password(key, site, password, password_file)
            print("Password added successfully!")
        elif choice == '2':
            site = input("Enter the site name: ")
            password = retrieve_password(key, site, password_file)
            if password:
                print(f"The password for {site} is: {password}")
            else:
                print("Password not found.")
        elif choice == '3':
            sites = list_passwords(password_file)
            if sites:
                print("Stored passwords for sites:")
                for site in sites:
                    print(site)
            else:
                print("No passwords stored.")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
