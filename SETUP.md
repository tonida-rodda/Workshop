# Setup

## Python & Flask

In this workshop, we will create an HTTP REST server using Flask and interact with a MySQL database.
First of all, you have make sure you have [**Python 3.7** or higher installed](https://www.python.org/downloads/).

If you have the right version installed, you should have something similar:
```sh
python --version || python3 --version
> Python 3.10.6 # OK
```

We'll now create our project in a virtual environment and install packages we need:
```sh
mkdir flask-workshop-poc && cd flask-workshop-poc

python -m venv venv
source venv/bin/activate

pip install flask mysql-connector-python
```

## MySQL

TODO

One thing is missing to our backend: a database!  
In this workshop, we'll use [**mysql**](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04).

If you have the right version installed, you should have something similar:
```sh
mysql --version
> mysql   Ver 8.0.30-0ubuntu0.22.04.1 for Linux on x86_64 ((Ubuntu)) # OK
```


[Go back to the exercises](./README.md)