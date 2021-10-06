FROM python:3.6.1-alpine


WORKDIR /Weavegrid
ADD . /Weavegrid
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "application.py"]