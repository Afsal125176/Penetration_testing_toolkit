import socket

def grab_banner(target, port):
    try:
        s = socket.socket()
        s.connect((target, port))
        s.send(b'Hello\r\n')
        banner = s.recv(1024)
        print(f"[+] Banner from {target}:{port} → {banner.decode().strip()}")
        s.close()
    except Exception as e:
        print(f"[!] Could not grab banner: {e}")
