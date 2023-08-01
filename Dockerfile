FROM python:3.10 

WORKDIR /app

RUN apt-get update && apt-get install -y ffmpeg 

COPY . . 

RUN pip3 install -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]




