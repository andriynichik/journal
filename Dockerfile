FROM ubuntu:20.04
RUN apt-get update && apt-get install -y python3.9 python3.9-dev
RUN apt-get -y install python3-pip
RUN apt-get -y install libusb-0.1-4 libccid pcscd libpcsclite1 pcscd pcsc-tools




# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV LD_LIBRARY_PATH=/cryptography/Modules/64



COPY requirements.txt .
# install python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# running migrations
RUN python3 manage.py migrate

# gunicorn
CMD ["gunicorn", "--config", "gunicorn-cfg.py", "core.wsgi"]
