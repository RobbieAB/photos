#!/usr/bin/python3.4

# Pillaged from http://stackoverflow.com/questions/7829499

# The contents of this file are under the CC-BY-SA license covering StackOverflow answers.

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

if __name__ == "__main__" :
    print(sha256sum(__file__))
