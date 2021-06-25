--- DATABASE 생성
CREATE DATABASE django_study_database;

--- User 생성
CREATE USER django_study_user WITH PASSWORD 'password';
ALTER ROLE django_study_user SET client_encoding TO 'utf8';
ALTER ROLE django_study_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE django_study_user WITH SUPERUSER;

--- DB에 대한 User 권한 부여
GRANT ALL PRIVILEGES ON DATABASE django_study_database TO django_study_user;
