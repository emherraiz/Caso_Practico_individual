FROM    bitnami/pytorch:latest
ADD     req.txt .
RUN     pip install -r req.txt
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libgl1-mesa-dri

WORKDIR /app
ADD     7_predict.py .
ADD     dogs_cats_model.pth .
CMD     ["python", "7_predict.py"]
