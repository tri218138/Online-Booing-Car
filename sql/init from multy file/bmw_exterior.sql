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
-- Table structure for table `exterior`
--

DROP TABLE IF EXISTS `exterior`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `exterior` (
  `exterior_ID` int unsigned NOT NULL AUTO_INCREMENT,
  `exterior_type` varchar(6) DEFAULT NULL COMMENT 'domain:{wheel, color}',
  `color_type` varchar(12) DEFAULT NULL,
  `wheel_desc` varchar(24) DEFAULT NULL,
  `wheel_range` varchar(12) DEFAULT NULL,
  PRIMARY KEY (`exterior_ID`),
  UNIQUE KEY `exterior_ID` (`exterior_ID`),
  CONSTRAINT `exterior_ibfk_1` FOREIGN KEY (`exterior_ID`) REFERENCES `component` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exterior`
--

LOCK TABLES `exterior` WRITE;
/*!40000 ALTER TABLE `exterior` DISABLE KEYS */;
INSERT INTO `exterior` VALUES (1,'color','non-metallic',NULL,NULL),(2,'color','metallic',NULL,NULL),(3,'color','metallic',NULL,NULL),(4,'color','metallic',NULL,NULL),(5,'color','metallic',NULL,NULL),(6,'color','metallic',NULL,NULL),(7,'wheels',NULL,'Performance Non Run-flat','Range 305 mi'),(8,'wheels',NULL,'All-season',NULL),(9,'wheels',NULL,NULL,NULL),(17,'color','non-metallic',NULL,NULL),(18,'color','metallic',NULL,NULL),(19,'color','metallic',NULL,NULL),(20,'color','metallic',NULL,NULL),(21,'color','metallic',NULL,NULL),(22,'color','metallic',NULL,NULL),(23,'color','metallic',NULL,NULL),(24,'wheels',NULL,'Performance Non Run-flat','Range 310 mi'),(25,'wheels',NULL,'Performance Non Run-flat','Range 310 mi');
/*!40000 ALTER TABLE `exterior` ENABLE KEYS */;
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
