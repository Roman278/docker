FROM alpine:3.18
WORKDIR /src
COPY . .
RUN pip install
RUN yum install php
