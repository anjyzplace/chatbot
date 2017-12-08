#!/bin/bash

mongod --dbpath /data/db --fork --syslog && mongoimport --db microsoftbotframework --collection healthdata --type csv --headerline --file ./data/newhealthdata.csv