FROM python:2.7

WORKDIR /usr/src/app
COPY . /usr/src/app

RUN pip install newrelic-plugin-agent[mongodb]
RUN pip install pyyaml

CMD bash start.sh
