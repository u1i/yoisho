FROM alpine
MAINTAINER uli.hitzel@gmail.com
RUN apk update
RUN apk add python2
RUN apk add py-pip
RUN mkdir /app
RUN pip install cherrypy bottle
COPY app /app
USER 9000
EXPOSE 8080
CMD ["python","/app/server.py"]
