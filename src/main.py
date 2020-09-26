from os import system, getcwd, chdir, popen
import argparse
from sys import argv


def main():
  root_path = f'{getcwd()}/{__file__}'.split('src')[0]

  parser = argparse.ArgumentParser('Ferramenta para auxiliar na comunicação com o Raspberry')
  parser.add_argument('--install', help='Configure the container', action='store_true')
  parser.add_argument('--start', help='Start the server', action='store_true')
  parser.add_argument('--stop', help='Stop the server', action='store_true')
  parser.add_argument('--delete', help='Delete the server', action='store_true')
  parser.add_argument('--overworld', help='Open the overworld container', action='store_true')
  parser.add_argument('--underworld', help='Open the underworld container', action='store_true')
  parser.add_argument('--list', help='List all containers', action='store_true')

  args = parser.parse_args()

  if (len(argv) <= 1):
    parser.print_help()
    exit(0)

  if (args.install):
    system('sudo apt-get update -y')
    system('sudo apt-get upgrade -y')
    system('sudo apt-get autoremove -y')

    system('sudo apt-get screen install docker.io apt-transport-https ca-certificates curl gnupg2 software-properties-common -y')
    system('curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -')
    system('sudo apt-key fingerprint 0EBFCD88')
    system('sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable"')
    system('sudo apt-get update -y')
    system('sudo apt-get install docker-ce docker-ce-cli containerd.io -y')

    system('sudo curl -L "https://github.com/docker/compose/releases/download/1.25.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose')
    system('sudo chmod +x /usr/local/bin/docker-compose')
    system('sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose')

    print('Success configuring server')

  if (args.start):
    chdir(f'{root_path}/container')
    system('sudo docker-compose up -d')

  if (args.stop):
    containers = getContainers()
    for container in containers:
      system(f'sudo docker stop {container}')
  
  if (args.delete):
    system('sudo docker system prune')
  
  if (args.overworld):
    overworld = getContainers()[0]
    system(f'sudo docker exec -it {overworld} /bin/bash')

  if (args.overworld):
    underworld = getContainers()[1]
    system(f'sudo docker exec -it {underworld} /bin/bash')

  if (args.list):
    system('sudo docker ps')

def getContainers():
  return popen('sudo docker ps -q').read().split('\n')[:-1]


if __name__ == '__main__':
  main()
