import psutil

print("System Health Monitoring\n")

cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent

print("CPU Usage:", cpu, "%")
print("Memory Usage:", memory, "%")
print("Disk Usage:", disk, "%")

if cpu > 80:
    print("Warning: High CPU Usage")

if memory > 80:
    print("Warning: High Memory Usage")

if disk > 80:
    print("Warning: Low Disk Space")