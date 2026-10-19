#!/bin/bash

# Wait up to 60 seconds for an IPv4 address
for i in {1..60}; do
    myIPAddress=$(ip -4 -o addr show wlan0 | awk '{print $4}' | cut -d/ -f1)
    [ -n "$myIPAddress" ] && break
    sleep 1
done

# Get MAC address
myMACAddress=$(cat /sys/class/net/wlan0/address)

# Send addresses if an IP address exists
if [ -n "$myIPAddress" ]; then
    curl -fsS --retry 5 --retry-delay 5 \
        -X POST https://faridfarahmand.net/EE465/checkipaddress.php \
        -d "IpAddress=$myIPAddress" \
        -d "MACAddress=$myMACAddress" \
        -o /dev/null

    echo "IP and MAC submission completed."
else
    echo "No IP address found."
    exit 1
fi
