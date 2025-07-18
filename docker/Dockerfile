# syntax=docker/dockerfile:1

FROM python:3.12-slim AS base
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential libxml2-dev libxslt1-dev libldap2-dev libsasl2-dev xmlsec1 git && \
    rm -rf /var/lib/apt/lists/*

FROM node:20-slim AS frontend-builder
WORKDIR /frontend
COPY package.json yarn.lock ./
RUN yarn install --frozen-lockfile
COPY ./ ./
RUN yarn build || yarn run build

FROM base AS dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

FROM base AS application
RUN adduser --disabled-password --gecos '' pda && mkdir /data && chown -R pda:pda /app /data
USER pda
COPY --from=dependencies /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=frontend-builder /frontend/powerdnsadmin/static ./powerdnsadmin/static
COPY . .

FROM application AS production
ENTRYPOINT ["/usr/local/bin/gunicorn","powerdnsadmin:create_app()"]
CMD ["-t","120","-w","4","-b","0.0.0.0:80"]
