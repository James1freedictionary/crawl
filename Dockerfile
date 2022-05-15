FROM python
COPY . /target
WORKDIR /target
RUN pip install -r requirements.txt
RUN python "crawl - BAckup.py"
CMD ["bash"]

