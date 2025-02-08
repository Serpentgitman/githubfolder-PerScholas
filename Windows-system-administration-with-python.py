import os

# Use 'dir' command for Windows
os.system("dir")

import subprocess

# Use 'dir' command for Windows with subprocess.run() and specify a directory
subprocess.run(["dir", "/B"], shell=True)

# Gather system information using 'systeminfo' command
command = "systeminfo"
print(f'Gathering system information with command: {command}')
subprocess.run([command], shell=True)

# Gather active process information using 'tasklist' command
command = "tasklist"
print(f'Gathering active process information with command: {command}')
subprocess.run([command], shell=True)

# Check disk space using 'wmic logicaldisk' command
command = "wmic"
commandArgument = "logicaldisk get size,freespace,caption"
print(f'Checking disk space with command: {command} {commandArgument}')
subprocess.run([command, commandArgument], shell=True)

# Get network configuration using 'ipconfig' command
command = "ipconfig"
print(f'Getting network configuration with command: {command}')
subprocess.run([command], shell=True)

# List installed programs using 'wmic product get name' command
command = "wmic"
commandArgument = "product get name"
print(f'Listing installed programs with command: {command} {commandArgument}')
subprocess.run([command, commandArgument], shell=True)

# Get system boot time using 'systeminfo' command
command = "systeminfo"
print(f'Getting system boot time with command: {command}')
subprocess.run([command], shell=True)

# List user accounts using 'net user' command
command = "net"
commandArgument = "user"
print(f'Listing user accounts with command: {command} {commandArgument}')
subprocess.run([command, commandArgument], shell=True)

# Check system uptime using 'net stats workstation' command
command = "net"
commandArgument = "stats workstation"
print(f'Checking system uptime with command: {command} {commandArgument}')
subprocess.run([command, commandArgument], shell=True)

# Get firewall status using 'netsh advfirewall show allprofiles' command
command = "netsh"
commandArgument = "advfirewall show allprofiles"
print(f'Getting firewall status with command: {command} {commandArgument}')
subprocess.run([command, commandArgument], shell=True)

# List running services using 'net start' command
command = "net"
commandArgument = "start"
print(f'Listing running services with command: {command} {commandArgument}')
subprocess.run([command, commandArgument], shell=True)

# Get event logs using 'wevtutil qe System /c:10 /f:text' command
command = "wevtutil"
commandArgument = "qe System /c:10 /f:text"
print(f'Getting event logs with command: {command} {commandArgument}')
subprocess.run([command, commandArgument], shell=True)