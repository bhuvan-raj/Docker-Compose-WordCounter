
# Word Counter Multi-Container Docker Project

This project demonstrates a multi-container Docker setup involving a frontend, worker, Redis, PostgreSQL database, and a result frontend. The frontend accepts text input, the worker counts words asynchronously, and the result frontend displays the word counts.

---
![Alt Text](bc8c39caf8f8cc8d36f5fbd21f3aa492eecd2320/Screenshot%20From%202025-05-23%2023-22-55.png)

## Project Structure

```

word-counter-app/
│
├── frontend/
│   ├── app.py
│   └── Dockerfile
│
├── worker/
│   ├── worker.py
│   └── Dockerfile
│
├── result-frontend/
│   ├── app.py
│   └── Dockerfile
│
└── README.md

````

---

## Prerequisites

- Docker installed
- Basic knowledge of Docker CLI
- Internet access to download base images

---

## Step 1: Create Docker Bridge Network

```bash
docker network create app-net
````

---

## Step 2: Start Required Containers

### Start Redis Container

```bash
docker run -d --name redis --network app-net redis
```

### Start PostgreSQL Container

```bash
docker run -d --name db --network app-net \
  -e POSTGRES_USER=user \
  -e POSTGRES_PASSWORD=pass \
  -e POSTGRES_DB=wordcount \
  postgres
```

### Create `results` Table in PostgreSQL

```bash
docker exec -it db psql -U user -d wordcount -c "CREATE TABLE results (id SERIAL PRIMARY KEY, text TEXT, word_count INT);"
```

---

## Step 3: Build Docker Images

From the project root, run:

```bash
docker build -t wordcount-frontend ./frontend
docker build -t wordcount-worker ./worker
docker build -t wordcount-result-frontend ./result-frontend
```

---

## Step 4: Run Application Containers

### Frontend (Input)

```bash
docker run -d --name frontend -p 5000:5000 --network app-net wordcount-frontend
```

### Worker (Background Processor)

```bash
docker run -d --name worker --network app-net wordcount-worker
```

### Result Frontend (Display Results)

```bash
docker run -d --name result-frontend -p 7000:5000 --network app-net wordcount-result-frontend
```

---

## Step 5: Access the Application

* Frontend input form: [http://localhost:5000](http://localhost:5000)
* Result display page: [http://localhost:7000](http://localhost:7000)

---

## Troubleshooting

* If you see `Internal Server Error`, check the logs:

```bash
docker logs result-frontend
```

* Verify the `results` table exists in PostgreSQL:

```bash
docker exec -it db psql -U user -d wordcount -c "\dt"
```

---

## Notes

* All containers run on the custom bridge network `app-net` for easy inter-container communication by container name.
* Redis is used as a message queue.
* PostgreSQL stores the final word count results.
* The worker listens to Redis and processes tasks asynchronously.
* Both frontend and result frontend are Flask apps running on port 5000 inside the container but mapped to different host ports.

---

## License

MIT License

---

Feel free to reach out if you want enhancements or docker-compose support!

```

```
