echo "host welcome.ita.uni-heidelberg.de" > ~/.ssh/config
echo "   User ttugendhat" >> ~/.ssh/config
echo "Host *.ita.uni-heidelberg.de" >> ~/.ssh/config 
echo "   ProxyCommand ssh -q -a ttugendhat@welcome-ita.zah.uni-heidelberg.de nc %h %p" >> >> ~/.ssh/config 
