import time
import datetime

host_path = "C:\Windows\System32\drivers\etc\hosts" # path to the hosts file in Windows OS
redirect = "127.0.0.1" # redirecting the website to localhost
website_list = ["www.facebook.com", "facebook.com", "www.youtube.com", "youtube.com"] # list of websites to be blocked
startDate = datetime.datetime(2020, 5, 1) # start date of the block
endDate = datetime.datetime(2020, 5, 31) # end date of the block
todayDate = datetime.datetime.now() # current date
while True:
    if startDate <= todayDate <= endDate: # checking if the current date is in between the start date and end date
        with open(host_path, "r+") as file: # opening the hosts file in read and write mode
            content = file.read() # reading the content of the file
            for website in website_list: # looping through the list of websites
                if website in content: # checking if the website is already blocked
                    pass # if the website is already blocked, then do nothing
                else: # if the website is not blocked
                    file.write(redirect + " " + website + "\n") # writing the website to the hosts file
        print("[*] Websites Blocked Successfully") # printing the message if the websites are blocked successfully
        break # breaking the loop
    else: # if the end date is less than the current date 
        with open(host_path, "r+") as file: # opening the hosts file in read and write mode
            content = file.readlines() # reading the content of the file
            file.seek(0) # setting the cursor to the beginning of the file
            for line in content: # looping through the content of the file
                if not any(website in line for website in website_list): # checking if the website is not blocked
                    file.write(line) # writing the line to the file
            file.truncate() # truncating the file
        print("[*] Websites Unblocked Successfully") # printing the message if the websites are unblocked successfully
        break # breaking the loop
    time.sleep(5) # waiting for 5 seconds before checking the date again
