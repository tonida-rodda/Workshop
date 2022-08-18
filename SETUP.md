# Setup

## 1. Python

In this workshop, we will create an HTTP REST server using Python.
First of all, you have make sure you have [**python 3** or higher installed](https://phoenixnap.com/kb/how-to-install-python-3-ubuntu).

If you have the right version installed, you should have something similar:
```sh
python --version
> python --version Python 3.8.10 # OK
```

## 3. Flask

we will need to install the backewnd framework.
First of all, you have make sure you have [**Flask**](https://flask.palletsprojects.com/en/2.2.x/installation/).

If you have the right version installed, you should have something similar:
```sh
flask --version
> flask --version 
Python 3.8.10
Flask 1.1.1
Werkzeug 0.16.1 # OK
```
## 2. Mysql

we will need to install a data base for managing our data.
First of all, you have make sure you have [**mysql**](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04).

If you have the right version installed, you should have something similar:
```sh
mysql --version
> mysql --version mysql  Ver 8.0.30-0ubuntu0.20.04.2 for Linux on x86_64 ((Ubuntu)) # OK
```

## 2. Postman, Hoppscotch, Curl

We will be using `postman` to test out our routes, but you can also use `Hoppscotch`, `curl`, or whatever other tool you want for your tests since they will be personal, but we highly recommend `postman` as we will explain you how to use it.

- [Postman](https://www.postman.com/downloads/)
- [Hoppscotch](https://hoppscotch.io/)
- [Curl](https://curl.haxx.se/) (often already installed on your computer)


## 3. Launching the server

Once everything is installed, you have to download the workshop files **[here](https://downgit.github.io/#/home?url=https://github.com/PoCInnovation/Workshops/tree/master/software/02.Go/src)**.
Then, go in the [src](./src) folder and execute:
```sh
go run ./
# to simply launch the server
```
or
```sh
go build ./ && ./poc-workshop-go
# to compile a binary and run it
```

**If you have `Server runs on http://localhost:8080`, you've finished the setup and you can go for the exercises**

[Go back to the exercises](./README.md)