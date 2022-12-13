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
-- Table structure for table `order`
--

DROP TABLE IF EXISTS `order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order` (
  `Code` varchar(20) NOT NULL,
  `totalprice` double NOT NULL,
  `shippingAddress` varchar(100) NOT NULL,
  `paymentMethod` char(100) NOT NULL,
  `cusID` int unsigned NOT NULL,
  `orderDate` date NOT NULL,
  `BA_ID` int unsigned NOT NULL,
  PRIMARY KEY (`Code`),
  KEY `order_cusid_foreign` (`cusID`),
  KEY `order_ba_id_foreign` (`BA_ID`),
  CONSTRAINT `order_ba_id_foreign` FOREIGN KEY (`BA_ID`) REFERENCES `employee` (`id`),
  CONSTRAINT `order_cusid_foreign` FOREIGN KEY (`cusID`) REFERENCES `customer` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order`
--

LOCK TABLES `order` WRITE;
/*!40000 ALTER TABLE `order` DISABLE KEYS */;
INSERT INTO `order` VALUES ('C01',75,'44 Riverside Street','full',1,'2021-03-03',2),('C02',80,'3827 John Wall Pass','partial',2,'2021-04-03',2),('C03',85,'8 Melody Avenue','full',3,'2021-05-02',2),('C04',76,'3079 Bayside Alley','partial',4,'2021-11-08',2),('C05',77.55,'2 Green Ridge Street','full',5,'2021-12-07',1),('C06',90,'13 Glacier Hill Court','partial',6,'2021-01-01',1),('C07',200,'5218 Knutson Hill','full',7,'2022-09-02',1),('C08',50,'55 Hansons Pass','partial',8,'2022-01-07',1);
/*!40000 ALTER TABLE `order` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-13  9:28:15
