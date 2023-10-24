FROM python:3.11.15
LABEL authors="nzern"
ENV WORKSPACE /opt/installs
RUN mkdir -p $WORKSPACE
WORKDIR $WORKSPACE
COPY requirements.txt requirements.txt
RUN python3.11 -m pip install -r requirements.txt
COPY assistant_on_demand.proto ./
COPY assistant_on_demand_pb2.py ./
COPY assistant_on_demand_pb2_grpc.py ./
COPY bot_connection.py ./
COPY publisher.py ./
COPY vars.py ./
COPY server.py ./
COPY README.md ./
CMD ["python3.11", "server.py"]