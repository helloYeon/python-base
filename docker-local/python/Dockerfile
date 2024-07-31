FROM python:3.11.9

##############################
# initialize
##############################
WORKDIR /app
COPY requirements.txt /app/
COPY src /app

##############################
# apt
##############################
RUN apt update
RUN apt-get update
RUN apt -y upgrade
RUN apt -y install vim apt-utils

##############################
# python
##############################
ENV PATH=$PATH:/app/site-packages/bin \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN pip install --upgrade pip
RUN pip install --force-reinstall -r requirements.txt

##############################
# alias & cmd
##############################
RUN echo 'alias ll="ls -al"' >> ~/.bashrc

CMD ["bash", "-c", "while :; echo 1;do sleep 2; done"]
