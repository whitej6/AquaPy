
echo "#############################################"
echo "# Update & Upgrade OS                       #"
echo "#############################################"

sudo apt-get -y update
sudo apt-get -y upgrade

echo "#############################################"
echo "# Installing Docker                         #"
echo "#############################################"

curl -fsSL https://get.docker.com -o /tmp/get-docker.sh
sudo sh /tmp/get-docker.sh
sudo usermod -aG docker pi
sudo rm -f /tmp/get-docker.sh

echo "#############################################"
echo "# Installing docker-compose                 #"
echo "#############################################"

sudo apt-get install -y libffi-dev libssl-dev
sudo pip3 install PyNaCl==1.2.1
sudo pip3 install docker-compose==1.26.0

echo "#############################################"
echo "# Building Docker Images                    #"
echo "#############################################"

sudo docker-compose build
sudo docker-compose pull

echo "#############################################"
echo "# Starting AquaPy                           #"
echo "#############################################"

sudo docker-compose up -d
