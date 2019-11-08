# Trabajo Practico

### Technologies:
    - SQLite ( sqlite tools for windows )
    - Python ( Anaconda for windows systems)

## Extra Technology:
    - Docker ( easy_to_build ) image to upload to the cloud or on-promise docker service.

### Libraries:
    - Bottle
    - Pony.ORM

# How to use:
Ensure you have " python3 " installed on your system and execute the following commands to deploy database with relathionships and populate data on Vouchers table.

anaconda for windows systems:
https://www.anaconda.com/distribution/

and sqltools for windows:
https://www.sqlitetutorial.net/download-install-sqlite/

# Docker image #####################################################
Please, get Docker installed on you laptop/desktop or create an account in some cloud service ( Google Cloud / Amazon or IBM Cloud ) to use it.

For Mac:
https://docs.docker.com/docker-for-mac/install

Youtuve Video:
https://www.youtube.com/watch?v=O4Yro0VN5Ds

For Windows:
https://hub.docker.com/editions/community/docker-ce-desktop-windows

For Linux ( RHEL / Centos or Fedora Core ):
#yum install docker or #dnf install docker

For Ubuntu:
#apt-get install docker

####################################################################

# For linux or Mac:

# Clone Repository

```sh
$ git clone URL
```

# Project Directory
```sh 
cd <path>
``` 

# Install Deps
```sh
$ make deps
```

# Start the App
```sh
$ make start
```

# Populate Database
```sh
$ make populate
```

# Cleanup 
```sh
$ make clean
```

# For windows:

# Clone Repository

```sh
$ git clone URL
```

# Project Directory
```sh 
cd <path>
``` 

# Install Deps ( anaconda console )
```sh
$ conda install -c conda-forge bottle
$ conda install -c conda-forge pony
```

# Start the App ( powershell console or cmd )
```sh
$ python start
```

# Populate Database ( powershell console or cmd )
```sh
$ python populate
```

# Cleanup ( powershell console or cmd )
``` delete sqlite.db file
```

# Docker Image
``` 
git clone project
```

``` 
cd project
```

``` 
docker build -t "tcl_pereyra" .
```

``` 
docker run -p 8080:8080 -it tcl_pereyra
```

``` 
Go to firefox browser -> url:  http://localhost:8080/route's
```

# Default routes ->

<h3> http://localhost:8080/medic <br>
     http://localhost:8080/patient <br>
     http://localhost:8080/user <br>
     http://localhost:8080/useradd <br>
</h3>

/medic <- Medic personal information pre-loaded.

/patient <-Patient Assignation to Medic

/useradd <- User add/delete/modification

/Medic <- Agenda by Specific medic.

### Author: Javier E. Pereyra
