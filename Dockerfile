FROM ubuntu:trusty

MAINTAINER Joel James <joel.james1985@gmail.com>


## Install Build Tools
RUN apt-get update && \
    apt-get install -y build-essential zlib1g-dev libssl-dev libreadline6-dev libyaml-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


## Add User
RUN useradd -ms /bin/bash app
RUN adduser app sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
RUN chmod 4755 /usr/bin/sudo
ENV HOME /home/app

## Install Python3 Tools and Postgres Tools
RUN apt-get update && \
    apt-get install -y wget python3-pip python3-dev python3-software-properties && \
    apt-get install -y libpq-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

## Install Node/Npm
ENV NODE_VERSION 0.11.14
ENV NPM_VERSION 2.1.6
RUN wget -q "http://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.gz" \
  && tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local --strip-components=1 \
  && rm "node-v$NODE_VERSION-linux-x64.tar.gz" \
  && npm install -g npm@"$NPM_VERSION" \
  && npm cache clear

EXPOSE 8000

# Don't run application as root
USER app

# Install Python dependencies
WORKDIR /usr/src/app
ADD requirements.txt /usr/src/app/
RUN sudo pip3 install -r requirements.txt

# Install Node dependencies
ADD app/assets/package.json /usr/src/app/app/assets/package.json
RUN cd app/assets/ && sudo npm install && cd ../..

ADD . /usr/src/app
RUN sudo chown -R app /usr/src/app

# Browserify (Build js)
# RUN cd app/assets/ && npm run build-js && cd ../..
