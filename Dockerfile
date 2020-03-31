FROM python:3.8-slim AS compile

RUN apt-get -y update && \
	apt-get -y install --no-install-recommends \
	curl \
	gcc \
	openssl \
    build-essential \
	libcurl4-openssl-dev \
	libssl-dev \
	pkg-config \
	graphviz-dev \
	&& rm -rf /var/lib/apt/lists/*

ENV PYTHONDONTWRITEBYTECODE=1
WORKDIR /opt/application

RUN python3 -m venv /home/app/venv
ENV PATH="/home/app/venv/bin:$PATH"

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip gunicorn && \
    pip3 install --no-cache-dir -r requirements.txt


# production image
FROM python:3.8-slim
RUN useradd --create-home app

COPY --from=compile /home/app/venv /home/app/venv

ENV PATH="/home/app/venv/bin:$PATH"

WORKDIR /home/app
USER app

COPY ./app app/
COPY ./instance instance/
COPY ./assets assets/
COPY package.json package.json
COPY run.py run.py
COPY gunicorn_config.py gunicorn_config.py

CMD ["gunicorn", "--config", "./gunicorn_config.py", "run:app"]