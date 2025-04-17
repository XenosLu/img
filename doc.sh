#!/bin/bash

current=$(dirname "$0")
cd "$current" || exit

echo "# Images" > README.md

for dir in */; do
    dir=${dir%/}  # 移除末尾的/
    if [[ "$dir" == ".github" || "$dir" == ".git" ]]; then
        continue
    fi
    echo "- xenocider/img:$dir" >> README.md
    echo "- registry.cn-shanghai.aliyuncs.com/xenocider/img:$dir" >> README.md
done

sleep 3
