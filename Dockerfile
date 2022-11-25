FROM python:3.10.7-slim

WORKDIR /workdir

ENV PATH /root/.local/bin:$PATH

COPY . /workdir
RUN apt update -y -qq && apt install -y curl
RUN pip install -U pip \
  && (curl -sSL https://install.python-poetry.org | python3 - --version 1.2.2) \
  && poetry config virtualenvs.create false \
  && poetry install 

