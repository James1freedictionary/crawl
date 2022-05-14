FROM python:alpine
ADD . /target
WORKDIR /target
RUN pip install -r requirements.txt

RUN python crawl.py 
CMD gunicorn --bind 0.0.0.0:$PORT k:l

