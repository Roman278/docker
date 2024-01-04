FROM golang:1.21-alpine
WORKDIR /src
COPY . .
RUN yum update
RUN yum install php
