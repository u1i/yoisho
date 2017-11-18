FROM reelio/debian-lxml
MAINTAINER uli.hitzel@gmail.com

EXPOSE 8080
RUN mkdir /app
RUN pip install cherrypy bottle
COPY app /app

CMD ["python","/app/server.py"]


