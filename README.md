# **📌 What is Docker Compose?**

Docker Compose is a tool used to **define and manage multi-container Docker applications**.
It allows you to describe all services (containers), networks, and volumes required for an application in a **single YAML file** called `docker-compose.yml`.

With one command, you can start or stop an entire application stack.

---

# **✨ Advantages of Docker Compose**

### **1. Single Command Deployment**

Start all containers using:

```
docker compose up
```

### **2. Human-Readable YAML File**

Configuration is stored in one easy-to-understand file:
`docker-compose.yml`

### **3. Automatic Network Creation**

Compose creates a dedicated network so containers can communicate using service names.

### **4. Easy Scaling**

You can scale services:

```
docker compose up --scale worker=3
```

### **5. Environment Reproducibility**

Students can pull the same code and get identical setups.

### **6. Built-in Support for Volumes**

Persistent data is handled seamlessly.

---

# **🧩 Architecture of This Project**

This Word Counter application consists of **six components**, all connected to a single custom network (`wc-net`):

```
 ┌────────────────┐      ┌──────────────┐      ┌─────────────────┐
 │ Input Frontend │ ---> │    Redis      │ ---> │     Worker       │
 └───────┬────────┘      └──────────────┘      └───────┬─────────┘
         │                                             │
         ▼                                             ▼
 ┌────────────────┐                           ┌──────────────────┐
 │ Results Front. │ <------------------------ │   PostgreSQL      │
 └────────────────┘                           └──────────────────┘
```

### **Components**

| Component            | Role                                                      |
| -------------------- | --------------------------------------------------------- |
| **Input Frontend**   | Accepts user text and pushes jobs to Redis                |
| **Redis**            | Message queue storing pending word-count jobs             |
| **Worker**           | Reads jobs from Redis, counts words, stores results in DB |
| **PostgreSQL**       | Stores processed results persistently                     |
| **Results Frontend** | Displays the latest word counts                           |
| **wc-net**           | Custom Docker bridge network connecting all components    |

---

# **📁 Project Structure**

```
word-counter/
├── docker-compose.yml
├── input-frontend/
│   ├── Dockerfile
│   ├── app.py
│   └── templates/index.html
├── results-frontend/
│   ├── Dockerfile
│   ├── app.py
│   └── templates/results.html
├── worker/
│   ├── Dockerfile
│   └── worker.py
└── db/
    └── init.sql
```

---

# **🔧 Main Docker Compose Commands**

### **Start all services**

```
docker compose up
```

### **Start with rebuild**

```
docker compose up --build
```

### **Run in background**

```
docker compose up -d
```

### **Stop all services**

```
docker compose down
```

### **View logs of all containers**

```
docker compose logs -f
```

### **View logs of a specific service**

```
docker compose logs <service-name>
```

Example:

```
docker compose logs worker
```

### **Check running containers**

```
docker ps
```

### **Destroy containers + volumes**

```
docker compose down -v
```

---

# **🧪 Lab Exercise – Run the Word Counter Application**

### **Step 1: Clone or download the project**

```
git clone <repo-url>
cd word-counter
```

### **Step 2: Build and start the application**

```
docker compose up --build
```

### **Step 3: Access the frontends**

| Service              | URL                                            |
| -------------------- | ---------------------------------------------- |
| **Input Frontend**   | [http://localhost:5000](http://localhost:5000) |
| **Results Frontend** | [http://localhost:5001](http://localhost:5001) |

### **Step 4: Test the application**

1. Open the **Input Frontend**
2. Type any text
3. Press **Submit**
4. Open **Results Frontend**
5. View the processed word count

### **Step 5: Stop the application**

```
docker compose down
```

---

# **🎯 Learning Outcomes**

By completing this lab, students will understand:

* How Docker Compose orchestrates multiple containers
* How microservices communicate using a custom bridge network
* How Redis acts as a message queue
* How workers process background jobs
* How to connect frontend services to backend services
* How to persist data using PostgreSQL volumes
* How Compose simplifies multi-container setups

---
