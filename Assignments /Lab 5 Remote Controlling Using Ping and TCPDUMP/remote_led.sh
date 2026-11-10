#!/bin/bash

# EE 465 - Project 3.1
# Remote LED and OLED Control Using TCPdump

GPIO=24
INTERFACE="wlan0"
OLED_PYTHON="/home/tklahr/oled-env/bin/python3"
OLED_SCRIPT="/home/tklahr/oled_message.py"

# Initialize LED
pinctrl set "$GPIO" op dl

echo "Listening for ping commands..."
echo "Press Ctrl+C to stop."

# Clean up background processes
cleanup() {
    trap - EXIT
    kill "$ON_PID" "$OFF_PID" "$OTHER_PID" 2>/dev/null
    wait 2>/dev/null
}

trap cleanup EXIT

# LED ON: aa ae
tcpdump -i "$INTERFACE" -nn -l \
'icmp[icmptype] = icmp-echo and (icmp[8:2] = 0xaaae or icmp[24:2] = 0xaaae)' 2>/dev/null |
while IFS= read -r packet; do
    pinctrl set "$GPIO" dh
    "$OLED_PYTHON" "$OLED_SCRIPT" "LED ON"
    echo "Ping received: LED ON"
done &
ON_PID=$!

# LED OFF: ab ae
tcpdump -i "$INTERFACE" -nn -l \
'icmp[icmptype] = icmp-echo and (icmp[8:2] = 0xabae or icmp[24:2] = 0xabae)' 2>/dev/null |
while IFS= read -r packet; do
    pinctrl set "$GPIO" dl
    "$OLED_PYTHON" "$OLED_SCRIPT" "LED OFF"
    echo "Ping received: LED OFF"
done &
OFF_PID=$!

# Unknown ping pattern
tcpdump -i "$INTERFACE" -nn -l \
'icmp[icmptype] = icmp-echo and not (icmp[8:2] = 0xaaae or icmp[24:2] = 0xaaae or icmp[8:2] = 0xabae or icmp[24:2] = 0xabae)' 2>/dev/null |
while IFS= read -r packet; do
    "$OLED_PYTHON" "$OLED_SCRIPT" "Unknown Ping"
    echo "Ping received: Unknown pattern"
done &
OTHER_PID=$!

wait
