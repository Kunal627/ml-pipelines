FROM tensorflow/tfx:latest
WORKDIR /airflow
COPY ./script .
ENV AIRFLOW_HOME=/airflow
ENV AIRFLOW_VERSION=2.2.4
ENV AIRFLOW_ADMIN_PASSWORD=admin
ENV AIRFLOW__CORE__LOAD_EXAMPLES=False
RUN sh setup_airflow.sh
COPY ./config/airflow.cfg .
COPY ./pipeline ./dags
EXPOSE 8080
ENTRYPOINT ["sh", "-c" , "./start_airflow.sh"]
#ENTRYPOINT ["tail", "-f", "/dev/null"]