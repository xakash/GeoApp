FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1


COPY ./src/requirements.txt /src/

WORKDIR /src

# COPY ./scripts/entrypoint.sh /src/

RUN apt-get update
RUN apt-get install -y apt-utils software-properties-common && apt-get update

RUN apt-get install -y --on-install-recommends binutils libproj-dev gdal-bin

RUN pip install --no-cache-dir -r requirements.txt


COPY ./src /src




COPY ./scripts /scripts

RUN chmod +x /scripts/*

# RUN adduser user
# RUN chown -R user:user /vol
# RUN chmod -R 755 /vol/app

# USER user

CMD ["sh", "../scripts/entrypoint.sh"]

EXPOSE 8000

