#!/usr/bin/env

for file in "$@"

do 
  md5 -r $file >> manifest-md5.txt
  echo $file 
done