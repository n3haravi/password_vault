from vault.vault import PasswordVault


def menu():
    print("\nPassword Vault Menu")
    print("1. Add new credential")
    print("2. View stored credentials")
    print("3. Exit")

def main():
    master_pwd = input("Enter your master password: ")
    vault = PasswordVault(master_pwd)

    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            service = input("Service name: ")
            username = input("Username: ")
            password = input("Password: ")
            vault.add_entry(service, username, password)
            print("Entry added successfully.")
        elif choice == "2":
            vault.view_entries()
        elif choice == "3":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
