import time

def fetch_code():
    print("Fetching code from repository...")
    time.sleep(1)

def build():
    print("Building application...")
    time.sleep(1)
    return True

def test():
    print("Running tests...")
    time.sleep(1)
    return True

def deploy():
    print("Deploying application...")
    time.sleep(1)
    return True

print("Starting DevOps Pipeline...\n")

fetch_code()

if build():
    print("Build Successful\n")
    
    if test():
        print("All Tests Passed\n")
        
        if deploy():
            print("Deployment Successful\n")
            print("FINAL STATUS: PIPELINE COMPLETED")
        else:
            print("Deployment Failed")
    else:
        print("Tests Failed")
else:
    print("Build Failed")