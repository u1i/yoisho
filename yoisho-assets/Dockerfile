FROM reelio/debian-lxml
MAINTAINER uli@sotong.io

RUN mkdir /app
RUN pip install spyne
COPY app /app

CMD ["python","/app/assets.py"]


