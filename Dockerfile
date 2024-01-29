FROM quay.io/karmab/python:3.11-slim-bookworm

MAINTAINER Karim Boumedhel <karimboumedhel@gmail.com>

LABEL name="karmab/dummy-app" \
      maintainer="karimboumedhel@gmail.com" \
      vendor="Karmalabs" \
      version="latest" \
      release="0" \
      summary="Dummy app to communicate two sites" \
      description="Dummy app to communicate two sites"

EXPOSE 7000

RUN mkdir /root/dummy-app
ADD dummy /root/dummy-app/dummy
COPY setup.py /root/dummy-app
COPY MANIFEST.in /root/dummy-app
ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1
RUN pip3 install --no-cache /root/dummy-app jinja2

ENTRYPOINT ["/usr/local/bin/kdummy"]
