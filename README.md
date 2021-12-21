# ValidityTest2021

1. Build Docker image
```
docker build -t validity-test .
```

2. Run image
```
docker run -dp 3000:3000 --name app validity-test
```

3. Run image using Docker Compose
```
docker-compose -f docker-compose.dev.yml up --build -d
```
