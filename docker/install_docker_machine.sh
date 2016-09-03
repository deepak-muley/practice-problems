#https://github.com/docker/machine/releases
curl -L https://github.com/docker/machine/releases/download/v0.8.1/docker-machine-`uname -s`-`uname -m` > docker-machine
sudo mv docker-machine /usr/local/bin/docker-machine
chmod +x /usr/local/bin/docker-machine
docker-machine version
