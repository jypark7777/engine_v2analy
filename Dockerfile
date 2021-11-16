FROM python:3.9.7

RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
RUN apt-get -y install tzdata g++ git curl
RUN apt-get -y install default-jdk default-jre

RUN pip install --upgrade pip

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

RUN pip install konlpy
RUN bash -c "$(curl -s https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh)"

WORKDIR /app/mecab-0.996-ko-0.9.2
RUN ./configure
RUN make
#RUN make check
RUN make install

WORKDIR /app/mecab-ko-dic-2.1.1-20180720
RUN autoreconf
RUN ./configure
RUN make
RUN make install
RUN pip install mecab-python3

RUN apt-get install -y nginx

# 기존에 존재하던 Nginx설정 파일들 삭제
RUN rm -rf /etc/nginx/sites-available/*
RUN rm -rf /etc/nginx/sites-enabled/*

COPY nginx.conf /etc/nginx/nginx.conf
COPY featuringeg-analy_gunicorn /etc/nginx/sites-available/

RUN mkdir -p /etc/nginx/sites-enabled/
RUN ln -s /etc/nginx/sites-available/featuringeg-analy_gunicorn /etc/nginx/sites-enabled/

#supervisor 추가
RUN apt-get -y install supervisor
COPY supervisor-app.conf /etc/supervisor/conf.d/

WORKDIR /app

EXPOSE 80
#supervisor 사용
CMD ["bash", "-c", "/usr/bin/supervisord -c /etc/supervisor/conf.d/supervisor-app.conf"]

#EXPOSE 8000
#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

#EXPOSE 80
#CMD ["service", "nginx", "start"]
#CMD ["nginx", "-g", "daemon off;"]

