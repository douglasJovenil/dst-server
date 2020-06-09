from os import system

def main():
    # underworld -> 1b4fa9fb99fe        
    # overworl -> 6755a22390a4        
    system('sudo apt-get upgrade -y')
    system('sudo apt-get autoremove -y')
    system('sudo apt-get install docker.io -y')  
    system('sudo curl -L "https://github.com/docker/compose/releases/download/1.25.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose')
    system('sudo chmod +x /usr/local/bin/docker-compose')
    system('sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose')

if __name__ == '__main__':
    main()
