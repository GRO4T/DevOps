#!/bin/bash
# Utility script for creating database users with access to a designated schema.

echo -n "Username: "
read -r username

echo -n "Password: "
read -r password

schema_name="$username"

psql "postgres://$DB_USER:$DB_PASS@$DB_HOST/$DB_NAME" << EOF
CREATE SCHEMA $schema_name;
CREATE USER $username LOGIN PASSWORD '$password';
ALTER ROLE $username SET search_path TO $schema_name, public;
GRANT ALL ON SCHEMA $schema_name TO $username;
EOF

