#!/bin/bash

# Exporting environment variables for the development environment
export COMPRESSIO_HOST=localhost
export COMPRESSIO_USER=admin_compressio_dev
export COMPRESSIO_PASSWORD=compressio_dev
export COMPRESSIO_DB=compressio_dev
export APP_SECRET_KEY="78a0656757164b45b8341066b718dcd8"

# Constructing the database URL using the exported variables
export DATABASE_URL=mysql+mysqldb://${COMPRESSIO_USER}:${COMPRESSIO_PASSWORD}@${COMPRESSIO_HOST}:3307/${COMPRESSIO_DB}

# Confirmation message
echo "Finished Creating dev environment variables!"
