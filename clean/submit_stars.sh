#!/bash/bin
thisfolder=$(pwd)
#for host in {structure03 cosmo35 planet04 cosmo33 cosmo02}; do
#for host in {structure03 cosmo35 planet04 cosmo02}; do
for host in $@; do
    cd $thisfolder
    ssh hanemile@${host}.ita.uni-heidelberg.de > /dev/null<<EOF
cd $thisfolder
for i in 1 2 3 4; do
python3 gen.py&
done
EOF
    echo "submitted on ${host}!"
done
