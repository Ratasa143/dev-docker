file = open("app.log", "r")

print("Analyzing Logs...\n")

for line in file:
    if "ERROR" in line:
        print("Error Found:", line.strip())

file.close()