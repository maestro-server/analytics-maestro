FROM maestroserver/maestro-python-gcc AS compile-graviz

RUN apt-get -y update && \
	apt-get -y install --no-install-recommends \
	pkg-config \
	graphviz-dev \
	&& rm -rf /var/lib/apt/lists/*

ENV PYTHONDONTWRITEBYTECODE=1
WORKDIR /opt/application

RUN python3 -m venv /home/app/venv
ENV PATH="/home/app/venv/bin:$PATH"

COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip gunicorn && \
    pip3 install --no-cache-dir -r requirements.txt


# production image
FROM python:3.8-slim
COPY --from=compile-graviz /home/app/venv /home/app/venv

ENV PATH="/home/app/venv/bin:$PATH"

RUN useradd --create-home app
WORKDIR /home/app
USER app

COPY ./ ./

CMD ["gunicorn", "--config", "./gunicorn_config.py", "run:app"]