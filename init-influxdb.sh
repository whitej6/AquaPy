#!/bin/bash
set -e

INFLUX_CMD="influx -host 127.0.0.1 -port 8086 -username ${INFLUXDB_ADMIN_USER} -password ${INFLUXDB_ADMIN_PASSWORD} -execute "

$INFLUX_CMD "CREATE USER \"$INFLUXDB_ADMIN_USER\" WITH PASSWORD '$INFLUXDB_ADMIN_PASSWORD' WITH ALL PRIVILEGES"
$INFLUX_CMD "CREATE DATABASE $INFLUXDB_DB"

$INFLUX_CMD "CREATE USER \"$INFLUXDB_USER\" WITH PASSWORD '$INFLUXDB_USER_PASSWORD'"
$INFLUX_CMD "REVOKE ALL PRIVILEGES FROM \"$INFLUXDB_USER\""
$INFLUX_CMD "GRANT ALL ON \"$INFLUXDB_DB\" TO \"$INFLUXDB_USER\""