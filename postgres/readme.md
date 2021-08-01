**Postgresql 설치**
---
* django interpreter 설정(env환경)
* pip install psycopg2-binary
* DATABASE 생성(Docker로 하는 방법만 정리 그외 설정은 나중에 ..)
```python
=== docker container 생성 ===
#!/usr/bin/env bash
container_name=django_study_postgres
docker rm -f $(docker ps -a | grep $container_name | awk "{print \$1}" )
docker run -itd -p 55432:5432 --name $container_name -e POSTGRES_PASSWORD=password --restart unless-stopped postgres:13
```
```python
=== docker로 생성한 container에 접속 ===
#!/usr/bin/env bash

container_name=django_study_postgres
docker exec -it $container_name /bin/bash

# 접속후 psql 접속은
# su postgres
# psql
```

* Settings에서 DB 설정 바꾸기

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_name',
        'USER': 'db_user',
        'PASSWORD': 'db_user_password',
        'HOST': 'your server ip',
        'PORT': 'your db port',
    }
}
```

**Postgresql 커맨드**
---
명령어들은 소문자로 사용하기(보기쉽게 대문자로 정리)
* **\L** : 데이터베이스 목록 보기

* **\C db_name** : DB변경  
   
* **\DU** : 유저 권한 확인

* **\DT** : 현재 접속한 DB의 테이블 리스트 보기

* **\D table_name** : 특정 테이블 조회

* **\TIMING** : Query 실행 시간 표시(On/Off 기능)

* **\I** : 외부 쿼리파일 실행시 쓰는 명령어(Timing으로 쿼리 테스트 할때 쓰면 좋을듯)
---