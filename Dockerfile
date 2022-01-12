FROM mcr.microsoft.com/azureml/openmpi3.1.2-ubuntu18.04:20210615.v1

RUN conda install pip
RUN pip install pandas
RUN pip install numpy

COPY . /app

CMD  /opt/miniconda/bin/python -m app.src.main
