from scapy.all import IP, ICMP, Raw, send

# Raspberry Pi IP address
PI_IP = "192.168.12.157"

# Choose a command
command = input("Enter ON, OFF, or UNKNOWN: ").strip().upper()

if command == "ON":
    payload = bytes.fromhex("aaae")
elif command == "OFF":
    payload = bytes.fromhex("abae")
elif command == "UNKNOWN":
    payload = bytes.fromhex("1234")
else:
    print("Invalid command")
    exit()

# Create and send ICMP Echo Request
packet = IP(dst=PI_IP) / ICMP(type=8) / Raw(load=payload * 2)

send(packet, count=1, verbose=False)

print(f"Sent {command} command to {PI_IP}")
