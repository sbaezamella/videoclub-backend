###########
# BUILDER #
###########

# Base Image
FROM python:3 as base

# Install Requirements
COPY requirements.txt /
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /wheels -r requirements.txt

#########
# FINAL #
#########

# Base Image
FROM python:3-slim

# Create directory for the app user
RUN mkdir -p /home/app

# Create the app user
RUN groupadd app && useradd -g app app

# Create the home directory
ENV HOME=/home/app
ENV APP_HOME=/home/app/fastapi
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# Install Requirements
COPY --from=base /wheels /wheels
COPY --from=base requirements.txt .
RUN pip install --no-cache /wheels/*

# Copy in the FastAPI code
COPY . $APP_HOME
# ENV PYTHONPATH=$APP_HOME

# Chown all the files to the app user
RUN chown -R app:app $APP_HOME

# Change to the app user
USER app
