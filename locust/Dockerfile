
FROM python:3.8

WORKDIR /app/

RUN pip install zeroc-ice locust \
    --index-url http://mirrors.aliyun.com/pypi/simple/ \
    --trusted-host mirrors.aliyun.com

COPY demo ./demo/
COPY locust/app/locustfile.py .
