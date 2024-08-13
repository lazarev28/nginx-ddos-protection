import sys

def handle_banned_ip(ip):
    print(f"IP {ip} заблокирован")

if __name__ == "__main__":
    ip_address = sys.argv[1]
    handle_banned_ip(ip_address)