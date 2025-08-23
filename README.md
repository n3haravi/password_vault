#  Python Password Vault

This is a mini password manager (LastPass-style) built using Python. It securely stores your service credentials using strong encryption and allows you to view them only with the correct master password.

> **Disclaimer**: This project is for educational purposes only. Do not use it to store real passwords or deploy it in production environments without further security measures.

---

##  Concepts Implemented

- AES encryption using the 'cryptography' library ('Fernet')
- Master-password-based key derivation
- Encrypted storage of credentials in a local file
- Simple command-line interface (CLI) for interaction
- File handling and input validation

---

## Tools Used

- Python 3.x
- 'cryptography' library (for encryption)
- Terminal / Command Line Interface (CLI)
- VS Code (optional for editing)

---

##  Workflow

### Master Password Setup
The vault uses a master password entered at launch to derive an encryption key.

### Add Entries
Each new credential (service, username, password) is encrypted and stored in a file named 'credentials.txt'.

### View Entries
Only the correct master password can decrypt and display the stored data.

---

## Screenshot

<img width="1787" height="847" alt="Screenshot (1578)" src="https://github.com/user-attachments/assets/8721f921-00c9-41c6-b3d8-168fe0d80b6a" />


---


