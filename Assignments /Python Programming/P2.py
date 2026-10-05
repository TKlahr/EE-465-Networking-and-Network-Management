with open("/etc/resolv.conf", "r") as file:
    for line in file:
        if line.startswith("nameserver"):
            print(line.split()[1])
            break
