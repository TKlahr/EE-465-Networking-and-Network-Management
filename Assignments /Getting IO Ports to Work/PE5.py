import subprocess
from pathlib import Path

# Directory containing PE0.py through PE4.py
BASE_DIR = Path(__file__).resolve().parent

programs = {
    "0": ("PE0: Sum of Numbers", "PE0.py"),
    "1": ("PE1: Button Detection", "PE1.py"),
    "2": ("PE2: Ping Google with Button", "PE2.py"),
    "3": ("PE3: Incoming Ping LED", "PE3.py"),
    "4": ("PE4: Wi-Fi Control", "PE4.py")
}

while True:
    print("\n-------------------------------")
    print(" Raspberry Pi Programming Menu")
    print("-------------------------------")

    for key, (description, filename) in programs.items():
        print(f"{key}) {description}")

    print("5) Exit")
    print("-------------------------------")

    choice = input("Enter Your Choice: ").strip()

    if choice == "5":
        print("Exiting program.")
        break

    if choice in programs:
        description, filename = programs[choice]
        filepath = BASE_DIR / filename

        if not filepath.is_file():
            print(f"Error: {filename} not found.")
            continue

        print(f"\nRunning {description}...")
        print("Press Ctrl+C to return to the menu.\n")

        try:
            command = ["python3", str(filepath)]

            # PE4 requires administrator privileges
            if choice == "4":
                command = ["sudo", "-n"] + command

            subprocess.run(command, cwd=BASE_DIR)

        except KeyboardInterrupt:
            print("\nReturning to menu.")

    else:
        print("Invalid choice. Please try again.")
