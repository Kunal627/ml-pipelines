# ml-pipelines
deploy ml models



# TFX pipeline on local Airflow setup with docker

1. cd  /ml-pipelines

# to build the image
2. docker build --no-cache -t kunal627/tfx:v1 -f .\docker\Dockerfile . 

# to run the container

3. docker run -d -p 8080:8080 -v $PWD/input:/airflow/input:ro -v tfxartifacts:/airflow/tfxartifacts  kunal627/tfx:v1