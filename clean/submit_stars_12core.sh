#!/bin/bash

#hosts: structure03 cosmo35 planet04 cosmo02 cosmo25

user=$(whoami)
thisfolder=$(pwd)

for host in $@; do
    cd $thisfolder
    ssh ${user}@${host}.ita.uni-heidelberg.de > /dev/null 2> /dev/null <<EOF
cd $thisfolder
for i in 1 2 3 4 5 6 7 8 9 10 11 12; do
nohup python3 gen.py > log 2> log.err < /dev/null &
done
EOF
    echo "submitted on ${host}!"
done
