FROM python:3.10

ENV MYSQL_SERVICE_HOST=''
ENV MYSQL_DB_USER=''
ENV MYSQL_DB_PASSWORD=''
ENV MYSQL_DB=''
ENV MYSQL_SERVICE_PORT=''

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt
RUN apt-get update -y  && apt-get install -y dnsutils
RUN apt-get update -y  && apt-get install -y curl
RUN apt-get update -y  && apt-get install -y iputils-ping
RUN apt-get update -y  && apt-get install -y netcat-traditional
RUN apt-get update -y  && apt-get install -y vim
RUN apt-get update -y  && apt-get install -y iptables
RUN apt-get update -y  && apt-get install -y iproute2
RUN apt-get update -y  && apt-get install -y net-tools

CMD ["python3","app.py"]