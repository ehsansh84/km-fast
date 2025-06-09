FROM python:3.10
WORKDIR /app
COPY requirements.txt /app/
RUN mkdir /app/logs
RUN mkdir /app/uploads
RUN mkdir /app/media
RUN pip install -r /app/requirements.txt
COPY . /app/
COPY docker.env /app/.env
CMD python /app/app/main.py
