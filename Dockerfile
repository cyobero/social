FROM python:3.7

WORKDIR /code
COPY . /code/
RUN chmod -R 755 env/
RUN env/bin/activate
RUN pip install -r requirements.txt
