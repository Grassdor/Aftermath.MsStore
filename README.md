# [MS] EVC Store

## Установка

### Краткая инструкция

#### Environment
```shell script
cp .env.example .env
```

### Локальные сборка и запуск

На проекте используется пакетный менеджер Poetry:
Для выбора версии Python 3.10 используйте `pyenv`

```
$ pip install -U pip setuptools
```
```
$ pip install poetry==1.4.2
```

Устанавливаем локально все необходимые модули:
```
poetry install
```

Запуск тестов
```
poetry run pytest
```

#### Сборка и запуск в Docker

```shell script
docker build -t "evc-ms-stores" .
docker run -dp 8000:8000 --name evc-ms-stores evc-ms-stores
```

### Если необходимо запустить внутри контейнера
перед нижеперечисленными командами добавить 
```bash
poetry run ...
```
или активировать виртуальное окружение
```bash
poetry shell
```

### Запуск линтеров
```bash
flake8
```

Рекомендуется использовать git-hook для запуска линтеров перед каждым коммитом:
```bash
pre-commit install
```

Используйте `isort` для автоматической сортировки импортов модулей, разбивая их по секциям и типам:

```bash
# From the command line:
isort file.py file2.py

# or recursively:
isort . 

# or to see the proposed changes without applying them:
isort file.py --diff
```

### Создание новой миграции БД

С автогенерацией
```shell script
alembic  revision --autogenerate -m {revision_name}
```

Без автогенерации
```shell script
alembic  revision -m {revision_name}
```

### Применение всех миграций БД

```shell script
alembic upgrade head
```
