import time

def create_vm():
    print("Creating Virtual Machine...")
    time.sleep(1)
    print("VM Created Successfully\n")

def create_storage():
    print("Setting up Storage...")
    time.sleep(1)
    print("Storage Configured\n")

def create_network():
    print("Configuring Network...")
    time.sleep(1)
    print("Network Setup Completed\n")

print("Starting Cloud Provisioning...\n")

create_network()
create_vm()
create_storage()

print("FINAL STATUS: CLOUD INFRASTRUCTURE READY")