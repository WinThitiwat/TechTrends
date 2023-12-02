FROM python:3.8
LABEL maintainer="Thitiwat Watanajaturaporn"

RUN mkdir techtrend_app
COPY . /techtrend_app
WORKDIR /techtrend_app

RUN pip install -r requirements.txt

# EXPOSE 3111

# CMD ["python", "app/db/init_db.py"]
# RUN python app/db/init_db.py

CMD [ "python", "main.py" ]