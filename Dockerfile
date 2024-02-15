FROM python:3.9-slim-buster
WORKDIR /app
COPY ./requirements.txt requirements.txt
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8080
ENV FLASK_APP=app.py
CMD ["python", "-m", "flask", "run", "--host", "0.0.0.0"]
