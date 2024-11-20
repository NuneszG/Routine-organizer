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

# Docker

Docker is a tool used to create and manage project containers. It allows the project container to be copied to your machine, without having to install all the dependencies with certain versions that were used in the real project, for the application to work correctly.

### Create database image
```
docker-compose up database --build
```
### Create application image 
```
docker-compose up application --build
```

### Run application container
```
docker-compose up
``` 

If this message returns in your console, it is because the container is running correctly on the declared port.

```
database-1     | 2024-11-20 22:19:39.190 UTC [1] LOG:  database system is ready to accept connections
application-1  | Operations to perform:
application-1  |   Apply all migrations: admin, auth, contenttypes, project, sessions
application-1  | Running migrations:
application-1  |   No migrations to apply.
application-1  | Watching for file changes with StatReloader
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