-- MySQL dump 10.13  Distrib 5.7.17, for macos10.12 (x86_64)
--
-- Host: 127.0.0.1    Database: uepp
-- ------------------------------------------------------
-- Server version	5.7.21

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `model_EducationCourses`
--

DROP TABLE IF EXISTS `model_EducationCourses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `model_EducationCourses` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `year` varchar(128) DEFAULT NULL,
  `majorName` varchar(128) DEFAULT NULL,
  `courseId` varchar(45) DEFAULT NULL,
  `courseName` varchar(128) DEFAULT NULL,
  `credit` float DEFAULT NULL,
  `creditHour` int(11) DEFAULT NULL,
  `semester` varchar(45) DEFAULT NULL,
  `courseAttribution` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `model_EducationCourses`
--

LOCK TABLES `model_EducationCourses` WRITE;
/*!40000 ALTER TABLE `model_EducationCourses` DISABLE KEYS */;
INSERT INTO `model_EducationCourses` VALUES (17,'2018','信息管理与信息系统','B2D282030','毛泽东思想与中国特色社会主义概论',3,48,'三','必修课'),(18,'2018','信息管理与信息系统','B2H512030','博雅课程（文化素质拓展）(3)',0.5,32,'四','必修课'),(19,'2017','信息管理与信息系统','B2D282030','毛泽东思想与中国特色社会主义概论',3,48,'一','必修课'),(20,'2018','信息管理与信息系统','B3B081150','计算机软件技术基础',2,32,'二','必修课'),(29,'2018','工业工程','B3I08336C','物流与供应链管理',2,32,'一','选修课'),(31,'2018','信息管理与信息系统','B3I08333D','管理信息系统',2,32,'三','必修课'),(33,'2018','工业工程','B3B081150','计算机软件技术基础',2,32,'二','必修课');
/*!40000 ALTER TABLE `model_EducationCourses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `model_EducationMajor`
--

DROP TABLE IF EXISTS `model_EducationMajor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `model_EducationMajor` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `year` int(11) DEFAULT NULL,
  `majorName` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `model_EducationMajor`
--

LOCK TABLES `model_EducationMajor` WRITE;
/*!40000 ALTER TABLE `model_EducationMajor` DISABLE KEYS */;
INSERT INTO `model_EducationMajor` VALUES (30,2018,'信息管理与信息系统'),(31,2018,'金融工程'),(32,2018,'工业工程'),(33,2018,'工程管理');
/*!40000 ALTER TABLE `model_EducationMajor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `model_EducationOverview`
--

DROP TABLE IF EXISTS `model_EducationOverview`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `model_EducationOverview` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `year` varchar(128) DEFAULT NULL,
  `desc` varchar(180) DEFAULT NULL,
  `status` varchar(45) DEFAULT '未审核',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `model_EducationOverview`
--

