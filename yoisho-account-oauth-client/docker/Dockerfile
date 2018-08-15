FROM alpine
MAINTAINER uli.hitzel@gmail.com

EXPOSE 8080

RUN apk update
RUN apk add python2
RUN apk add py-pip
RUN mkdir /app
RUN pip install cherrypy bottle requests
COPY yoisho-client.py /app/yoisho-client.py

CMD ["python","/app/yoisho-client.py"]
