## setup testcase for TC06
plese check [design slide](https://docs.google.com/presentation/d/1T-oVlVRT6dkG9qvErxL3lXZNHZ9Og9wEdlvx86Pk8Mc/edit?usp=sharing)

```sh
$sh setup.sh
```

## run apps
```sh
$docker-compose up -d
```

## docker-compose.yml
```yml
version: '3.5'
services:
  db1:
    image: postgres:14.1-alpine
    restart: always
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    volumes:
       - data1:/var/lib/posgresql/data
    ports:
      - "15432:5432"
  db2:
    image: postgres:14.1-alpine
    restart: always
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    volumes:
       - data2:/var/lib/posgresql/data
    ports:
      - "25432:5432"
  
  app1:
    build:
      context: ./app1
    ports:
      - "18000:8000"
    volumes:
      - ./app1/code:/code
    command: python manage.py runserver 0.0.0.0:8000
    depends_on:
      - db1

  app2:
    build:
      context: ./app2
    ports:
      - "28000:8000"
    volumes:
      - ./app2/code:/code
    command: python manage.py runserver 0.0.0.0:8000
    depends_on:
      - db2

volumes:
    data1:
    data2:
```
