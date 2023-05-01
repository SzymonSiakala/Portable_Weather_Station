# Portable Weather Station
# Szymon Siąkała

# DOCKERFILE

FROM python:3.9

WORKDIR /python-docker

COPY requirements.txt ./

RUN pip install -r requirements.txt
RUN pip install RPi.GPIO

COPY . .

ENV TZ="Europe/Warsaw"

CMD ["/bin/bash", "-c", "python3 -m flask initialize; python3 -m flask load; python3 -m flask run --host=0.0.0.0"]