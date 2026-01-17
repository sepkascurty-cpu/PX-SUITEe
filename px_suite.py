import socket
import requests
from colorama import Fore, Style, init

# Inisialisasi warna untuk Windows/Linux
init(autoreset=True)

def show_banner():
    banner = f"""
    {Fore.CYAN}
    ██████╗ ██╗  ██╗      ███████╗██╗   ██╗██╗████████╗███████╗
    ██╔══██╗╚██╗██╔╝      ██╔════╝██║   ██║██║╚══██╔══╝██╔════╝
    ██████╔╝ ╚███╔╝ █████╗███████╗██║   ██║██║   ██║   █████╗  
    ██╔═══╝  ██╔██╗ ╚════╝╚════██║██║   ██║██║   ██║   ██╔════╝
    ██║     ██╔╝ ██╗      ███████║╚██████╔╝██║   ██║   ███████╗
    ╚═╝     ╚═╝  ╚═╝      ╚══════╝ ╚═════╝ ╚═╝   ╚═╝   ╚══════╝
    {Fore.GREEN}      >> Cybersecurity Toolkit v1.5 | Created by: sepkascurty-cpu <<
    """
    print(banner)

def port_scanner():
    print(f"\n{Fore.YELLOW}[*] Starting Port Scanner...")
    target = input(f"{Fore.WHITE}Masukkan Target (IP/Domain): ").strip()
    # List port yang paling sering jadi celah
    common_ports = [21, 22, 23, 25, 53, 80, 110, 443, 3306, 8080]
    
    print(f"{Fore.CYAN}[+] Scanning {target}...")
    for port in common_ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"{Fore.GREEN}  [!] Port {port} is OPEN")
        s.close()
    print(f"{Fore.YELLOW}[*] Scan Selesai.")

def banner_grabber():
    print(f"\n{Fore.YELLOW}[*] Starting Banner Grabber...")
    target = input(f"{Fore.WHITE}Masukkan Target IP: ").strip()
    port = int(input(f"{Fore.WHITE}Masukkan Port: "))
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((target, port))
        banner = s.recv(1024).decode().strip()
        print(f"\n{Fore.GREEN}[SUCCESS] Banner: {Fore.WHITE}{banner}")
        s.close()
    except Exception as e:
        print(f"{Fore.RED}[ERROR] Tidak bisa mengambil banner: {e}")

def dir_buster():
    print(f"\n{Fore.YELLOW}[*] Starting Directory Buster...")
    target_url = input(f"{Fore.WHITE}Masukkan URL (contoh: google.com): ").strip()
    # List directory populer untuk dicheck
    wordlist = ["admin", "login", "config", "backup", "v1", "api", "uploads", "phpmyadmin"]
    
    print(f"{Fore.CYAN}[+] Mencari folder tersembunyi di {target_url}...")
    for folder in wordlist:
        url = f"http://{target_url}/{folder}"
        try:
            response = requests.get(url, timeout=2)
            if response.status_code == 200:
                print(f"{Fore.GREEN}  [!] DITEMUKAN: {url} (Status: 200)")
            elif response.status_code == 403:
                print(f"{Fore.RED}  [!] TERLARANG: {url} (Status: 403)")
        except:
            pass
    print(f"{Fore.YELLOW}[*] Scan Selesai.")

def main():
    while True:
        show_banner()
        print(f"{Fore.WHITE}Menu Pilihan:")
        print(f"  1. Port Scanner (Recon)")
        print(f"  2. Banner Grabber (Service Info)")
        print(f"  3. Directory Buster (Web Discovery)")
        print(f"  4. Exit")
        
        choice = input(f"\n{Fore.GREEN}PX-Shell > ").strip()
        
        if choice == "1":
            port_scanner()
        elif choice == "2":
            banner_grabber()
        elif choice == "3":
            dir_buster()
        elif choice == "4":
            print(f"{Fore.RED}Mematikan sistem... Sampai jumpa, Agent.")
            break
        else:
            print(f"{Fore.RED}[!] Pilihan salah!")
        
        input(f"\n{Fore.CYAN}Tekan Enter untuk kembali ke menu...")

if __name__ == "__main__":
    main()
