# 🦊 FoxKill

Advanced ARP Spoofing tool to disconnect any device from your local network.

## 🧐 What is FoxKill?

**FoxKill** is a powerful network security tool designed to perform ARP Spoofing attacks. It allows you to scan your local network, identify active devices, and selectively or globally terminate their internet connection. 

> **🚀 A Nuclear Scan feature has been added to detect even the most hidden devices.**

---

## ⚡ Features

* **Nuclear Scan:** 10x repetition bruteforce scanning to find every single device.
* **Targeted Kill:** Disconnect a specific device by its ID.
* **Rage Mode (Total Lockdown):** Disconnect every device on the network at once.
* **Auto-Restore:** Automatically restores network connectivity upon exit (Ctrl+C).
* **High Performance:** Optimized to run smoothly on systems like Ryzen 7.

---

## 💻 This Tool Tested On:

* **Kali Linux**
* **Termux (Rooted)**
* **Ubuntu**
* **Parrot Security OS**

---

## 🛠️ Installing and Requirements

This tool requires **Python 3**, **Scapy**, and **Nmap**. First, install the system dependencies:

📥 Step-by-Step Installation:

1.
sudo apt-get update && sudo apt-get install nmap python3-pip -y

2.
git clone https://github.com/cyberlatchofficial-ctrl/foxkill.git

3.
cd foxkill

4.
pip install -r requirements.txt --break-system-packages

5.
sudo python3 foxkill.py


📜 Change Log:
Version: 1.0 - Initial Release
✅ Added: Nuclear Scan (Bruteforce Device Detection).

✅ Added: FoxEngine for stable packet injection.

✅ Added: Total Lockdown mode (ID 0).

✅ Added: Colorized terminal interface for better UX.

⚠️ Important Notice
Unauthorized use of this tool on networks you don't own is strictly prohibited.

For more videos, subscribe to our YouTube Channel:
👉 www.youtube.com/@CyberLatch

Disclaimer: FoxKill is created for educational purposes and authorized penetration testing only. The developer is not responsible for any misuse or illegal activities.
