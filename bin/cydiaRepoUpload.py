#!/usr/bin/env python

from time import sleep
import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from config import *

import fnmatch
import paramiko

# Open control file
if os.path.exists('control'):
    with open('control', 'rb') as f:
        try:
            for line in f:
                if line.startswith('Version:'):
                    # Get version from file
                    version = line.split()[1]
                    print("The version of the compiled code is: \n" + version + "\n")

        except:
            print("Couldn't read control file!")
else:
    print("Found no control file!")


# Print pwd
print("Path at terminal when executing this file: \n" + os.getcwd() + "\n")


# Log
paramiko.util.log_to_file(log_file)
print("Logging to file: \n" + os.getcwd() + "/" + log_file + "\n")


# Get most recent .deb file
matches = []
for root, dirnames, filenames in os.walk(os.getcwd()):
    for filename in fnmatch.filter(filenames, '*.deb'):
        matches.append(os.path.join(root, filename))

newest = max(matches, key=os.path.getmtime)

print("Most recent .deb file is: \n" + newest + "\n")


# SSH
print("Setting up SSH connection...")
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    ssh.connect(repo, username=user, key_filename=os.path.expanduser('~/.ssh/id_rsa'))
except:
    print("Server seems to be offline! Exiting...")
    sys.exit()

sftp = ssh.open_sftp()


# Copy .deb file
print("Copying .deb file...")
sftp.put(newest, remote_path + "/debs/" + filename)


# Update repo
print("Updating repo...\n\n")
print("Output from dpkg-scanpackages:")
print("---------------------------------------------------")
#ssh.exec_command('cd' + remote_path + '; touch "hej.txt"')

stdin_, stdout_, stderr_ = ssh.exec_command('cd ' + remote_path + '; ' + './update.sh', get_pty=True)
stdout_.channel.recv_exit_status();
lines = stdout_.readlines();
for line in lines:
    print line;
print("---------------------------------------------------\n\n")

ssh.close()
print("Closed SSH session.")
