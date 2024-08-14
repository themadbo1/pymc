import sys
import subprocess
import os
import json
import socket

def get_ip():#finds the local IP address of your computer
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        s.connect(('10.254.254.254', 1)) #just to get the local ip address
        IP = s.getsockname()[0]#copypasta from stackoverflow
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

if ((os.path.isfile(os.getcwd() + "\\start.bat")) and (os.path.isfile(os.getcwd() + "\\server.jar"))):#checks if theres is an existing server
    print("Server.jar found in current directory.\nStarting server.")
    subprocess.run("start.bat",shell=True)
    sys.exit(0)




def link_haver(version):#loads the link of the server jar.
    with open("versions.json") as f:
        data=json.load(f)
        try:
            return data[version]
        except:
            print("The desired version is not available.")
            sys.exit(1)

    
def main():
    print("one time use after you close the server run the start.bat to start your server.")
    version = input("What version of Minecaft would you like to play in? (ex: 1.8.9):")
    link = link_haver(version)
    command = "curl -o server.jar "+ link #downloads server jar
    subprocess.run(command, shell=True)
    
    
    print("https://www.minecraft.net/en-us/eula")
    EULA=input("Do you accept MINECRAFT'S server agreement and EULA? (Y/N): ")
    if (EULA == "n") or (EULA == "N"):
        exit()
    elif (EULA=="Y") or (EULA=="y"):
        with open("eula.txt", "w") as file:
            file.write("eula=true")
        with open("server.properties", "w") as f:
            f.write(f"server-ip={get_ip()}")
    ram=int(input("how much RAM you would like to give to your server in gigabytes? (ex: 4): "))
    ram = ram*1024
    command = f"java -Xmx{ram}M -Xms{ram}M -jar server.jar nogui" 
    with open("start.bat","w") as start_bat:
        start_bat.write(command)
    subprocess.run(command, shell=True)





if __name__ == '__main__':
    main()