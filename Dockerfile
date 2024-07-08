FROM python:3.10.12-slim

WORKDIR /app

COPY requirements.txt requirements.txt
COPY fastapi_.py fastapi_.py
COPY config.py config.py
COPY utils.py utils.py
COPY data/train.csv data/train.csv
COPY models/xgb_model.pkl models/xgb_model.pkl

RUN pip install -U pip
RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["uvicorn", "fastapi_:app", "--host", "0.0.0.0", "--port", "8080"]
