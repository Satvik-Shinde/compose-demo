# Python Flask and MySQL using Docker Compose

### 1. Build and Start Containers
```bash
docker compose up -d --build
```

### 2. Check Container Status
```bash
docker compose ps
```

### 3. View Logs
```bash
docker compose logs
```

### 4. Access the Application

Open the configured application port in your browser, for example:

```text
http://localhost:5000
```

### 5. Access MySQL
```bash
docker compose exec mysql mysql -u root -p
```

### 6. Stop and Remove Containers
```bash
docker compose down
```


