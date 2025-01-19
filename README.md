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

### Run The API:
- API URL: http://127.0.0.1:800/text-to-image/
```
Request Body: 
	{
		"text": "A footballer kid",
		"no_of_image": 3
	}
```
```
API Output:
{
	task_ids": [
		"4782f50b-d971-4f8b-8c5d-cd7264864950",
		"76ba8aed-ca5c-4378-850f-3c75aa6dcc4e",
		"83519e52-e576-484c-9bfe-d28b9c2f7feb"
	],
	"message": "3 tasks is running parallel into background"
}
```

after runing api, what ever no_of_image will pass, that no of task will run parallel and image will be created, image_file path and title will be stored into database

### Django Admin Creds:
- URL: http://localhost:800/admin/
- Username: admin
- password: admin
