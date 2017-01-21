#!/bin/bash
if [ $# -ne 1 ];then
    echo "Usage: sh $0 {you commit message}";
    exit -1
fi
echo 'Notice: this script can be only used at commit TRACKED file!! '

# to clean *.pyc file
sh -x rmpyc

# to get diff files
arr=($(git diff --name-only))
len=${#arr[@]}
if [ $len -le 0 ];then
    echo 'No diff.'
    exit -1
fi

echo "The diff files num is: ${len}, there are as follows:"
echo ${arr[@]}

#begin to commit and push to git
git add -u .
git commit -m $1
wait
git push origin master

echo 'Commit Done.'
