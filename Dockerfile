# Assignment: CI / CD: Flask webapp with Docker & GitHub Actions
# Date: 09/21/2022
# "Hey Siri, play September by Earth, Wind & Fire"
# Author: derekYankie

# create image from python repo
FROM python:3.10.4-alpine3.16

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# set working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . /app

# configure the container to run flask server
CMD ["python","-m","flask","run", "--host=0.0.0.0 --port=5000"]