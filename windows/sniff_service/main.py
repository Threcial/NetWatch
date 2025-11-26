import os
from scapy.all import ARP, DHCP,sniff
import json
from datetime import datetime
from win11toast import toast
from .events import DeviceEvent


KNOWN_FILE = os.path.join(os.path.dirname(__file__), "known_macs.json")

def load_known_macs():
    if not os.path.exists(KNOWN_FILE):
        return set()
    try:
        with open(KNOWN_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        return set(m.lower() for m in data)
    except Exception:
        return set()
    
known_macs = load_known_macs()

def save_known_mac(mac_set):
    with open(KNOWN_FILE, "w", encoding="utf-8") as f:
        json.dump(list(mac_set), f, ensure_ascii=False, indent=2)

def show_toast(title, msg):
    toast(
        title = title,
        body = msg,
        duration = "long"
    )

def start_sniff(event_callback=None):
    def _emit_event(mac, ip, info):
        event = DeviceEvent(
            type="new_device",
            time=datetime.now(),
            mac=mac,
            ip=ip,
            info=info
        )

        if event_callback:
            event_callback(event)
        else:
            print(event)

    def handle_packet(pkt):
        global known_macs

        mac = None
        ip = None
        info = ""

        if pkt.haslayer(ARP):
            mac = pkt[ARP].hwsrc
            ip = pkt[ARP].psrc
            info = "ARP"
        elif pkt.haslayer(DHCP):
            mac = pkt.src
            info = "DHCP"
        if mac:
            mac = mac.lower()
            if mac not in known_macs:
                known_macs.add(mac)
                save_known_mac(known_macs)
                _emit_event(mac, ip, info)

    sniff(
        filter="arp or (udp and (port 67 or 68))",
        prn=handle_packet,
        store=0
    )

if __name__ == "__main__":
    start_sniff()