FROM python:3.10.6-buster

WORKDIR Heart_Risk_Kaggle/

COPY .venv .venv
COPY requirements.txt requirements.txt
COPY fastapi_.py fastapi_.py
COPY config.py config.py
COPY utils.py utils.py
COPY data/train.csv data/train.csv
COPY models/model_final_svm.pkl models/model_final_svm.pkl

RUN pip install -U pip
RUN pip install -r requirements.txt

CMD uvicorn fastapi_:app --host 0.0.0.0 --port 8080