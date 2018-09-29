create database edulab;
use edulab;
create table DataAnalyst_ncr(
	Job_id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
	Job_Title VARCHAR(100) NOT NULL,
	Experience VARCHAR(100) NOT NULL,
	Company_Name VARCHAR(100) NOT NULL,
	Link TEXT(21845) NOT NULL,
	Keyskills VARCHAR(100),
	Description TEXT(21845),
	Salary VARCHAR(100),
    posted_by varchar(100),
    posted_on varchar(100),
	last_updated_on TIMESTAMP NOT NULL ON UPDATE CURRENT_TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (Job_id)
);

create table location_jobs(
	Locn_id INTEGER  UNSIGNED NOT NULL AUTO_INCREMENT,
	Job_id INTEGER UNSIGNED NOT NULL,
	location VARCHAR(100) NOT NULL,
	FOREIGN KEY (Job_id) REFERENCES DataAnalyst_ncr(Job_id),
	PRIMARY KEY (Locn_id)
);

drop database edulab;

select * from DataAnalyst_ncr;