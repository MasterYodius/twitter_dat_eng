FROM python:3.7

WORKDIR /app

ENV FLASK_APP=app.py

COPY src/requirements.txt .

RUN pip install -r src/requirements.txt

COPY . .

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD ["app.py"]
