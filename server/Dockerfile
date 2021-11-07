FROM python:3.6
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r /app/requirements.txt

ENTRYPOINT [ "python", "-u", "/app/server.py" ]