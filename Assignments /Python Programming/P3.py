import subprocess
import re

url = "https://faridfarahmand.net/firstpage.html"

page = subprocess.check_output(["curl", "-s", url], text=True)

match = re.search(r"Secret Code:\s*(\S+)", page, re.IGNORECASE)

if match:
    print(match.group(1))
