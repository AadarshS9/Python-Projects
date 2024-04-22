#Run the code below this on the terminal to show all the WiFi profiles saved on your computer
#netsh wlan show profile

#Run the code below this to show the password of a specific WiFi profile saved on your computer. Replace PROFILE-NAME with the name of the WiFi profile.
#netsh wlan show profile PROFILE-NAME key=clear

#Run the code below this to show all the WiFi passwords saved on your computer
import subprocess

command = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [i.split(":")[1][1:-1] for i in command if "All User Profile" in i]
for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        print("{:<30}| {:<}".format(i, results[0]))
    except IndexError:
        print("{:<30}| {:<}".format(i, ""))
input("")