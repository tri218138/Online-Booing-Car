-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: bmw
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `address` varchar(100) DEFAULT NULL,
  `phonenumber` varchar(20) DEFAULT NULL,
  `name` varchar(20) NOT NULL,
  `BA_ID` int unsigned NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `customer_ba_id_foreign` (`BA_ID`),
  CONSTRAINT `customer_ba_id_foreign` FOREIGN KEY (`BA_ID`) REFERENCES `employee` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1,'44 Riverside Street','+86-222-233-4768','Juana Bonhomme',2),(2,'3827 John Wall Pass','+62-997-119-7586','Agnella Ferretti',2),(3,'8 Melody Avenue','+389-669-940-9891','Erny Clancy',2),(4,'3079 Bayside Alley','+230-223-720-8568','Alfie Olohan',2),(5,'2 Green Ridge Street','+86-385-503-5650','Maxim Ketteringham',1),(6,'13 Glacier Hill Court','+33-375-609-8862','Milicent Ure',1),(7,'5218 Knutson Hill','+62-744-990-0379','Ellette Itzik',1),(8,'55 Hansons Pass','+55-633-583-2927','Sissie Prettyjohns',1),(9,'24 Riverside Street','+86-222-233-4768','Christine',2),(10,'327 John Wall Pass','+86-232-233-4788','Susan',2),(11,'18 Melody Avenue','+86-272-533-4768','Margaret',2),(12,'3029 Bayside Alley','+86-227-233-4764','Judith',2),(13,'12 Green Ridge Street','+86-922-293-4728','Jennifer',2),(14,'16 Glacier Hill Court','+86-242-293-4968','Mary',2),(15,'518 Knutson Hill','+86-212-233-5672','Elizabeth',1),(16,'555 Hansons Pass','+86-222-233-4768','Patricia',1),(17,'24 Riverside Street','+86-232-233-4788','Linda',1),(18,'327 John Wall Pass','+86-272-533-4768','Barbara',2),(19,'18 Melody Avenue','+86-227-233-4764','Lynette',1),(20,'3029 Bayside Alley','+86-922-293-4728','Robyn',1),(21,'12 Green Ridge Street','+86-242-293-4968','Anne',2),(22,'24 Riverside Street','+86-212-233-5672','Karen',2),(23,'327 John Wall Pass','+86-222-233-4768','Helen',2),(24,'18 Melody Avenue','+86-232-233-4788','Diane',1),(25,'25 Riverside Street','+86-272-533-4768','Sandra',1),(26,'328 John Wall Pass','+86-227-233-4764','Wendy',1),(27,'19 Melody Avenue','+86-222-233-4768','Janet',1),(28,'25 Riverside Street','+86-232-233-4788','Heather',2),(29,'328 John Wall Pass','+86-272-533-4768','Pamela',2),(30,'19 Melody Avenue','+86-227-233-4764','Carol',2),(31,'3030 Bayside Alley','+86-922-293-4728','Janice',2),(32,'13 Green Ridge Street','+86-242-293-4968','Julie',1),(33,'17 Glacier Hill Court','+86-212-233-5672','Suzanne',2),(34,'519 Knutson Hill','+86-222-233-4768','Lorraine',1),(35,'556 Hansons Pass','+86-232-233-4785','Dianne',2),(36,'25 Riverside Street','+86-272-533-4768','Marilyn',2),(37,'328 John Wall Pass','+86-227-233-4764','Rosemary',1),(38,'19 Melody Avenue','+86-922-293-4728','Raewyn',2),(39,'3030 Bayside Alley','+86-242-293-4268','Kathleen',1),(40,'13 Green Ridge Street','+86-212-233-5672','Pauline',1),(41,'25 Riverside Street','+86-222-233-4778','Alison',2),(42,'328 John Wall Pass','+86-232-233-4788','Gail',1),(43,'19 Melody Avenue','+86-272-533-4768','Denise',1),(44,'26 Riverside Street','+86-227-233-4764','Sharon',1),(45,'329 John Wall Pass','+86-222-233-4768','Lesley',2),(46,'20 Melody Avenue','+86-232-533-4788','Yvonne',1),(47,'26 Riverside Street','+86-272-433-4768','Catherine',2),(48,'329 John Wall Pass','+86-227-333-4764','Shirley',2),(49,'20 Melody Avenue','+86-922-293-4728','Beverley',2),(50,'3031 Bayside Alley','+86-242-193-4968','Maureen',1);
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-13  9:28:14
