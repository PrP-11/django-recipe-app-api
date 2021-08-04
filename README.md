# django-recipe-app-api
Production grade django backend API project using postgres, docker and TDD style development.


# Docker Build
`docker build .`

# Docker Compose
`docker-compose build`

# Setup Django
`docker-compose run app sh -c "django-admin.py startproject app ."`

# Run tests
`docker-compose run app sh -c  "python manage.py test"`

# Run tests (with linting)
`docker-compose run app sh -c  "python manage.py test && flake8"`

# Setup core app
`docker-compose run app sh -c  "python manage.py startapp core"`

# Setup core migrations for db
`docker-compose run app sh -c "python manage.py makemigrations core"`