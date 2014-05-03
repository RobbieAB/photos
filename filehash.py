#!/usr/bin/python3.3

import hashlib

def sha256sum(filename):
    sha = hashlib.sha256()
    with open(filename, mode='rb') as f:
        while True:
            buf=f.read(4096)
            if not buf:
                break
            sha.update(buf)
    return sha.hexdigest()

