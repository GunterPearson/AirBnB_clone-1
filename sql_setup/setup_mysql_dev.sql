-- Prepares db hbnb_dev_db & user hbnb_dev (in localhost)
-- and some settings
-- TO EXECUTE THIS COMMAND:
-- cat setup_mysql_dev.sql | mysql -hlocalhost -uroot -p
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
