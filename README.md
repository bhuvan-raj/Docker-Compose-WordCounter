
# 🐳 Word Counter App – Docker Compose Version

This repository demonstrates a **multi-container Docker application** managed with **Docker Compose**. The project includes:

- A frontend to input text
- A worker to count words in the background
- Redis as a message queue
- PostgreSQL to store results
- A result frontend to display the word counts

---

## 📘 What is Docker Compose?

**Docker Compose** is a tool used to define and manage multi-container Docker applications. It uses a YAML file (`docker-compose.yml`) to configure the application’s services, networks, and volumes.

---

## ❓ Why Use Docker Compose?

- Manage **multiple containers** with a single command
- Easier to define networks, volumes, and dependencies
- Supports version control with a single config file
- Ideal for **development, testing, and teaching**

---

## ⚙️ Installing Docker Compose

Docker Compose is included in **Docker CLI v2+**, so if you have Docker installed, you likely already have Compose:

```bash
docker compose version
````

If not installed, follow the [official instructions](https://docs.docker.com/compose/install/) for your OS.

---

## 🛠️ Docker Compose Commands

| Command                 | Description                              |
| ----------------------- | ---------------------------------------- |
| `docker compose up`     | Start all services in the background     |
| `docker compose down`   | Stop and remove all containers/networks  |
| `docker compose ps`     | Show running services                    |
| `docker compose logs`   | View logs of all services                |
| `docker compose build`  | Build images defined in the compose file |
| `docker compose config` | Validate and view the final YAML config  |

---

## 🚀 How to Run This Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/bhuvan-raj/Docker-Compose-WordCounter.git
```
```
cd Docker-Compose-WordCounter
```


### 2️⃣ Run the Application

```bash
docker compose up -d
```

* `-d`: Run containers in the background

---

### 3️⃣ Check Running Containers

```bash
docker compose ps
```

You should see 5 services running: `redis`, `db`, `frontend`, `worker`, and `result-frontend`.

---

### 4️⃣ Open in Browser

* Input Form (Frontend): [http://localhost:5000](http://localhost:5000)
* Result Viewer: [http://localhost:7000](http://localhost:7000)

Try submitting a sentence on the input page and check the result on the result page.

---

### 5️⃣ Tear Down the Application

To stop and remove all containers, volumes, and networks:

```bash
docker compose down
```

---

## 📂 Folder Structure

```
Docker-word-counter-app/
│
├── frontend/            # Flask app to accept text input
├── worker/              # Background task for word counting
├── result-frontend/     # Flask app to display results
├── init.sql             # SQL file to create the 'results' table
├── docker-compose.yml   # Main Compose configuration
└── README.md            # This file
```

---

## 📌 Notes for Students

* All services are connected using a custom **bridge network**
* **Redis** is used to pass messages from frontend to worker
* **PostgreSQL** stores the final results
* **Docker Compose** makes starting/stopping the project easy with a single command

---

## 🧼 Cleanup

If you want to **remove everything**, including images and volumes:

```bash
docker compose down --volumes --rmi all
```

---

## 📜 License

MIT License

---

