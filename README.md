## Product Python REST API

## VirtualEnv and dependencies

```bash
pipenv shell
pipenv install
```

> Dependencies will be installed from the Pipfile. Python version 3.9.6 is used for this project.

## Run the Application

```bash
pipenv run start
```

> This will start the application on port 5000

## Run the Application in Dev Mode

```bash
FLASK_ENV=development pipenv run start
```

> This will start the application on port 5000 and will reload the application on file changes.

## Deploy

```bash
FLASK_ENV=production pipenv run prod
```

> This will start the application on port 5000

## Maintainer

- Ruslan Gonzalez
- Twitter: [@ruslangonzalez](https://twitter.com/ruslangonzalez)
