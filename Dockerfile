FROM python:alpine
WORKDIR /target
COPY . .
RUN pip install -r requirements.txt
RUN python crawl.py
CMD ["gunicorn", "
