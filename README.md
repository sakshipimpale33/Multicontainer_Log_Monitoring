#  Docker Multi-Container Logging with Loki, Grafana & Promtail

##  Overview

We've built a powerful multi-container logging system using **Docker**, **Loki**, **Promtail**, and **Grafana** to collect, store, and visualize logs from multiple running applications. This setup enables real-time monitoring and efficient log management in containerized environments.

<img src="https://blog.cavelab.dev/2022/08/collecting-logs-with-loki-and-promtail/cover.png" alt="Grafana Logo" width="200" align="center"/>

##  Components

### Application Containers

- **Flask API (Python)** running on port **5000**
- **Node.js API** running on port **4000**
- Both APIs generate logs upon receiving requests

### Logging Infrastructure

- **Loki**: Collects and stores logs from all containers
- **Promtail**: Forwards container logs to Loki
- **Grafana**: Provides a dashboard for searching and visualizing logs

---

##  How It Works

### 1️⃣ Container Logging

- Each container (Flask & Node.js) generates logs, including:
  - API calls
  - Startup messages
  - Errors and exceptions

### 2️⃣ Log Collection with Promtail

- Docker captures logs from standard output
- **Promtail** forwards logs to Loki efficiently

### 3️⃣ Log Querying

- Grafana connects to Loki as a data source
- Logs can be queried using Loki’s query language:
  ```
  {container_name=~".flask-api.|.node-api."}
  ```
- Filters can be applied by container name, timestamp, or log content

### 4️⃣ Monitoring in Grafana

- View real-time logs in an interactive dashboard
- Apply filters for specific services, timeframes, and log types
- Gain deep insights into system health and application performance

---

##  Benefits

✅ **Centralized Logging**: No more scattered logs across containers—everything is in one place.  
✅ **Easy Troubleshooting**: Search logs across multiple services for quick issue resolution.  
✅ **Real-Time Monitoring**: See application activity and errors as they happen.  
✅ **No Log File Hassle**: Automated log storage and rotation handled by Loki.  
✅ **Scalability**: Works efficiently as more containers and services are added.

---

##  Enhancing with OpenTelemetry (Future Scope)

To take observability to the next level, we can integrate **OpenTelemetry** to include:

- **Traces**: Monitor request flows across distributed services
- **Metrics**: Track performance indicators like response times
- **Logs**: Correlate logs with traces for deeper debugging

### 📊 Output

Here are sample outputs from our logging setup:

<img src="images/1.png" alt="containers" width="600"/>

<img src="images/2.png" alt="Logs" width="600"/>

<img src="images/3.png" alt="Logs" width="600"/>

### How OpenTelemetry Adds Value

🔹 **Full Request Visibility**: Track API calls across multiple services.  
🔹 **Root Cause Analysis**: Identify exactly where issues originate.  
🔹 **Performance Bottleneck Detection**: Pinpoint slow queries or endpoints.

In the future, we will integrate **Jaeger** for traces and **Prometheus** for metrics collection to further enhance monitoring:

- **Jaeger**: Used to collect and store distributed traces, allowing us to visualize the flow of requests across services and pinpoint performance bottlenecks.
- **Prometheus**: Will track metrics such as response times, error rates, and system resource utilization, enabling better monitoring of service health and performance.


---

## Prerequisites

- **Docker**
- **Docker Compose**

## Steps

```bash
1️⃣ Clone the repository:
git clone https://github.com/sakshipimpale33/Multicontainer_Log_Monitoring.git
cd Multicontainer_Log_Monitoring

2️⃣ Start the multi-container setup:
docker-compose up -d

3️⃣ Access Grafana at: http://localhost:3000

Default credentials: admin / admin

4️⃣ Stop the setup:
docker-compose down
```

---

## 📂 Folder Structure

```
📁 Multicontainer_Log_Monitoring
├── 📁 flask-api                 # Python API (Flask)
│   ├── Dockerfile
│   ├── app.py
│   ├── requirements.txt
├── 📁 node-api                  # Node.js API
│   ├── Dockerfile
│   ├── package.json
│   ├── package-lock.json
│   ├── server.js
├── 📁 grafana-provisioning       # Grafana Configuration
│   ├── datasources
│   │   ├── loki.yml
├── 📁 loki                      # Loki Configuration
├── 📁 otel-collector             # OpenTelemetry Collector
│   ├── otel-config.yaml
├── 📝 promtail-config.yml        # Promtail Configuration
├── 📝 docker-compose.yml         # Multi-container setup
└── 📝 README.md                  # Project documentation
```

---

