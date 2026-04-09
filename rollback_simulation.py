import time

def deploy():
    print("Deploying new version...")
    time.sleep(1)
    return False  

def rollback():
    print("Rolling back to previous stable version...")
    time.sleep(1)
    print("Rollback Successful")

print("Starting Deployment...\n")

if deploy():
    print("Deployment Successful")
else:
    print("Deployment Failed\n")
    rollback()
    print("\nFINAL STATUS: SYSTEM RESTORED")