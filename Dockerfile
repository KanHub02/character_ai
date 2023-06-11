FROM python:3.9-alpine

RUN mkdir -p /opt/services/charai-web

WORKDIR /opt/services/charai-web

ADD requirements.txt /opt/services/charai-web

ADD . /opt/services/charai-web

RUN apk add --no-cache gcc curl musl-dev linux-headers && \
        chmod 755 /opt/services/charai-web/entrypoints/* && \
            chmod +x /opt/services/charai-web/entrypoints/* && \
                pip install -r requirements.txt