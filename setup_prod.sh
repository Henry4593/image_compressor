#!/bin/bash

# Exporting environment variables for the development environment
export COMPRESSIO_HOST=localhost
export COMPRESSIO_USER=admin_compressio
export COMPRESSIO_PASSWORD=compressio
export COMPRESSIO_DB=compressio

# Constructing the database URL using the exported variables
export DATABASE_URL=mysql+mysqldb://${COMPRESSIO_USER}:${COMPRESSIO_PASSWORD}@${COMPRESSIO_HOST}:3306/${COMPRESSIO_DB}

# Confirmation message
echo "Finished Creating dev environment variables!"
