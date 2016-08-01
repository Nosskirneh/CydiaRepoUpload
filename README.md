# CydiaRepoUpload

> Python script to easily upload tweaks (.deb files) to a repo

## Installation
1. Put the script somewhere in your path.

2. Install Python.

3. Install pip by running [this file](https://bootstrap.pypa.io/get-pip.py).

4. Run `pip install paramiko`.

5. Add your local id_rsa.pub to the authorized_keys on the remote machine to be able to login without password. Tip: use [ssh-copy-id](http://linux.die.net/man/1/ssh-copy-id).

## Usage
1. Run this script when you're in a tweak directory created by theos.