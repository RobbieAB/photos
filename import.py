#!/usr/bin/python3.4

import os

import filehash

imgdir="/home/robert/Pictures/photos/"

srcdir="/home/photos/CARD02/"

imglist=os.listdir(srcdir)

for img in imglist :
    imgpath=os.path.join(srcdir,img)
    imghash=filehash.sha256sum(imgpath)
    print(imghash, imgpath)
    print(imghash[0:2], imghash[2:])
