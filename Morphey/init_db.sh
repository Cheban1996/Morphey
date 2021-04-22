#!/bin/sh
set -e

psql -v ON_ERROR_STOP=1 --username "postgres" --dbname "postgres" <<-EOSQL

    CREATE USER morphey_db WITH PASSWORD 'morphey_db';
    CREATE DATABASE morphey_db;
    GRANT ALL PRIVILEGES ON DATABASE morphey_db TO morphey_db;


EOSQL
