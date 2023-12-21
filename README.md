# Introduction
Hello there! If you see this, this is just a repository for me to upload my notes and python_learning bash files for learning the basics. I'll get to the intermediate level sometime soon but feel free to checkout my other projects 😎

[Repositories](https://github.com/DeonteHorton?tab=repositories)

## Docker installation
If you have docker downloaded and want to run the files I have in this repository. You'll have to run these commands to have it up to play around with

### Pull the docker image

`docker pull python`

### Create the docker container using the docker compose yaml file

`docker compose up -d`

### SSH / Entering the python container through exec

`docker exec -it python_learning bash`

### After that, you can execute the files by using the command below

`python [FILE_NAME]`

## If you don't have docker installed
You can download python from their [website](https://www.python.org/downloads/) based on your OS, following the steps after downloading the executable. Once your done, you can run this command to execute the python files.
<br/>
`python [FILE_NAME]`