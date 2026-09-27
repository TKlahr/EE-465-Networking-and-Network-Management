import subprocess

result = subprocess.check_output(["nslookup", "google.com"], text=True)

for line in result.splitlines():
    if line.startswith("Address:"):
        address = line.split("Address:")[1].strip()
        address = address.split("#")[0]
        print(address)
        break
