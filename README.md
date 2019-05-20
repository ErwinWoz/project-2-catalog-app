# Catalog Application

## Overview
This application provides a list of sport items within a variety of sport categories as well as provide a user registration and authentication system. Registered users will have the ability to add, edit and delete their own items.
Modern web applications perform a variety of functions and provide amazing features and utilities to their users;but deep down, it’s really all just creating, reading, updating and deleting data.

## Required Libraries and Dependencies
The project requires the following software:

- [Python](https://www.python.org/downloads/)
- [Flask](http://flask.pocoo.org/)
- [SQLite](https://www.sqlite.org/index.html) 
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Bootstrap](https://getbootstrap.com/)

## Setup and Instalation:
This project is run in a virutal machine created using Vagrant

1. Install [Vagrant](https://www.vagrantup.com/)
1. Install [VirtualBox](https://www.virtualbox.org/)
1. Inside vagrant directory create new directory called: catalog
`mkdir catalog` 
1. Download this project on your machine: [Catalog app](https://github.com/ErwinWoz/project-2-catalog-app)
1. Unzip and copy all files into the directory called 'catalog' that you have just created

## Running the project
1. Using terminal navigate to your project e.g. /Udacity/projects
1. cd to vagrant directory
`cd vagrant`
1. Build your vm using
`vagrant up` command
1. It might take a while. Once it's build use
`vagrant ssh` command to connect
1. cd to correct directory 
`cd /vagrant/catalog`
1. run script
`python application.py`
When ImportError - you might need to download some libraries to run this applicaton. All needed libraries are on top of the application.py file. Depending on your error message download libraries using terminal.
import error example: 
`$ python application.py`
`Traceback (most recent call last):`
  `File "application.py", line 3, in <module>`
    `import httplib2`
`ImportError: No module named httplib2`

To download missing module run in terminal:
`pip install --user httplib2`
Use this command do download all needed modules
1. Open your web browser to this URL: http://localhost:5000
1. In order to add, edit and delete items in categories you have to login first with your Google account.


1. This app also implements API endpoints with responses formatted in JSON. ( /JSON )







