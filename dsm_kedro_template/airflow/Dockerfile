FROM apache/airflow:2.4.1-python3.8

# COPY etl-pipeline/dist/etl_pipeline-0.1-py3-none-any.whl  /resource/
# RUN pip install /resource/etl_pipeline-0.1-py3-none-any.whl 
# RUN pip install



# upgrade db for airflow
RUN airflow db upgrade


# install git as root
USER root
RUN echo 'airflow ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers
USER airflow
RUN sudo apt update && sudo apt-get install -y git

ADD . /code

WORKDIR /code/etl-pipeline
RUN pip install -r src/requirements.txt --use-deprecated=legacy-resolver

# install conflict package
RUN pip install attrs==22.1.0