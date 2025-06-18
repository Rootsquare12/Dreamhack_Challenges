FROM ubuntu:24.04

ENV USER rootsquare

USER root
RUN apt-get update && apt-get install -y socat python3 python3-pip
RUN adduser -u 1337 $USER

WORKDIR /home/rootsquare

COPY shell.py .
COPY secret .

RUN chown $USER:$USER /home/rootsquare/shell.py /home/rootsquare/secret
RUN chmod 0500 /home/rootsquare/shell.py
RUN chmod 0400 /home/rootsquare/secret

USER $USER

EXPOSE 5000

CMD ["socat", "TCP-LISTEN:5000,reuseaddr,fork", "EXEC:python3 shell.py,nofork,stderr"]
