FROM python:3.7-alpine

WORKDIR /code
RUN pip install requests
ADD . /code

EXPOSE 8000
CMD ["python3", "server.py"]