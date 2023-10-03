FROM Ubuntu:latest

ENV API_type="text"


RUN apt-get update && apt-get install -y python3 python3-pip

WORKDIR /app

COPY dockerScript.py /app/dockerScript.py
COPY API_type_text_config.json /app/API_type_text_config.json
COPY API_type_image_config.json /app/API_type_image_config.json
RUN mkdir -p /app/output
RUN pip install requirements.txt
CMD ["python3","dockerScript.py"] 
