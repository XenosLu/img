#!/bin/sh
cd $(mktemp -d)

python3 -m xenoslib.onedrive login $*

taskpath="/media/upload/bin/task.sh"
task=$(basename $taskpath)

if [ "" == "$URL" ]
then
    python3 -m xenoslib.onedrive download "$taskpath"
    sh $task
    rm $task
else youtube-dl "$URL"
fi

ls -lh

python3 -m xenoslib.onedrive login $*
python3 -m xenoslib.onedrive upload . --folder "/media/upload"
python3 -m xenoslib.onedrive logout
