#!/bin/bash

#hosts: structure03 cosmo35 planet04 cosmo33 cosmo02

user=$(whoami)
thisfolder=$(pwd)

for host in $@; do
    cd $thisfolder
    ssh ${user}@${host}.ita.uni-heidelberg.de > /dev/null 2> /dev/null <<EOF
cd $thisfolder
for i in 1 2 3 4; do
nohup python3 gen.py > log 2> log.err < /dev/null &
done
EOF
    echo "submitted on ${host}!"
done
