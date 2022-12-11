-- Active: 1670147479576@@127.0.0.1@3306@bwm
DROP DATABASE IF EXISTS `BWM`;
CREATE DATABASE `BWM`;
USE `BWM`;

CREATE TABLE `Customer`(
    `id` INT UNSIGNED NOT NULL UNIQUE AUTO_INCREMENT,
    `address` VARCHAR(100) NULL,
    `phonenumber` VARCHAR(20) NULL,
    `name` VARCHAR(20) NOT NULL,
    `BA_ID` INT UNSIGNED NOT NULL
);
ALTER TABLE
    `Customer` ADD PRIMARY KEY `customer_id_primary`(`id`);
CREATE TABLE `CusAccount`(
    `username` VARCHAR(100) NOT NULL,
    `password` VARCHAR(100) NOT NULL,
    `cusID` INT UNSIGNED NOT NULL,
    PRIMARY KEY (`username`)
);
CREATE TABLE `Order`(
    `Code` VARCHAR(20) NOT NULL,
    `totalprice` DOUBLE NOT NULL,
    `shippingAddress` VARCHAR(100) NOT NULL,
    `paymentMethod` CHAR(100) NOT NULL, -- domain: {full,partial} 
    `cusID` INT UNSIGNED NOT NULL,
    `orderDate` DATE NOT NULL,
    `BA_ID` INT UNSIGNED NOT NULL
);
ALTER TABLE
    `Order` ADD PRIMARY KEY `order_code_primary`(`Code`);
CREATE TABLE `Employee`(
    `id` INT UNSIGNED NOT NULL UNIQUE AUTO_INCREMENT,
    `Name` VARCHAR(20) NOT NULL,
    `salary` DOUBLE NULL,
    `SSN` INT NOT NULL,
    `typejob` VARCHAR(20) NULL, -- domain: {Leader,BA,Worker,Manger,Designer,null} 
    `languageSkill` VARCHAR(30) NULL,
    `technicalSkill` VARCHAR(30) NULL,
    `manageSkill` VARCHAR(30) NULL,
    `memID` INT NULL
);
ALTER TABLE
    `Employee` ADD PRIMARY KEY `employee_id_primary`(`id`);
ALTER TABLE
    `Employee` ADD UNIQUE `employee_ssn_unique`(`SSN`);
CREATE TABLE `Project`(
    `id` INT UNSIGNED NOT NULL UNIQUE AUTO_INCREMENT,
    `description` VARCHAR(255) NOT NULL,
    `leaderID` INT UNSIGNED NULL
);
ALTER TABLE
    `Project` ADD PRIMARY KEY `project_id_primary`(`id`);
CREATE TABLE `Group`(
    `id` INT UNSIGNED NOT NULL UNIQUE AUTO_INCREMENT,
    `name` VARCHAR(20) NOT NULL
);
ALTER TABLE
    `Group` ADD PRIMARY KEY `group_id_primary`(`id`);
CREATE TABLE `Car`( 
    `id` INT UNSIGNED NOT NULL UNIQUE AUTO_INCREMENT,
    `model_name` VARCHAR(5) NOT NULL,
    `series_name` VARCHAR(100) NOT NULL,
    `title` VARCHAR(255) NOT NULL,
    `starting_msrp` DOUBLE UNSIGNED NOT NULL,
    `shown_msrp` DOUBLE UNSIGNED NULL,
    `mass` DOUBLE UNSIGNED NOT NULL,
    `color` VARCHAR(20) NOT NULL,
    `img_url` VARCHAR(1000) NOT NULL,
    `wallpaper` VARCHAR(1000) NOT NULL,
    `branch` VARCHAR(20) NOT NULL,
    `year` YEAR NOT NULL,
    `proID` INT UNSIGNED NOT NULL,
    `startDate` DATE NOT NULL,
    `progress` VARCHAR(20) NOT NULL, -- domain:{to do; in progress, complete} 
    `blueprintID` INT UNSIGNED NOT NULL
);
ALTER TABLE
    `Car` ADD PRIMARY KEY `car_id_primary`(`id`);
    
CREATE TABLE `faq` (
	`carid` INT UNSIGNED NOT NULL,
    `question` VARCHAR(255) NOT NULL,
    `answer` VARCHAR(500) NOT NULL,
    PRIMARY KEY(`carid`,`question`,`answer`),
    FOREIGN KEY(`carid`) REFERENCES `Car`(`id`)
);

