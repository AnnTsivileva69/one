FROM continuumio/miniconda3

COPY environment.yml model.pkl predict_model.py ./

RUN conda env create -f environment.yml
ENV PATH /opt/conda/envs/mlops_project/bin:$PATH
RUN /bin/bash -c "source activate mlops_project"

CMD [ "python", "predict_model.py" ]

