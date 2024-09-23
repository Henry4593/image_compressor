-- Create the database if it does not exist
CREATE DATABASE IF NOT EXISTS compressio;

-- Drop the user if it exists (optional, but ensures no conflict)
DROP USER IF EXISTS 'admin_compressio'@'localhost';

-- Create the user
CREATE USER 'admin_compressio'@'localhost' IDENTIFIED BY 'compressio';

-- Grant all privileges on the database to the user
GRANT ALL PRIVILEGES ON compressio.* TO 'admin_compressio'@'localhost';

-- Grant SELECT privileges on performance_schema
GRANT SELECT ON performance_schema.* TO 'admin_compressio'@'localhost';

-- Flush privileges to ensure all changes take effect
FLUSH PRIVILEGES;