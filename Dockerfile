# https://hub.docker.com/r/tensorflow/tensorflow/
FROM tensorflow/tensorflow

ENV APP_HOME /home/app

WORKDIR $APP_HOME

COPY sample.py sample.py
