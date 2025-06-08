import pyzipper
import os

def brute_force_zip(zip_file_path, wordlist_file_path):
    if not os.path.isfile(zip_file_path):
        print(f"[-] File ZIP '{zip_file_path}' tidak ditemukan.")
        return

    if not os.path.isfile(wordlist_file_path):
        print(f"[-] Wordlist '{wordlist_file_path}' tidak ditemukan.")
        return

    with open(wordlist_file_path, 'r', errors='ignore') as file:
        passwords = file.readlines()

    for count, password in enumerate(passwords):
        password = password.strip()
        try:
            with pyzipper.AESZipFile(zip_file_path) as zf:
                zf.pwd = bytes(password, 'utf-8')
                zf.extractall()
                print(f"[+] Password ditemukan: {password}")
                return
        except RuntimeError as e:
            print(f"[-] Salah ke-{count + 1}: {password}")
        except Exception as e:
            print(f"[!] Error lain: {e}")
            continue

    print("[-] Password tidak ditemukan di wordlist.")

# ==================================
#   Brute Force ZIP Password Tool
# ==================================
if __name__ == "__main__":
    print("=== AES ZIP Password Brute Force Tool ===\n")
    zip_path = input("[?] Masukkan path ke file ZIP: ").strip('"')
    wordlist_path = input("[?] Masukkan path ke wordlist: ").strip('"')
    brute_force_zip(zip_path, wordlist_path)