LOCK TABLES `model_EducationOverview` WRITE;
/*!40000 ALTER TABLE `model_EducationOverview` DISABLE KEYS */;
INSERT INTO `model_EducationOverview` VALUES (5,'2018','2018年度培养方案','已批准'),(7,'2017','2017年度培养方案','已批准');
/*!40000 ALTER TABLE `model_EducationOverview` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `model_EducationPlan`
--

DROP TABLE IF EXISTS `model_EducationPlan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `model_EducationPlan` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `grade` varchar(128) DEFAULT NULL,
  `year` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `model_EducationPlan`
--

LOCK TABLES `model_EducationPlan` WRITE;
/*!40000 ALTER TABLE `model_EducationPlan` DISABLE KEYS */;
INSERT INTO `model_EducationPlan` VALUES (2,'2015级','2018'),(3,'2017级','2018');
/*!40000 ALTER TABLE `model_EducationPlan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `model_EducationPlanCourses`
--

DROP TABLE IF EXISTS `model_EducationPlanCourses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `model_EducationPlanCourses` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `grade` varchar(128) DEFAULT NULL,
  `year` varchar(128) DEFAULT NULL,
  `majorName` varchar(128) DEFAULT NULL,
  `educationPlanId` varchar(128) DEFAULT NULL,
  `courseName` varchar(128) DEFAULT NULL,
  `semester` varchar(45) DEFAULT NULL,
  `status` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `model_EducationPlanCourses`
--

LOCK TABLES `model_EducationPlanCourses` WRITE;
/*!40000 ALTER TABLE `model_EducationPlanCourses` DISABLE KEYS */;
INSERT INTO `model_EducationPlanCourses` VALUES (39,'2015级','2018','信息管理与信息系统','','毛泽东思想与中国特色社会主义概论','三',''),(40,'2015级','2018','信息管理与信息系统','','博雅课程（文化素质拓展）(3)','四',''),(41,'2015级','2018','信息管理与信息系统','','计算机软件技术基础','二',''),(42,'2015级','2018','工业工程','','物流与供应链管理','一',''),(43,'2015级','2018','信息管理与信息系统','','管理信息系统','三',''),(44,'2015级','2018','工业工程','','计算机软件技术基础','二',''),(45,'2017级','2018','信息管理与信息系统','','毛泽东思想与中国特色社会主义概论','三','正进行'),(46,'2017级','2018','信息管理与信息系统','','博雅课程（文化素质拓展）(3)','四',''),(47,'2017级','2018','信息管理与信息系统','','计算机软件技术基础','二','未开始'),(48,'2017级','2018','工业工程','','物流与供应链管理','一',''),(49,'2017级','2018','信息管理与信息系统','','管理信息系统','三',''),(50,'2017级','2018','工业工程','','计算机软件技术基础','二','');
/*!40000 ALTER TABLE `model_EducationPlanCourses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `model_EducationPlanMajor`
--

DROP TABLE IF EXISTS `model_EducationPlanMajor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `model_EducationPlanMajor` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `grade` varchar(128) DEFAULT NULL,
  `year` varchar(128) DEFAULT NULL,
  `majorName` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `model_EducationPlanMajor`
--

LOCK TABLES `model_EducationPlanMajor` WRITE;
/*!40000 ALTER TABLE `model_EducationPlanMajor` DISABLE KEYS */;
INSERT INTO `model_EducationPlanMajor` VALUES (1,'2015级','2018','信息管理与信息系统'),(2,'2015级','2018','金融工程'),(3,'2015级','2018','工业工程'),(4,'2015级','2018','工程管理'),(5,'2017级','2018','信息管理与信息系统'),(6,'2017级','2018','金融工程'),(7,'2017级','2018','工业工程'),(8,'2017级','2018','工程管理');
/*!40000 ALTER TABLE `model_EducationPlanMajor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `model_EducationPlanMajorSemester`
--

DROP TABLE IF EXISTS `model_EducationPlanMajorSemester`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `model_EducationPlanMajorSemester` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `grade` varchar(128) DEFAULT NULL,
  `year` varchar(128) DEFAULT NULL,
  `majorName` varchar(128) DEFAULT NULL,
  `educationPlanId` varchar(128) DEFAULT NULL,
  `semester` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `model_EducationPlanMajorSemester`
--

LOCK TABLES `model_EducationPlanMajorSemester` WRITE;
/*!40000 ALTER TABLE `model_EducationPlanMajorSemester` DISABLE KEYS */;
INSERT INTO `model_EducationPlanMajorSemester` VALUES (1,'2017级','2018','信息管理与信息系统','2016-2017-1','一'),(2,'2017级','2018','信息管理与信息系统','','二'),(3,'2017级','2018','信息管理与信息系统','','三'),(4,'2017级','2018','信息管理与信息系统','','四'),(5,'2017级','2018','信息管理与信息系统','','五'),(6,'2017级','2018','信息管理与信息系统','','六'),(7,'2017级','2018','信息管理与信息系统','','七'),(8,'2017级','2018','信息管理与信息系统','','八'),(9,'2017级','2018','金融工程','','一'),(10,'2017级','2018','金融工程','','二'),(11,'2017级','2018','金融工程','','三'),(12,'2017级','2018','金融工程','','四'),(13,'2017级','2018','金融工程','','五'),(14,'2017级','2018','金融工程','','六'),(15,'2017级','2018','金融工程','','七'),(16,'2017级','2018','金融工程','','八'),(17,'2017级','2018','工业工程','','一'),(18,'2017级','2018','工业工程','','二'),(19,'2017级','2018','工业工程','','三'),(20,'2017级','2018','工业工程','','四'),(21,'2017级','2018','工业工程','','五'),(22,'2017级','2018','工业工程','','六'),(23,'2017级','2018','工业工程','','七'),(24,'2017级','2018','工业工程','','八'),(25,'2017级','2018','工程管理','','一'),(26,'2017级','2018','工程管理','','二'),(27,'2017级','2018','工程管理','','三'),(28,'2017级','2018','工程管理','','四'),(29,'2017级','2018','工程管理','','五'),(30,'2017级','2018','工程管理','','六'),(31,'2017级','2018','工程管理','','七'),(32,'2017级','2018','工程管理','','八');
/*!40000 ALTER TABLE `model_EducationPlanMajorSemester` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-05-08  0:42:17
