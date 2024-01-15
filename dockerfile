FROM alpine:3.18
WORKDIR /src
COPY . .
RUN yum -y install mkpasswd && yum -y clean all  && rm -rf /var/cache
RUN yum install php
