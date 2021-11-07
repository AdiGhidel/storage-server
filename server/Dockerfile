FROM python:3.6
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r /app/server/requirements.txt

ENTRYPOINT [ "python", "-u", "/app/server/server.py" ]