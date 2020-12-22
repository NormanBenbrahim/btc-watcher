# https://hub.docker.com/r/tiangolo/uvicorn-gunicorn/
FROM tiangolo/uvicorn-gunicorn:python3.7-slim

# Allow statements and log   messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

# Copy local code to the container image.
ENV APP_HOME /container_image
WORKDIR $APP_HOME
COPY . ./

# update and install c compiler
RUN apt-get update -y
RUN apt-get -y install gcc

# install python dependencies
RUN pip install --no-cache-dir --use-feature=2020-resolver -r requirements.txt 

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
CMD exec gunicorn -k uvicorn.workers.UvicornWorker --bind :$PORT --workers 4 --threads 8 --timeout 0 app:app