FROM ubuntu:latest
LABEL authors="Vinicius Morgado"

ENTRYPOINT ["top", "-b"]