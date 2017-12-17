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
                            gunicorn \
                            language-pack-en

RUN apt-get update && \
            apt-get install -y software-properties-common vim \
                              python-pip python-dev build-essential

ENV LANG en_GB.UTF-8

RUN wget https://bootstrap.pypa.io/get-pip.py -O /tmp/get-pip.py

RUN python3 /tmp/get-pip.py

RUN pip install --user pipenv

RUN apt-get update

RUN python3 --version

RUN pip --version

RUN pip install -U nltk

RUN python3 -m nltk.downloader punkt

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY . /usr/src/app/

RUN echo $LANG

RUN pip install -r requirements.txt

CMD [ "python3", "app/main.py" ]


