FROM python:3.8.12-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install build-essential -y && \
    apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Add the application source code.
COPY requirements.txt .

RUN pip install --upgrade pip --user && \
    pip install --no-cache-dir -r requirements.txt && \
    rm -rf requirements.txt && rm -rf /var/lib/apt/lists/*

COPY . .

RUN mkdir -p /root/.streamlit

RUN bash -c 'echo -e "\
    [server]\n\
    enableCORS = false\n\
    " > /root/.streamlit/config.toml'

# remember to expose the port your app'll be exposed on.
EXPOSE 8080

# run it!
CMD ["streamlit", "run", "app/main.py", "--server.port=8080", "--server.address=0.0.0.0"]
