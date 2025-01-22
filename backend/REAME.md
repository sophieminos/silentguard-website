# Instructions

### run app
```bash
python3 app.py
```

### build Docker image
```bash
docker build --platform linux/amd64 -t sophieminos/silentguard-backend:latest .
```

### push Docker image to hub
```bash
docker push sophieminos/silentguard-backend:latest
```