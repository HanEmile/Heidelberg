#!/bin/bash
folder=$1
user=$(whoami)
host=cosmo5
mkdir -p ./data/${folder}
echo "copying data..."
scp hanemile@cosmo5.ita.uni-heidelberg.de:~/github/Heidelberg/clean/data/kang.ita* ./data/${folder}
echo "cleaning up..."
ssh ${user}@${host}.ita.uni-heidelberg.de > /dev/null 2> /dev/null <<EOF
rm -r ~/github/Heidelberg/clean/data/kang.ita*
EOF