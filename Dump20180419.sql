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
-- Table structure for table `model_CourseCategory`
--

DROP TABLE IF EXISTS `model_CourseCategory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `model_CourseCategory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `courseCategory` varchar(45) DEFAULT NULL,
  `description` varchar(180) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `model_CourseCategory`
--

LOCK TABLES `model_CourseCategory` WRITE;
/*!40000 ALTER TABLE `model_CourseCategory` DISABLE KEYS */;
INSERT INTO `model_CourseCategory` VALUES (1,'语言类','语言类描述22');
/*!40000 ALTER TABLE `model_CourseCategory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `model_CourseModule`
--

DROP TABLE IF EXISTS `model_CourseModule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `model_CourseModule` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `courseModule` varchar(45) DEFAULT NULL,
  `description` varchar(180) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `model_CourseModule`
--

LOCK TABLES `model_CourseModule` WRITE;
/*!40000 ALTER TABLE `model_CourseModule` DISABLE KEYS */;
INSERT INTO `model_CourseModule` VALUES (1,'基础课程','基础课程');
/*!40000 ALTER TABLE `model_CourseModule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `model_CoursePrevious`
--

DROP TABLE IF EXISTS `model_CoursePrevious`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `model_CoursePrevious` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `courseName` varchar(128) DEFAULT NULL,
  `pCourseName` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `model_CoursePrevious`
--

LOCK TABLES `model_CoursePrevious` WRITE;
/*!40000 ALTER TABLE `model_CoursePrevious` DISABLE KEYS */;
INSERT INTO `model_CoursePrevious` VALUES (1,'数据结构','离散数学'),(2,'管理信息系统','电子商务');
/*!40000 ALTER TABLE `model_CoursePrevious` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `model_Courses`
--

DROP TABLE IF EXISTS `model_Courses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `model_Courses` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `courseId` varchar(10) NOT NULL,
  `courseName` varchar(128) NOT NULL,
  `courseEngName` varchar(128) DEFAULT NULL,
  `credit` float DEFAULT NULL,
  `creditHour` int(11) DEFAULT NULL,
  `theoryCreditHour` int(11) DEFAULT NULL,
  `experimentCreditHour` int(11) DEFAULT NULL,
  `practiceCreditHour` int(11) DEFAULT NULL,
  `courseModule` varchar(45) DEFAULT NULL,
  `courseCategory` varchar(45) DEFAULT NULL,
  `courseAttribution` varchar(45) DEFAULT NULL,
  `isSchoolCourse` varchar(10) DEFAULT NULL,
  `isCollegeCourse` varchar(10) DEFAULT NULL,
  `courseType` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `model_Courses`
--

LOCK TABLES `model_Courses` WRITE;
/*!40000 ALTER TABLE `model_Courses` DISABLE KEYS */;
INSERT INTO `model_Courses` VALUES (1,'C001','管理信息系统','Information and Management System',1,2,1,3,1,'','',NULL,'','',NULL);
/*!40000 ALTER TABLE `model_Courses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `model_EducationCourses`
--

DROP TABLE IF EXISTS `model_EducationCourses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `model_EducationCourses` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `year` int(11) DEFAULT NULL,
  `majorName` varchar(128) DEFAULT NULL,
  `courseId` varchar(45) DEFAULT NULL,
  `courseName` varchar(128) DEFAULT NULL,
  `credit` float DEFAULT NULL,
  `creditHour` int(11) DEFAULT NULL,
  `semester` varchar(45) DEFAULT NULL,
  `courseAttribution` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `model_EducationCourses`
--

LOCK TABLES `model_EducationCourses` WRITE;
/*!40000 ALTER TABLE `model_EducationCourses` DISABLE KEYS */;
INSERT INTO `model_EducationCourses` VALUES (2,2018,'信息管理与信息系统','C002','管理信息系统',2,48,'四','必修课');
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `model_EducationMajor`
--

LOCK TABLES `model_EducationMajor` WRITE;
/*!40000 ALTER TABLE `model_EducationMajor` DISABLE KEYS */;
INSERT INTO `model_EducationMajor` VALUES (1,2018,'信息管理与信息系统');
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
  `year` int(11) DEFAULT NULL,
  `desc` varchar(180) DEFAULT NULL,
  `status` varchar(45) DEFAULT '未审核',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `model_EducationOverview`
--

LOCK TABLES `model_EducationOverview` WRITE;
/*!40000 ALTER TABLE `model_EducationOverview` DISABLE KEYS */;
INSERT INTO `model_EducationOverview` VALUES (1,2018,'desc','未批准'),(2,2017,'ddsdf',NULL),(3,2016,'sdfsg',NULL);
/*!40000 ALTER TABLE `model_EducationOverview` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-04-19 22:33:36
