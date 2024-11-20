# Routine organizer

The routine organizer is a website with a crud system for tasks. Made by me, with the objective of being able to better organize my daily tasks, in which I can create tasks with a title and content with separate functions, which is a timer and an alarm clock for certain tasks.

<img src="assets/images/Captura de ecrã 2024-11-20 153834.png" style="width: 400px"> 

### Features
- Schedule your daily activities by adding tasks
- Each task has a timer and alarm to help you, or alert you when necessary
- Update or delete your completed tasks

### Technologies used
- Python
- Django
- PostgreSQL
- JavaScript
- Docker
- Make

<div style="display: grid; grid-template-columns: repeat(2, 400px); gap: 10px;">
  <img src="assets/images/Captura de ecrã 2024-11-20 153844.png" style="width: 400px">
  <img src="assets/images/Captura de ecrã 2024-11-20 153902.png" style="width: 400px">
  <img src="assets/images/Captura de ecrã 2024-11-20 153916.png" style="width: 400px">
  <img src="assets/images/Captura de ecrã 2024-11-20 154747.png" style="width: 400px">
</div>

### Clone repository
```
https://github.com/NuneszG/Routine-organizer.git
```

### Virtual space 
```
Linux or MacOS
source venv/bin/activate

Windows
./venv/Scripts/activate
```

### Docker
```
docker-compose up database --build
```
```
docker-compose up application --build
```

### Run application container
```
docker-compose up
``` 

### Run application with Makefile 
```
Make run
```

### Run application 
```
Makefile
Make run

Without makefile
python manage.py runserver
```

### Access application in the Browser
```
http://localhost:8000
```