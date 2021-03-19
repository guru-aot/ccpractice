

@REM Bring down any previously running containers
docker-compose down

@REM  Build images
echo 'Building images...'
docker-compose build --no-cache

@REM  pause

echo 'Complete'


@REM  Bring up new containers (silently)
docker-compose up -d BACKEND

timeout /t 10 /nobreak > NUL

docker-compose up -d FRONTEND

timeout /t 10 /nobreak > NUL

start "" http://localhost:8080/




