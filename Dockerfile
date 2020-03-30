FROM maestroserver/maestro-python-gcc

RUN apk add --no-cache --virtual .build-dependencies pkgconfig graphviz-dev && \
    apk del --no-cache --purge .build-dependencies \
    RUN rm -rf /var/cache/apk/*

ENV APP_PATH=/opt/application
WORKDIR $APP_PATH

COPY docker-entrypoint.sh /usr/local/bin/
COPY ./app app/
COPY ./instance instance/
COPY ./assets assets/
COPY requirements.txt requirements.txt
COPY package.json package.json
COPY run.py run.py
COPY gunicorn_config.py gunicorn_config.py

RUN chmod +x /usr/local/bin/docker-entrypoint.sh
RUN addgroup -S app && adduser -S app -G app
RUN pip3 install --upgrade pip gunicorn && \
    pip3 install -r requirements.txt

ENTRYPOINT ["/sbin/tini","-g","--"]
CMD ["docker-entrypoint.sh"]