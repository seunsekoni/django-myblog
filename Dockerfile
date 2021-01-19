FROM python:3.8

# ensures that the output Django writes to the terminal comes out in real time without being buffered 
# somewhere. This makes your Docker logs useful and complete.
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app