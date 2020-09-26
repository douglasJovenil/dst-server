from os import system

def main():
    system('sudo apt-get update -y')
    system('sudo apt-get upgrade -y')
    system('sudo apt-get autoremove -y')

    system('sudo apt-get install apt-transport-https ca-certificates curl gnupg2 software-properties-common -y')
    system('curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -')
    system('sudo apt-key fingerprint 0EBFCD88')
    system('sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable"')
    system('sudo apt-get update -y')
    system('sudo apt-get install docker-ce docker-ce-cli containerd.io -y')

    system('sudo curl -L "https://github.com/docker/compose/releases/download/1.25.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose')
    system('sudo chmod +x /usr/local/bin/docker-compose')
    system('sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose')
    # system('cd ~/dst_server')
    # system('sudo docker-compose up -d')


if __name__ == '__main__':
    main()
