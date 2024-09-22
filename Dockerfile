FROM python:latest

WORKDIR /app

COPY requirements.txt .

#install all lib
RUN pip install -r requirements.txt

#copy all
COPY . .

#port
EXPOSE 8000

CMD ["uvicorn", "main:app", "--reload", "--port", "8000", "--host", "127.0.0.1"]

