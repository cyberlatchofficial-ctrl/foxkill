🦊 FoxKill: Advanced Network Access Controller
FoxKill is a powerful Python-based security tool designed for network penetration testing and research. Utilizing ARP Spoofing techniques, it allows users to monitor and selectively disconnect devices from a local network.

⚡ Key Features
Nuclear Scan Mode: A high-intensity, 10-pass bruteforce discovery engine that detects every active device on the network, bypassing standard silent-host defenses.

Targeted Termination: Precision-kill functionality to disconnect specific IP addresses.

Total Lockdown (Rage Mode): Instantly disconnect every device on the network (excluding the host) with a single command.

Auto-Restoration: Intelligent cleanup protocol that restores network connectivity for targets upon exit.

Optimized Engine: Built to leverage high-performance hardware (like Ryzen 7) for near-instant packet injection.

⚠️ Legal Disclaimer
FOR EDUCATIONAL PURPOSES ONLY. Accessing or disrupting networks without explicit permission is illegal and unethical. This tool is intended for authorized security auditing and educational research only. The developer assumes no liability for misuse.

🛠️ Installation & Setup
Follow these steps to deploy FoxKill on your Kali Linux or any Debian-based system:

1. Clone the Repository
Download the source code from GitHub:

Bash
git clone https://github.com/Cyberlatchofficial/FoxKill.git
cd FoxKill
2. Install Required Dependencies
FoxKill requires scapy and colorama. Install them using the following command:

Bash
pip install -r requirements.txt --break-system-packages
3. Install Network Tools
Ensure nmap is installed for the Nuclear Scan feature to function at full capacity:

Bash
sudo apt update && sudo apt install nmap -y
🚀 Execution Guide
To launch the tool, you must have root privileges as it interacts directly with the network interface:

Bash
sudo python3 foxkill.py
Operation Steps:
Initialization: The tool automatically detects your Gateway IP and local network range.

Network Discovery: Wait for the Nuclear Scan to complete. It will display a table of all connected devices with their IP and MAC addresses.

Select Target:

Enter 0 to activate Total Lockdown (Kill everyone).

Enter a specific ID number from the list to kill a single target.

Cease Attack: Press Ctrl + C to stop the attack and automatically restore the targets' internet access.

📂 Project Structure
foxkill.py: The main user interface and scanning logic.

engine.py: The core attack engine and packet injection logic.

requirements.txt: List of necessary Python libraries.

👨‍💻 Developed By
Cyberlatchofficial Mission: Zero Device Escape
