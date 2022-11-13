FROM python:3.10.4-slim

# Install python/pip

COPY ./requirements.txt /app/requirements.txt

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8501

CMD streamlit run app/main.py