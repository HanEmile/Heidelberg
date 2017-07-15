echo "host welcome.ita.uni-heidelberg.de" > ~/.ssh/config
echo "   User hanemile" >> ~/.ssh/config
echo "Host *.ita.uni-heidelberg.de" >> ~/.ssh/config 
echo "   ProxyCommand ssh -q -a hanemile@welcome-ita.zah.uni-heidelberg.de nc %h %p" >> >> ~/.ssh/config 
