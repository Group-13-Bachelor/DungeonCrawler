# DungeonCrawler
Dungeon crawler scenario in our bachelor project

# Setup
This section explains how to setup a development enviroment for this project

## Virtual environment
1. Clone repository: `git clone git@github.com:Group-13-Bachelor/DungeonCrawler.git dungeonCrawler`
2. Enter the repository: `cd dungeonCrawler`
3. Create virutal environment: `python venv ./.venv`
4. Activate virutal environment:
    - Windows: `.venv\Scripts\activate.bat`
    - Linux: `source .venv/bin/activate`

## Install package
1. Stand in project root directory: `cd <path to directory>/dungeonCrawler/`
2. Install project packages: `pip install -e .`
    - This also installs packages in `requirements.txt`
3. Install developer tools: `pip install -r .\requirements_dev.txt`

# TODO
Fix tox and flake8

# 

If you add another package to requirements.txt reinstall with pip
If you want to create another package create a folder in './src/' and add the package to the setup.cfg packages = 