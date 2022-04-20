#!/bin/sh
cd $(mktemp -d)

python3 -m xenoslib.onedrive login $*

if [ "" == "$URL" ]
then
    python3 -m xenoslib.onedrive download "/media/upload/conf/task.sh"
    sh task.sh
else youtube-dl "$URL" 
fi

ls -lh

python3 -m xenoslib.onedrive upload . --folder "/media/upload"
python3 -m xenoslib.onedrive logout
