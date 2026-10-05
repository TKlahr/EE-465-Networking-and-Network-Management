import subprocess

result = subprocess.run(
    ["curl", "-s", "https://faridfarahmand.net/firstpage.html"],
    capture_output=True,
    text=True
)

for line in result.stdout.splitlines():
    if "Secret Code:" in line:
        code = line.split("Secret Code:")[1].split("</p>")[0].strip()
        print(code)
