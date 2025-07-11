#!/usr/bin/env python3

import socket
import sys

def banner_grab(ip, port):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((ip, port))
        s.send(b'HEAD / HTTP/1.0\r\n\r\n')
        banner = s.recv(1024).decode()
        print(f"[+] Banner on {ip}:{port}:\n{banner}")
    except:
        print(f"[!] Failed to connect to {ip}:{port}")
    finally:
        s.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 reconcreep.py <target-ip>")
        sys.exit(1)

    target = sys.argv[1]
    common_ports = [21, 22, 80, 443, 8080]

    for port in common_ports:
        banner_grab(target, port)
