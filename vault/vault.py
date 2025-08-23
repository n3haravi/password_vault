from cryptography.fernet import Fernet
import os
import base64
import hashlib

class PasswordVault:
    def __init__(self, master_password):
        self.key = self._derive_key(master_password)
        self.fernet = Fernet(self.key)
        self.file = "vault/credentials.txt"
        if not os.path.exists(self.file):
            open(self.file, "w").close()

    def _derive_key(self, password):
        hashed = hashlib.sha256(password.encode()).digest()
        return base64.urlsafe_b64encode(hashed)

    def add_entry(self, service, username, password):
        encrypted = self.fernet.encrypt(f"{service},{username},{password}".encode())
        with open(self.file, "ab") as f:
            f.write(encrypted + b"\n")

    def view_entries(self):
        with open(self.file, "rb") as f:
            lines = f.readlines()
            for line in lines:
                try:
                    decrypted = self.fernet.decrypt(line.strip()).decode()
                    service, username, password = decrypted.split(",")
                    print(f"Service: {service} | Username: {username} | Password: {password}")
                except Exception:
                    print("Could not decrypt a line – wrong master password?")
