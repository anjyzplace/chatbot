## Setup

### Install Microsoft Bot framework
https://dev.botframework.com/

### Install Microsoft Bot framework  
http://microsoftbotframework.readthedocs.io/en/latest/

### Install Microsoft Bot framework  Emulator
https://github.com/Microsoft/BotFramework-Emulator/releases/
### Start app
At the root of the application, run the command below.

```python
python main.py

```

### Launch Bot Framework 
Connect to http://localhost:5000/api/messages


# Using Docker ?

In the root folder run

```
docker-compose up
```

To run the tests before starting the app, run;
```
docker-compose -f docker-compose-test up
```
## Install ngrok

Download and install ngrok from https://ngrok.com/download


## Setup ngrok

Extract to folder and add folder to path if on Windows

Run the command below so we can setup

```
ngrok.exe http 5000 -host-header="localhost:5000"
```

  In Emulator settings, add the ngrok path to the URL for the emulator

```
Session Status                online
Version                       2.2.8
Region                        United States (us)
Web Interface                 http://127.0.0.1:4041
Forwarding                    http://0736d439.ngrok.io -> localhost:5000
Forwarding                    https://0736d439.ngrok.io -> localhost:5000

Connections                   ttl     opn     rt1     rt5     p50     p90
                              0       0       0.00    0.00    0.00    0.00
```
e.g.  http://0736d439.ngrok.io/api/messages                             


### To connect the emulator with an online bot, run using the IP or doamin name

```
ngrok http 192.168.1.1:5000
```

<category>
<pattern> What is your name </pattern>
<template>My name is Henry. </template>
</category>
