#!/usr/bin/python3.3

import hashlib

imgdir="/home/robert/Pictures/photos/"

def sha256sum(filename):
    sha = hashlib.sha256()
    with open(filename, mode='rb') as f:
        while True:
            buf=f.read(4096)
            if not buf:
                break
            sha.update(buf)
    return sha.hexdigest()

print(sha256sum("/home/photos/CARD01/IMG_3268.JPG"))

