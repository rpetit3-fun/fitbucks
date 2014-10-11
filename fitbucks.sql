sudo -u postgres psql postgres
CREATE DATABASE fit_bucks;
CREATE USER fit_bucks_user WITH PASSWORD 'fit_bucks';
GRANT ALL PRIVILEGES ON DATABASE fit_bucks to fit_bucks_user;
\q
