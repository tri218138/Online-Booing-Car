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
-- Table structure for table `blueprint`
--

DROP TABLE IF EXISTS `blueprint`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `blueprint` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `url` varchar(255) NOT NULL,
  `name` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blueprint`
--

LOCK TABLES `blueprint` WRITE;
/*!40000 ALTER TABLE `blueprint` DISABLE KEYS */;
INSERT INTO `blueprint` VALUES (1,'http://dummyimage.com/250x250.png/ff4444/ffffff','BLP1'),(2,'http://dummyimage.com/250x250.png/ff4444/ffffff','BLP2'),(3,'http://dummyimage.com/250x250.png/ff4444/ffffff','BLP3'),(4,'http://dummyimage.com/250x250.png/ff4444/ffffff','BLP4'),(5,'http://dummyimage.com/250x250.png/ff4444/ffffff','BLP5'),(6,'http://dummyimage.com/250x250.png/ff4444/ffffff','BLP6'),(7,'http://dummyimage.com/250x250.png/ff4444/ffffff','BLP7'),(8,'http://dummyimage.com/250x250.png/ff4444/ffffff','BLP8'),(9,'http://dummyimage.com/250x250.png/ff4444/ffffff','BLP9'),(10,'http://dummyimage.com/250x250.png/ff4444/ffffff','BLP10'),(11,'http://dummyimage.com/250x250.png/ff4444/ffffff','BLP11'),(12,'http://dummyimage.com/250x250.png/ff4444/ffffff','BLP12'),(13,'http://dummyimage.com/250x250.png/ff4444/ffffff','BLP13'),(14,'http://dummyimage.com/250x250.png/ff4444/ffffff','BLP14'),(15,'http://dummyimage.com/250x250.png/ff4444/ffffff','BLP15'),(16,'http://dummyimage.com/250x250.png/ff4444/ffffff','BLP16'),(17,'http://dummyimage.com/250x250.png/ff4444/ffffff','BLP17'),(18,'http://dummyimage.com/250x250.png/ff4444/ffffff','BLP18'),(19,'http://dummyimage.com/250x250.png/ff4444/ffffff','BLP19'),(20,'http://dummyimage.com/250x250.png/ff4444/ffffff','BLP20'),(21,'http://dummyimage.com/250x250.png/ff4444/ffffff','BLP21'),(22,'http://dummyimage.com/250x250.png/ff4444/ffffff','BLP22'),(23,'http://dummyimage.com/250x250.png/ff4444/ffffff','BLP23'),(24,'http://dummyimage.com/250x250.png/ff4444/ffffff','BLP24'),(25,'http://dummyimage.com/250x250.png/ff4444/ffffff','BLP25'),(26,'http://dummyimage.com/250x250.png/ff4444/ffffff','BLP26'),(27,'http://dummyimage.com/250x250.png/ff4444/ffffff','BLP27'),(28,'http://dummyimage.com/250x250.png/ff4444/ffffff','BLP28'),(29,'http://dummyimage.com/250x250.png/ff4444/ffffff','BLP29'),(30,'http://dummyimage.com/250x250.png/ff4444/ffffff','BLP30'),(31,'http://dummyimage.com/250x250.png/ff4444/ffffff','BLP31'),(32,'http://dummyimage.com/250x250.png/ff4444/ffffff','BLP32'),(33,'http://dummyimage.com/250x250.png/ff4444/ffffff','BLP33'),(34,'http://dummyimage.com/250x250.png/ff4444/ffffff','BLP34'),(35,'http://dummyimage.com/250x250.png/ff4444/ffffff','BLP35');
/*!40000 ALTER TABLE `blueprint` ENABLE KEYS */;
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
