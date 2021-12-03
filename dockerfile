FROM registry.access.redhat.com/ubi8/python-38:latest

# copy files
COPY ./requirements.txt /app/requirements.txt
COPY ./main.py /app/main.py
# copy static files
COPY ./static /app/static/frontend

WORKDIR /app/

# install requirements
RUN pip3 install -r requirements.txt

# execute the run script
CMD python3 main.py