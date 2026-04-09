keywords = ["password", "api_key", "token"]

file = open("config.txt", "r")

print("Scanning for secrets...\n")

for line in file:
    for key in keywords:
        if key.lower() in line.lower():
            print("Potential Secret Found:", line.strip())

file.close()