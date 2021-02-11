FROM redis:alpine3.12

RUN apk update && apk add supervisor && apk add python3 && apk add py3-pip && pip3 install redis flask

RUN mkdir -p /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY FlaskRedis.py .
COPY HelloRedis.py .

EXPOSE 8080

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
