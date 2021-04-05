FROM python:3.7.2-stretch
WORKDIR /app
ADD . /app
RUN pip install -r requirement.txt
CMD python main.py