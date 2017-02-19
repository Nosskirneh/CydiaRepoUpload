# CydiaRepoUpload

> Python script to easily upload tweaks (.deb files) to a repo

## Installation
1.&nbsp;&nbsp;&nbsp;&nbsp; Install Python.

2.&nbsp;&nbsp;&nbsp;&nbsp; Install pip by running [this file](https://bootstrap.pypa.io/get-pip.py).

3.&nbsp;&nbsp;&nbsp;&nbsp; Run `pip install paramiko`.

4.&nbsp;&nbsp;&nbsp;&nbsp; Add your local id_rsa.pub to the authorized_keys on the remote machine to be able to login without password. Tip: use [ssh-copy-id](http://linux.die.net/man/1/ssh-copy-id).

5.&nbsp;&nbsp;&nbsp;&nbsp; Add the bin folder to your path.

6.&nbsp;&nbsp;&nbsp;&nbsp; Place a file named `update.sh` on the repo with this content:
```
# Delete old
rm -r Packages.bz2

# Generate new
dpkg-scanpackages -m . /dev/null >Packages
bzip2 Packages
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; and make it executable with `chmod +x update.sh`.

## Usage
Run this script when you're in a tweak directory created by theos to upload the most recent .deb file and update the repo.
