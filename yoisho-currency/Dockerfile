FROM reelio/debian-lxml
MAINTAINER uli.hitzel@gmail.com

RUN mkdir /app
RUN pip install spyne
COPY app /app

CMD ["python","/app/currency.py"]


