

@REM Bring down any previously running containers
docker-compose down

@REM  Build images
echo 'Building images...'
docker-compose build --no-cache

@REM  pause

echo 'Complete  Building'


@REM  Bring up new containers (silently)

echo 'Compose up CAMUNDA BPM...'
docker-compose up -d CAMUNDA

timeout /t 10 /nobreak > NUL
echo 'deploying WorkFlow'
docker exec -it cccamundacontainer /bin/bash -c "/app/deploywfmodel.sh"

timeout /t 5 /nobreak > NUL

echo 'Compose Up  PostgreDB ... '
docker-compose up -d postgresqldb

timeout /t 10 /nobreak > NUL

echo 'Migrating DB to  PostgreDB ... '
docker-compose up -d setupdb

timeout /t 10 /nobreak > NUL

echo 'Compose up BACKEND python flask ... '
docker-compose up -d BACKEND

timeout /t 10 /nobreak > NUL

echo 'Compose up FRONTEND VueJS app... '
docker-compose up -d FRONTEND

timeout /t 10 /nobreak > NUL

start "" http://localhost:8080/




