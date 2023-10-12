# Janneck Lehmann 12.10.2023
# Description: This file contains the functions to request the IPMI data from diffrent Servers
import os



def getData(serverModdell, username, password, ipaddress):
    # use The ipmitool to get the data from the server
    data = str()
    result = {}
    
    # get the command from the serverModdells dictionary
    command = serverModdells[serverModdell]["command"]
    # replace the placeholders with the given data
    command = command.replace("{username}", username)
    command = command.replace("{password}", password)
    command = command.replace("{ipaddress}", ipaddress)
    # execute the command
    data = os.popen(command).read()
    
    data = data.strip().split('\n')[1:]

    # Iteriere über jede Zeile und extrahiere Daten
    for line in data:
        parts = line.split('|')
        if len(parts) == 3:
            key = parts[0].strip()
            value = parts[1].strip()
            status = parts[2].strip()
            key = key.replace('|', '').strip()
            result[key] = {
                'Value': value,
                'Status': status
            }
    print(data)
    #return data
    
    
# Dictionary for the server models and the corresponding commands
serverModdells = {
    "dellPoweredgeR720": {
        "command": 'ipmitool -I lanplus -H {ipaddress} -U {username} -P {password} sdr',
        "description": 'Dell Poweredge R720'
    },
}

getData("dellPoweredgeR720","root","Potsdam1","192.69.69.42")