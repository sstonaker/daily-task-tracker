FROM python:3.10

WORKDIR /usr/src/app

COPY ./setup.py setup.py

RUN pip3 install .

COPY app/ app/
COPY templates/ templates/

ENV PYTHONPATH=.

CMD ["python", "app/main.py"]