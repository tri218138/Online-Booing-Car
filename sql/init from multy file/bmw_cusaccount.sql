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
-- Table structure for table `cusaccount`
--

DROP TABLE IF EXISTS `cusaccount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cusaccount` (
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `cusID` int unsigned NOT NULL,
  PRIMARY KEY (`username`),
  KEY `cusaccount_cusid_foreign` (`cusID`),
  CONSTRAINT `cusaccount_cusid_foreign` FOREIGN KEY (`cusID`) REFERENCES `customer` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cusaccount`
--

LOCK TABLES `cusaccount` WRITE;
/*!40000 ALTER TABLE `cusaccount` DISABLE KEYS */;
INSERT INTO `cusaccount` VALUES ('Alison','MQ66WH79',41),('Anne','LR96XW69',21),('Barbara','FW47WT90',18),('Beverley','BR31QA85',49),('Carol','DU61UM83',30),('Catherine','LR75YV66',47),('Christine','ZV64BW74',9),('customer_1','1_customer',1),('customer_2','2_customer',2),('customer_3','3_customer',3),('customer_4','4_customer',4),('customer_5','5_customer',5),('customer_6','6_customer',6),('customer_7','7_customer',7),('customer_8','8_customer',8),('Denise','KZ73PP75',43),('Diane','QE80VS68',24),('Dianne','EJ39GD65',35),('Elizabeth','TI18CH67',15),('Gail','ZI48IU89',42),('Heather','LA56QR66',28),('Helen','OI45ZE77',23),('Janet','JS73MO87',27),('Janice','ZN58RR79',31),('Jennifer','GW18ZG80',13),('Judith','BT44JN65',12),('Julie','MU73DZ73',32),('Karen','IW32ED70',22),('Kathleen','NV43PN65',39),('Lesley','NW53RH86',45),('Linda','WM78PF66',17),('Lorraine','YA56CF70',34),('Lynette','AB46LJ67',19),('Margaret','FE29LC90',11),('Marilyn','QF80KP71',36),('Mary','WM77WO83',14),('Maureen','FL86DW79',50),('Pamela','HR52ZT84',29),('Patricia','RT10KB90',16),('Pauline','QZ89AT88',40),('Raewyn','MJ73WC69',38),('Robyn','KN46GC76',20),('Rosemary','XE40WB75',37),('Sandra','TX77PI76',25),('Sharon','LZ64HU77',44),('Shirley','DU58KN67',48),('Susan','HZ36RW79',10),('Suzanne','QG53MC65',33),('Wendy','EP67KV68',26),('Yvonne','YS12CQ81',46);
/*!40000 ALTER TABLE `cusaccount` ENABLE KEYS */;
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
