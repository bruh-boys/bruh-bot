FROM ubuntu:20.04

WORKDIR /usr/bot

COPY . .

# install the dependencies
RUN apt update -y && apt upgrade -y
RUN apt-get install -y python3.8
RUN apt install python3-pip -y
RUN apt-get install -y curl

RUN pip3 install -r requirements.txt

# excute the bot
CMD ["python3","bot.py"]