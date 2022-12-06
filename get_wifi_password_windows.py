import subprocess
import re

value = input("Would you like to view saved profiles (y/n): ")
value = value.lower()
if value == 'y':
    print("Getting saved profiles...")
    profiles = subprocess.run('netsh wlan show profiles', shell=True)
    print(profiles)
else:
    print("Now exiting...")
profile_name = input("Enter a 'profile name' to view details about a profile: ")
profile_name = str(profile_name)
output1 = subprocess.run(f"netsh wlan show profiles name=\"{profile_name}\"", shell=True, capture_output=True)
print(output1.stdout.decode())
get_password = input("\nDo you wish to see the password (y/n): ")
if get_password == 'y':
    output2 = subprocess.run(f"netsh wlan show profiles name=\"{profile_name}\" key=clear", shell=True, capture_output=True)
    password = output2.stdout.decode()
    #print(password)
    pattern = re.compile(r'(Key+.+)')
    m = pattern.search(password)
    print(m[1])
else:
    print("Now exiting the program...")
    
get_input = input("Press Enter to quit: ")
