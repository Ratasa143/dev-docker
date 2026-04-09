import argparse
import psutil

parser = argparse.ArgumentParser()

parser.add_argument("--cpu", action="store_true")
parser.add_argument("--memory", action="store_true")

args = parser.parse_args()

if args.cpu:
    print("CPU Usage:", psutil.cpu_percent(interval=1), "%")

if args.memory:
    print("Memory Usage:", psutil.virtual_memory().percent, "%")

if not args.cpu and not args.memory:
    print("Please provide an argument: --cpu or --memory")