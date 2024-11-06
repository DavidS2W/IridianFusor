FROM ubuntu:20.04 AS builder-image

# avoid stuck build due to user prompt
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install --no-install-recommends -y python3.9 python3.9-dev python3.9-venv python3-pip python3-wheel build-essential && \
	apt-get clean && rm -rf /var/lib/apt/lists/*

# create and activate virtual environment
# using final folder name to avoid path issues with packages
RUN python3.9 -m venv /home/yourdir/venv
ENV PATH="/home/yourdir/venv/bin:$PATH"

# install requirements
COPY requirements.txt .
RUN pip3 install --no-cache-dir wheel
RUN pip3 install --no-cache-dir -r requirements.txt

FROM ubuntu:20.04 AS runner-image
RUN apt-get update && apt-get install --no-install-recommends -y python3.9 python3-venv && \
    # Install ffmpeg and opus
    apt-get install -y ffmpeg && apt-get install libopus0



RUN useradd --create-home yourdir
COPY --from=builder-image /home/yourdir/venv /home/yourdir/venv

USER root
RUN mkdir /home/yourdir/code
WORKDIR /home/yourdir/code
COPY . .

EXPOSE 8080

# make sure all messages always reach console
ENV PYTHONUNBUFFERED=1

# activate virtual environment
ENV VIRTUAL_ENV=/home/yourdir/venv
ENV PATH="/home/yourdir/venv/bin:$PATH"


# /dev/shm is mapped to shared memory and should be used for gunicorn heartbeat
# this will improve performance and avoid random freezes
CMD python main.py