CREATE TABLE `Blueprint`(
    `id` INT UNSIGNED NOT NULL UNIQUE AUTO_INCREMENT,
    `url` VARCHAR(255) NOT NULL,
    `name` VARCHAR(20) NOT NULL
);
ALTER TABLE
    `Blueprint` ADD PRIMARY KEY `blueprint_id_primary`(`id`);
    
CREATE TABLE `Design_bp`(
    `desID` INT UNSIGNED NOT NULL UNIQUE AUTO_INCREMENT,
    `blueprintID` INT UNSIGNED NOT NULL
);
ALTER TABLE
    `Design_bp` ADD PRIMARY KEY `design_bp_desid_blueprintid_primary`(`desID`, `blueprintID`);

CREATE TABLE `Component`(
    `id` INT UNSIGNED NOT NULL UNIQUE AUTO_INCREMENT,
    `type` VARCHAR(20) NOT NULL, -- domain: {machine;interior,exterior,null} 
    `name` VARCHAR(20) NOT NULL,
    `img_url` VARCHAR(255) NOT NULL,
    `price` DOUBLE NOT NULL,
    `carID` INT UNSIGNED NOT NULL,
    `supID` INT UNSIGNED NULL,
    `suppliedDate` DATE NULL
);
ALTER TABLE
    `Component` ADD PRIMARY KEY `component_id_primary`(`id`);
    
CREATE TABLE `Interior`(
    `interiorid` INT UNSIGNED NOT NULL UNIQUE AUTO_INCREMENT,
    `interiorType` VARCHAR(20) NULL COMMENT '{upholstery, trim}',
	`upholstery_type` VARCHAR(50) NULL
);
ALTER TABLE
    `Interior` ADD PRIMARY KEY `interior_interiorid_primary`(`interiorid`);
CREATE TABLE `Exterior`(
    `exteriorID` INT UNSIGNED NOT NULL UNIQUE AUTO_INCREMENT,
    `exteriorType` VARCHAR(20) NULL COMMENT 'domain:{wheel, color}',
	`color_type` VARCHAR(50) NULL,
	`wheel_desc` VARCHAR(50) NULL,
	`wheel_range` VARCHAR(50) NULL
);
ALTER TABLE
    `Exterior` ADD PRIMARY KEY `exterior_exteriorid_primary`(`exteriorID`);



-- 
CREATE TABLE `Automatic_equippment`(
    `id` INT UNSIGNED NOT NULL UNIQUE AUTO_INCREMENT,
    `type` VARCHAR(20) NOT NULL,
    `location` VARCHAR(100) NOT NULL,
    `maID` INT UNSIGNED NOT NULL,
    `compID` INT UNSIGNED NULL
);
ALTER TABLE
    `Automatic_equippment` ADD PRIMARY KEY `automatic_equippment_id_primary`(`id`);
CREATE TABLE `eq_notify_ma`(
    `maID` INT UNSIGNED NOT NULL,
    `eqID` INT UNSIGNED NOT NULL
);
ALTER TABLE
    `eq_notify_ma` ADD PRIMARY KEY `eq_notify_ma_eqid_primary`(`eqID`);
CREATE TABLE `notify_message`(
    `edID` INT UNSIGNED NOT NULL UNIQUE AUTO_INCREMENT,
    `status` VARCHAR(20) NOT NULL, -- domain: {overheating; repairing; normal,null} 
    `datetime` DATETIME NOT NULL
);
ALTER TABLE
    `notify_message` ADD PRIMARY KEY `notify_message_status_datetime_edid_primary`(`status`, `datetime`, `edID`);
CREATE TABLE `Account`(
    `username` VARCHAR(100) NOT NULL,
    `password` VARCHAR(100) NOT NULL,
    `empID` INT UNSIGNED NULL
);
ALTER TABLE
    `Account` ADD PRIMARY KEY `account_username_primary`(`username`);
CREATE TABLE `Task`(
    `name` VARCHAR(20) NOT NULL,
    `details` VARCHAR(255) NOT NULL,
    `proID` INT UNSIGNED NULL,
    `groupID` INT UNSIGNED NULL,
    `leaderID` INT UNSIGNED NULL
);
ALTER TABLE
    `Task` ADD PRIMARY KEY `task_name_proid_groupid_primary`(`name`, `proID`, `groupID`);
