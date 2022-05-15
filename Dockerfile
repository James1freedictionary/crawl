FROM python
ADD . /target
WORKDIR /target
RUN pip install -r requirements.txt
RUN python crawl.py

