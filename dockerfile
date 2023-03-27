FROM    bitnami/pytorch:latest
ADD     req.txt .
RUN     pip install -r req.txt
WORKDIR /app
ADD     7_predict.py .
ADD     dogs_cats_model.pth .
CMD     ["python", "7_predict.py"]
