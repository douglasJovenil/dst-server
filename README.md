# Don't Starve Together Server

This repository provides a CLI to build and manage a Don't Starve Together server based on [docker-dontstarvetogether](https://github.com/fairplay-zone/docker-dontstarvetogether) container.

## 💻 Project

#### CLI

![CLI](./docs/images/00_cli.png)

## 🚀 Technologies

This project was developed with the following technologies:

<img align="left" alt="Python" width="26px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png" /> Python3.7+

<img align="left" alt="Docker" width="26px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/docker/docker.png" /> Docker

<img align="left" alt="Docker-compose" width="26px" src="https://cdn.rancher.com/wp-content/uploads/2016/04/20182217/compose.png"/> Docker Compose

## 🏃 Usage

Before installing you need to configure your world

### Setting World

First thing you need to get is your server **TOKEN**, just follow the steps below:

Open DST, and click **Account** on the initial menu
![Klei page](./docs/images/01_dst_pagina_inicial.png)

A klei page will open, then click on **games**
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

Open the files [underworld](./container/underworld.env) and [overworld](./container/overworld.env), and paste your **TOKEN** on both files, as follows:

![Saving token on overworld](./docs/images/07_saving_token_on_overworld.png)

![Saving token on underworld](./docs/images/08_saving_token_on_underworld.png)

Besides that you can change other fields, like:

- **NAME**: this is the name that will appear on the server list inside the DST
- **DESCRIPTION**: your server's description
- **GAME_MODE**: can be `survival`, `wilderness` or `endless`
- **PAUSE_WHEN_EMPTY**: when set to `true` the world will stop if there's no one on server. You can set it to `false` if you like to let days running.
- **INTENTION**: can be `social`, `cooperative`, `competitive` or `madness`

Leave the rest of the fields with the default values. To **add more configurations** check out this [documentation page](https://github.com/fairplay-zone/docker-dontstarvetogether/blob/develop/docs/configuration.md) for the available options.

Now you have to configure the options of your world, the easiest wat to do it is create a **local** world as you like:

![Setup world](./docs/images/22_setup_world.png)

Then open the data files of this world:

![Open data](./docs/images/23_open_data.png)

Navigate to **WOLRD_ID/Cluster_1/Master** and find **leveldataoverride.lua**, this file contain all configuration of your overworld, just open it, copy all content and past it on [docker-compose.yml](container/docker-compose.yml), just have shore to put it on field **LEVELDATA_OVERRIDES** relative to overworld.

![Setup overworld](./docs/images/24_copy_and_paste_overworld.png)

You have to do the same thing to underworld, so navigate to **WOLRD_ID/Cluster_1/Caves** and do the same process:

![Setup underworld](./docs/images/25_copy_and_paste_underworld.png)

With all done, you can jump to [Installing CLI and Building Server](#installing-cli-and-building-server) if you want a vanilla server.

## Adding mods

First you have to find your mod on the [Don't Starve Together workshop](https://steamcommunity.com/app/322330/workshop/), just open the link and choose a mod, in this case i will install **Simple Health Bar**. Put the mod name on the search box and once the mod appears just click it:

![Search mod](./docs/images/09_search_mod.png)

We will need the mod **id**, you can find it at URL of your browser

![Find mod id](./docs/images/10_find_mod_id.png)

With the mod id copied open the file [modoverrides.lua](./container/modoverrides.lua) and paste it as follows:

```lua
return {
	['workshop-MOD_ID_THAT_YOU_COPIED'] = { enabled=true },
}
```

![Add mod](./docs/images/11_add_mod.png)

Open the file [docker-compose.yml](./container/docker-compose.yml) and put all mods that you have installed on the field `MODS`, you need to set this field to both **overworld** and **underworld** sections

![Add mod docker compose overworld](./docs/images/12_add_mod_docker_compose_overworld.png)

![Add mod docker compose underworld](./docs/images/13_add_mod_docker_compose_underworld.png)

You can have as many mods you want.

## Setting up a mod

If you want to tweak some configuration on your mod, follow this simple guide:

Open **DST** on **Steam** and click on button **workshop**
![Open workshop on Steam](./docs/images/14_open_workshop_on_steam.png)

Serach the mod that yout want to configure and open it
![Search and open mod on Steam](./docs/images/15_search_and_open_mod_steam.png)

Click on **Subscribe**
![Subscribe to mod](./docs/images/16_subscribe_to_mod.png)

Right click and then **Copy Page URL**
![Copy page URL](./docs/images/17_copy_page_URL.png)

Open any text editor and paste the URL and identify the mod id
![Paste URL and get ID](./docs/images/18_paste_url_get_id.png)

Now you will have to find this mod on your computer, normally they are installed on `STEAM_FOLDER/steamapps/common/Don't Starve Together/mods`, just open the folder with the ID that you identified on previous step
![Find folder](./docs/images/19_find_folder.png)

Open the file modinfo.lua
![Open modinfo](./docs/images/20_open_modinfo.png)

This file have all mod options, just search for what you want to modify and put your modifications on the file [modoverrides.lua](./container/modoverrides.lua)
![Modinfo](./docs/images/21_modinfo.png)

## Installing CLI and Building Server

```bash
$ sudo add-apt-repository ppa:deadsnakes/ppa -y
$ sudo apt-get update -y
$ sudo apt-get install python3.8 -y
$ cd dst-server/src
$ sudo python3.8 main.py --install
$ exec bash
```

## Running Server

```
$ dst --start
```

## CLI Options

- **install**: installs all dependencias and configure the server
- **start**: starts the container
- **stop**: stops the container
- **delete**: deletes the server (_tip: make a backup before using this option_)
- **overworld**: opens a bash shell on overworld container
- **underworld**: opens a bash shell on underworld container
- **containers**: shows a list of all running containers
- **images**: shows a list of all images installed
