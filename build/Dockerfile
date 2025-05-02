FROM alpine:latest
LABEL MAINTAINER="https://github.com/PrathamJain10/PhantomStrikes"
WORKDIR /PhantomStrikes
ADD . /PhantomStrikes
RUN apk add --no-cache bash ncurses curl unzip wget php
CMD ["bash", "scripts/Phantom.sh"]
