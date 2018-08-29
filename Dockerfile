FROM python:3.6
RUN mkdir /easy2make
WORKDIR /easy2make
ADD . /easy2make
RUN apt-get install -y libmysqlclient-dev
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "/binup-api/manage.py", "makemigrations"]
CMD ["python", "/binup-api/manage.py", "migrate"
CMD ["python", "/binup-api/manage.py", "runserver", "0.0.0.0:8000"]
