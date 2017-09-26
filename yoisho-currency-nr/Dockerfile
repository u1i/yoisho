FROM reelio/debian-lxml
MAINTAINER uli.hitzel@gmail.com

RUN mkdir /app
RUN pip install spyne
COPY app /app
RUN useradd -c 'webservice' -m -d /home/webservice -s /bin/bash webservice
USER webservice
ENV HOME /home/webservice

EXPOSE 8080
CMD ["python","/app/currency.py"]


