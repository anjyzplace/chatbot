FROM ubuntu:16.04

# Install MongoDB.
RUN \
  apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10 && \
  echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' > /etc/apt/sources.list.d/mongodb.list && \
  apt-get update && \
  apt-get install -y mongodb-org && \
  rm -rf /var/lib/apt/lists/*

# Define mountable directories.
VOLUME ["/data/db"]

RUN mkdir -p /data/db

EXPOSE 27017
# Define working directory.
WORKDIR /data

COPY . .

# RUN mongoimport --db microsoftbotframework --collection healthdata --type csv --headerline --file /data/newhealthdata.csv
RUN ls
# RUN mongod --dbpath /data/db --fork --syslog && mongoimport --db microsoftbotframework --collection healthdata --type csv --headerline --file ./data/newhealthdata.csv

# RUN mongod --dbpath /data/db --fork --syslog && mongoimport --db microsoftbotframework --collection exercise --type csv --headerline --file ./data/exercise_recommendation.csv
# Define default command.
EXPOSE 27017

# CMD ["/bin/bash", "/scripts/populate.sh"]

CMD /bin/bash -c  ./scripts/populate.sh

# Expose ports.
#   - 27017: process
#   - 28017: http
