FROM ubuntu:17.10
LABEL Author="anjola.awofisoye@sky.uk"

RUN apt-get update && \
            apt-get install -y tar \
                            git \
                            curl \
                            nano \
                            wget \
                            unzip \
                            dialog \
                            net-tools \
                            build-essential \
                            language-pack-en

RUN apt-get update && \
            apt-get install -y software-properties-common vim \
                              python-pip python-dev build-essential

ENV LANG en_GB.UTF-8

RUN wget https://bootstrap.pypa.io/get-pip.py -O /tmp/get-pip.py

RUN python3 /tmp/get-pip.py

RUN pip install --user pipenv
# RUN python3.6 -m pip install pip --upgrade

# RUN python3.6 -m pip install wheel
RUN apt-get update

RUN python3 --version

RUN pip --version

RUN pip install -U nltk

RUN python3 -m nltk.downloader punkt

# RUN wget https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages/tokenizers/punkt.zip

# RUN unzip -d /usr/nltk_data/ punkt.zip

# RUN mkdir /usr/nltk_data/

# RUN mv punkt.zip /usr/nltk_data/

# RUN mv /usr/nltk_data/punkt/* /usr/nltk_data/ 

# RUN ls

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

# Install app dependencies
COPY . /usr/src/app/



RUN echo $LANG

RUN pip install -r requirements.txt

# RUN export LANG=en_GB.UTF-8

CMD [ "python3", "main.py" ]