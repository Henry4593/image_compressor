-- Create the database if it does not exist
CREATE DATABASE IF NOT EXISTS compressio_dev;

-- Drop the user if it exists (optional, but ensures no conflict)
DROP USER IF EXISTS 'admin_compressio_dev'@'localhost';

-- Create the user
CREATE USER 'admin_compressio_dev'@'localhost' IDENTIFIED BY 'compressio_dev';

-- Grant all privileges on the database to the user
GRANT ALL PRIVILEGES ON compressio_dev.* TO 'admin_compressio_dev'@'localhost';

-- Grant SELECT privileges on performance_schema
GRANT SELECT ON performance_schema.* TO 'admin_compressio_dev'@'localhost';

-- Flush privileges to ensure all changes take effect
FLUSH PRIVILEGES;