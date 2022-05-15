FROM python
COPY . /target
WORKDIR /target
RUN pip install -r requirements.txt
CMD python "crawl - BAckup.py"

