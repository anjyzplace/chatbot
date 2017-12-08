#!/bin/bash

mongoimport --db microsoftbotframework --collection healthdata --type csv --headerline --file /data/newhealthdata.csv