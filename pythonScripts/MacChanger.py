import sys # importing sys module to use sys.stdout.flush() function
import subprocess # importing subprocess module to use subprocess.call() function
import argparse # importing argparse module to use argparse.ArgumentParser() function
import random # importing random module to use random.choice() function
import time # importing time module to use time.sleep() function
import re # importing re module to use re.search() function
  
  

def get_arguments(): # function to get arguments from the user
    
    parser = argparse.ArgumentParser() # creating an object of ArgumentParser class
   
    parser.add_argument("-i", "--interface",
                dest="interface",
                help="Name of the interface. "
                "Type ifconfig for more details.") # adding arguments to the parser object
    options = parser.parse_args() # parsing the arguments
   
    if options.interface: # checking if the user has entered the interface name
        return options.interface # returning the interface name
    else:
        parser.error("[!] Invalid Syntax. "
                     "Use --help for more details.") # if the user has not entered the interface name, then print the error message and exit the program
  

def change_mac(interface, new_mac_address): # function to change the MAC address

    subprocess.call(["sudo", "ifconfig", interface,
                     "down"]) # calling the subprocess.call() function to execute the command
    subprocess.call(["sudo", "ifconfig", interface,
                     "hw", "ether", new_mac_address]) # calling the subprocess.call() function to execute the command and change the MAC address
    subprocess.call(["sudo", "ifconfig", interface,
                     "up"]) # calling the subprocess.call() function to execute the command and bring the interface up
  

def get_random_mac_address(): # function to generate a random MAC address
    characters = "0123456789abcdef" # characters to be used in the MAC address
    random_mac_address = "00" # first two characters of the MAC address
    for i in range(5): # loop to generate the remaining 10 characters of the MAC address
        random_mac_address += ":" + \
                        random.choice(characters) \
                        + random.choice(characters) # appending the random characters to the random_mac_address variable
    return random_mac_address # returning the random MAC address
  

def get_current_mac(interface): # function to get the current MAC address
    output = subprocess.check_output(["ifconfig",
                                      interface]) # calling the subprocess.check_output() function to execute the command and get the output
    return re.search("\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",
                  str(output)).group(0) # returning the current MAC address
  

if __name__ == "__main__": # main function
    print("[* Welcome to MAC ADDRESS Changer *]") # printing the welcome message
    print("[*] Press CTRL-C to QUIT") # printing the message to quit the program using CTRL-C
    
    TIME_TO_WAIT = 60 # time to wait before changing the MAC address
    interface = get_arguments() # getting the interface name from the user
    current_mac = get_current_mac(interface) # getting the current MAC address
    try: # try block to handle the KeyboardInterrupt exception
        while True: # infinite loop
            random_mac = get_random_mac_address() # getting the random MAC address
            change_mac(interface, random_mac) # changing the MAC address
            new_mac_summary = subprocess.check_output( 
                ["ifconfig", interface]) # getting the output of ifconfig command
            if random_mac in str(new_mac_summary): # checking if the MAC address has been changed
                print("\r[*] MAC Address Changed to",
                      random_mac,
                      end=" ") # printing the message if the MAC address has been changed successfully
                sys.stdout.flush() # flushing the output to the screen
          
            time.sleep(TIME_TO_WAIT) # waiting for the specified time
  
    except KeyboardInterrupt:  # handling the KeyboardInterrupt exception
        change_mac(interface, current_mac) # changing the MAC address to the original MAC address
        print("\n[+] Quitting Program...") # printing the message to quit the program