CREATE TABLE `supplier`(
    `id` INT UNSIGNED NOT NULL UNIQUE AUTO_INCREMENT,
    `bank_account` VARCHAR(50) NULL,
    `address` VARCHAR(100) NOT NULL,
    `name` VARCHAR(20) NOT NULL,
    `taxcode` VARCHAR(20) NULL,
    `memID` INT UNSIGNED NULL
);
ALTER TABLE
    `supplier` ADD PRIMARY KEY `supplier_id_primary`(`id`);
CREATE TABLE `performanceLog`(
    `datatime` INT UNSIGNED NOT NULL UNIQUE AUTO_INCREMENT,
    `speed` DOUBLE NOT NULL,
    `temperature` DOUBLE NOT NULL,
    `eqID` INT UNSIGNED NOT NULL
);
ALTER TABLE
    `performanceLog` ADD PRIMARY KEY `performancelog_datatime_speed_temperature_eqid_primary`(
        `datatime`,
        `speed`,
        `temperature`,
        `eqID`
    );
ALTER TABLE
    `Order` ADD CONSTRAINT `order_cusid_foreign` FOREIGN KEY(`cusID`) REFERENCES `Customer`(`id`);
ALTER TABLE
    `Order` ADD CONSTRAINT `order_ba_id_foreign` FOREIGN KEY(`BA_ID`) REFERENCES `Employee`(`id`);
ALTER TABLE
    `Project` ADD CONSTRAINT `project_leaderid_foreign` FOREIGN KEY(`leaderID`) REFERENCES `Employee`(`id`);
ALTER TABLE
    `Customer` ADD CONSTRAINT `customer_ba_id_foreign` FOREIGN KEY(`BA_ID`) REFERENCES `Employee`(`id`);
ALTER TABLE
    `Car` ADD CONSTRAINT `car_proid_foreign` FOREIGN KEY(`proID`) REFERENCES `Project`(`id`);
ALTER TABLE
    `Component` ADD CONSTRAINT `component_carid_foreign` FOREIGN KEY(`carID`) REFERENCES `Car`(`id`);
ALTER TABLE
    `Component` ADD CONSTRAINT `component_supid_foreign` FOREIGN KEY(`supID`) REFERENCES `supplier`(`id`);

ALTER TABLE
	`Interior` ADD FOREIGN KEY(`interiorID`) REFERENCES `Component`(`id`);
ALTER TABLE
	`Exterior` ADD FOREIGN KEY(`exteriorID`) REFERENCES `Component`(`id`);
ALTER TABLE
    `Automatic_equippment` ADD CONSTRAINT `automatic_equippment_compid_foreign` FOREIGN KEY(`compID`) REFERENCES `Component`(`id`);
ALTER TABLE
    `eq_notify_ma` ADD CONSTRAINT `eq_notify_ma_maid_foreign` FOREIGN KEY(`maID`) REFERENCES `Employee`(`id`);
ALTER TABLE
    `Account` ADD CONSTRAINT `account_empid_foreign` FOREIGN KEY(`empID`) REFERENCES `Employee`(`id`);
ALTER TABLE
    `CusAccount` ADD CONSTRAINT `cusaccount_cusid_foreign` FOREIGN KEY(`cusID`) REFERENCES `Customer`(`id`);
ALTER TABLE
    `Task` ADD CONSTRAINT `task_proid_foreign` FOREIGN KEY(`proID`) REFERENCES `Project`(`id`);
ALTER TABLE
    `Task` ADD CONSTRAINT `task_groupid_foreign` FOREIGN KEY(`groupID`) REFERENCES `Group`(`id`);
ALTER TABLE
    `Task` ADD CONSTRAINT `task_leaderid_foreign` FOREIGN KEY(`leaderID`) REFERENCES `Employee`(`id`);
ALTER TABLE
    `performanceLog` ADD CONSTRAINT `performancelog_eqid_foreign` FOREIGN KEY(`eqID`) REFERENCES `Automatic_equippment`(`id`);
ALTER TABLE
    `Design_bp` ADD CONSTRAINT `design_bp_desid_foreign` FOREIGN KEY(`desID`) REFERENCES `Employee`(`id`);
ALTER TABLE
    `Design_bp` ADD CONSTRAINT `design_bp_blueprintid_foreign` FOREIGN KEY(`blueprintID`) REFERENCES `Blueprint`(`id`);
ALTER TABLE
    `Car` ADD CONSTRAINT `car_blueprintid_foreign` FOREIGN KEY(`blueprintID`) REFERENCES `Blueprint`(`id`);