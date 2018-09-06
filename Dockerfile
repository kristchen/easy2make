FROM python:3.6
RUN mkdir /easy2make
WORKDIR /easy2make
ADD . /easy2make
RUN chmod +x /easy2make/entrypoint.sh
RUN apt-get install -y default-libmysqlclient-dev
RUN pip install -r requirements.txt
EXPOSE 8000
