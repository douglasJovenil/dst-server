# Don't Starve Together Server

This repository provides a CLI to build and manage a docker server based on [docker-dontstarvetogether](https://github.com/fairplay-zone/docker-dontstarvetogether)

## 💻 Project

#### CLI

![CLI](./docs/images/00_cli.png)

## 🚀 Technologies

This project was developed with the following technologies:

<img align="left" alt="Python" width="26px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png" /> Python3.6+

<img align="left" alt="Docker" width="26px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/docker/docker.png" /> Docker

<img align="left" alt="Docker-compose" width="26px" src="https://cdn.rancher.com/wp-content/uploads/2016/04/20182217/compose.png"/> Docker Compose

## 🏃 Usage

Before install you have to configure your world

### Setting World

First thing you need to get is your server **TOKEN**, just follow the steps bellow:

Open your DST Game, on initial menu click on **Account**
![Klei page](./docs/images/01_dst_pagina_inicial.png)

After you clicked **Account** a klei page will open, on this page click on **games**
![Klei account](./docs/images/02_klei_conta.png)

Click on **Game Servers**
![Klei game servers](./docs/images/03_klei_game_servers.png)

This page will show all your servers, to add a new one just click on **ADD NEW SERVER**
![Klei add new server](./docs/images/04_klei_add_new_server.png)

A text input field will appear, put any name you want to identify your server, in this case I choose **NAME OF MY CLUSTER**, then click on **ADD NEW SERVER**
![Klei adding new](./docs/images/05_klei_adding_new_server.png)

Your server will be added and now you get access to your **TOKEN**
![Klei new server added](./docs/images/06_klei_new_server_added.png)

Clone this repository with:
```bash
$ git clone https://github.com/douglasJovenil/dst-server
```

Open the files [underworld](./container/underworld.env) and [overworld](./container/overworld.env), copy the generated **TOKEN** and past it on field **TOKEN** on both files, as follows:

![Saving token on overworld](./docs/images/07_saving_token_on_overworld.png)

![Saving token on underworld](./docs/images/08_saving_token_on_underworld.png)

Besides that you can change other fields, like:

- **NAME**: this name will appear on server list inside the DST
- **DESCRIPTION**: description that will appear on your server
- **GAME_MODE**: can be _survival_, _wilderness_ or _endless_
- **PAUSE_WHEN_EMPTY**: when is set to **true** the world will stop if there's no one on server. You can set to **false** if you like to let days running
- **INTENTION**: can be _social_, _cooperative_, _competitive_ or _madness_

The rest of the fields leave with the default values. To **add more configurations** you can find on this [documentation](https://github.com/fairplay-zone/docker-dontstarvetogether/blob/develop/docs/configuration.md) what are the available options

## Adding mods

First you have to find your mod on [Don't Starve Together workshop](https://steamcommunity.com/app/322330/workshop/), just open the link and choose a mod, in this case i will install **Simple Health Bar**. Put the mod name on search box and once the mod appears just click it

![Search mod](./docs/images/09_search_mod.png)

We will need the mod **id**, you can find it at URL of your navigator

![Find mod id](./docs/images/10_find_mod_id.png)

With the mod id copied open the file [modoverrides.lua](./container/modoverrides.lua) and past it as follows:

```lua
return {
	['workshop-MOD_ID_THAT_YOU_COPIED'] = { enabled=true },
}
```

![Add mod](./docs/images/11_add_mod.png)

Open the file [docker-compose.yml](./container/docker-compose.yml) and put all mods that you have installed on field **MODS**, you have set this field to **overworld** and **underworld** configuration

![Add mod docker compose overworld](./docs/images/12_add_mod_docker_compose_overworld.png)

![Add mod docker compose underworld](./docs/images/13_add_mod_docker_compose_underworld.png)

You can have as many mods you want.

## Setting up a mod

If you want to tweek some configuraiton of your mod, you can follow this simple guide:

Open **DST** on **Steam** and click on button **workshop**
![Open workshop on Steam](./docs/images/14_open_workshop_on_steam.png)

Serach the mod that yout want to setting up and open it
![Search and open mod on Steam](./docs/images/15_search_and_open_mod_steam.png)

Click on **Subscribe**
![Subscribe to mod](./docs/images/16_subscribe_to_mod.png)

Right click and then **Copy Page URL**
![Copy page URL](./docs/images/17_copy_page_URL.png)

Open any text editor and paste the URL, identify the mod id
![Paste URL and get ID](./docs/images/18_paste_url_get_id.png)

Now you will have to find this mod on your computer, normally they are installed on folder **STEAM_FOLDER/steamapps/common/Don't Starve Together/mods**, just open the folder with the ID that you identified on previous step
![Find folder](./docs/images/19_find_folder.png)

Inside the folder open the file modinfo.lua
![Open modinfo](./docs/images/20_open_modinfo.png)

This file have all options of mod, just look what you want to modify and put this modifications on file [modoverrides.lua](./container/modoverrides.lua)
![Modinfo](./docs/images/21_modinfo.png)

## Installing CLI and Building Server

```bash
$ cd src
$ sudo python main.py --install
$ exec bash
$ dst --install
```

## Running Server

```
$ dst --start
```

## CLI Options

- **install**: execute the installation of all dependencias and configure the server
- **start**: start the container
- **stop**: stop the container
- **delete**: delete the server (_tip: make a backup before use this option_)
- **overworld**: open a bash on overworld container
- **underworld**: open a bash on underworld container
- **containers**: show a list of all running containers
- **images**: show a list of all images installed
