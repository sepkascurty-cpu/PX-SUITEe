import socket
from colorama import Fore, Style, init

# Inisialisasi warna
init(autoreset=True)

def show_banner():
    banner = f"""
    {Fore.CYAN}#################################################
    #                                               #
    #   {Fore.GREEN}PX-SUITE v1.0 - Cybersecurity Toolkit{Fore.CYAN}       #
    #   {Fore.YELLOW}Created by: sepkascurty-cpu{Fore.CYAN}                 #
    #                                               #
    #################################################
    """
    print(banner)

def port_scanner():
    print(f"\n{Fore.YELLOW}[*] Starting Port Scanner...")
    target = input("Masukkan Target (IP/Domain): ")
    ports = [21, 22, 80, 443, 8080]
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"{Fore.GREEN}[+] Port {port} is OPEN")
        s.close()

def banner_grabber():
    print(f"\n{Fore.YELLOW}[*] Starting Banner Grabber...")
    target = input("Masukkan Target IP: ")
    port = int(input("Masukkan Port: "))
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((target, port))
        banner = s.recv(1024).decode().strip()
        print(f"{Fore.CYAN}[BANNER]: {banner}")
    except:
        print(f"{Fore.RED}[-] Gagal mengambil banner.")

def main():
    while True:
        show_banner()
        print(f"{Fore.WHITE}1. Port Scanner")
        print(f"{Fore.WHITE}2. Banner Grabber")
        print(f"{Fore.WHITE}3. Exit")
        
        choice = input(f"\n{Fore.GREEN}PX-Shell > ")
        
        if choice == "1":
            port_scanner()
        elif choice == "2":
            banner_grabber()
        elif choice == "3":
            print(f"{Fore.RED}Exiting...")
            break
        else:
            print(f"{Fore.RED}Pilihan salah!")

if __name__ == "__main__":
    main()
