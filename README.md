# Chaotix_Assignment Setup

### Required Tools:
    • Docker version 27.1.1
    • docker-compose version 1.29.2
    • Python 3.10.12

### Clone the Repo and Go to 
```bash
git clone https://github.com/Shoony0/Chaotix_Assignment.git
cd Chaotix_Assignment
```

### Setup the Django, Redis, and Celery Server
```bash
docker compose -f docker-compose.yml up --build --force-recreate --remove-orphans
```

### API Root URL:
- http://localhost:800/