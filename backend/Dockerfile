###########
# BUILDER # 
# ---- Docker container built in 2 stages – the Builder stage and the Final stage
# use this Dockerfile to prepare our container before it is up and running our django_app 
# as one of the services for docker-compose. 
# Since a container is nothing but a stripped-down version of Linux, 
# we would need to prepare it before it is ready to run our django_app. 
# This is what all the steps in the Dockerfile define. Some other parameters 
# would be defined in the docker-compose file
###########

# pull official base image
FROM python:3.7.9-slim-stretch as builder

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt


#########
# FINAL #
#########

# pull official base image
FROM python:3.7.9-slim-stretch

# installing netcat (nc) since we are using that to listen to postgres server in entrypoint.sh
RUN apt-get update && apt-get install -y --no-install-recommends netcat && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# install dependencies
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --no-cache /wheels/*

# set work directory
WORKDIR /usr/src/app

# copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

# copy our django project
COPY ./django_app .

# run entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]