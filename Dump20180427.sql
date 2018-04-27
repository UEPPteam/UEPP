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
-- Table structure for table `Model_corecoursesinspecializedsubject`
--

DROP TABLE IF EXISTS `Model_corecoursesinspecializedsubject`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Model_corecoursesinspecializedsubject` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `spec_sub` varchar(20) NOT NULL,
  `course` varchar(20) NOT NULL,
  `courseId` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Model_corecoursesinspecializedsubject`
--

LOCK TABLES `Model_corecoursesinspecializedsubject` WRITE;
/*!40000 ALTER TABLE `Model_corecoursesinspecializedsubject` DISABLE KEYS */;
INSERT INTO `Model_corecoursesinspecializedsubject` VALUES (27,'信息管理与信息系统','c语言程序设计','B3I081140'),(28,'工业工程','物流与供应链管理','B3I08336C');
/*!40000 ALTER TABLE `Model_corecoursesinspecializedsubject` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Model_coursesindisciplines`
--

DROP TABLE IF EXISTS `Model_coursesindisciplines`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Model_coursesindisciplines` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `subject` varchar(20) NOT NULL,
  `course` varchar(20) NOT NULL,
  `courseId` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=138 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Model_coursesindisciplines`
--

LOCK TABLES `Model_coursesindisciplines` WRITE;
/*!40000 ALTER TABLE `Model_coursesindisciplines` DISABLE KEYS */;
INSERT INTO `Model_coursesindisciplines` VALUES (135,'管理科学与工程','管理信息系统','B3I08333D'),(136,'管理科学与工程','电子商务基础','B3I08353D'),(137,'金融工程','微观经济学','B3I08221B');
/*!40000 ALTER TABLE `Model_coursesindisciplines` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Model_disciplines`
--

DROP TABLE IF EXISTS `Model_disciplines`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Model_disciplines` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `subjectName` varchar(20) DEFAULT NULL,
  `subjectDes` varchar(512) DEFAULT NULL,
  `courseList` varchar(512) NOT NULL,
  `subjectId` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Model_disciplines`
--

LOCK TABLES `Model_disciplines` WRITE;
/*!40000 ALTER TABLE `Model_disciplines` DISABLE KEYS */;
INSERT INTO `Model_disciplines` VALUES (8,'管理科学与工程','管科','B2E332030 B2H512030 B2D282030 B3I08111B B3I08221B B1A09204A B3I08222B','sub001'),(9,'金融工程','金融工程','B2E332030 B2H512030 B2D282030 B3I08111B B1A09204A B3I08222B B3I081140 B3I08333D B3I08336C B3B081150','sub002'),(10,'会计','会计','B2E332030 B2H512030 B2D282030 B3I08111B B3I08221B B1A09204A B3I08222B B3I081140 B3I08333D B3I08353D B3I08336C B3B081150','sub003');
/*!40000 ALTER TABLE `Model_disciplines` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Model_electivecourses`
--

DROP TABLE IF EXISTS `Model_electivecourses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Model_electivecourses` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `course` varchar(20) NOT NULL,
  `courseId` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Model_electivecourses`
--

LOCK TABLES `Model_electivecourses` WRITE;
/*!40000 ALTER TABLE `Model_electivecourses` DISABLE KEYS */;
INSERT INTO `Model_electivecourses` VALUES (4,'宏观经济学','B3I08222B');
/*!40000 ALTER TABLE `Model_electivecourses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Model_electivecoursesinspecializedsubject`
--

DROP TABLE IF EXISTS `Model_electivecoursesinspecializedsubject`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Model_electivecoursesinspecializedsubject` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `spec_sub` varchar(20) NOT NULL,
  `course` varchar(20) NOT NULL,
  `courseId` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Model_electivecoursesinspecializedsubject`
--

LOCK TABLES `Model_electivecoursesinspecializedsubject` WRITE;
/*!40000 ALTER TABLE `Model_electivecoursesinspecializedsubject` DISABLE KEYS */;
INSERT INTO `Model_electivecoursesinspecializedsubject` VALUES (6,'金融工程','电子商务基础','B3I08353D'),(7,'信息管理与信息系统','计算机软件技术基础','B3B081150');
/*!40000 ALTER TABLE `Model_electivecoursesinspecializedsubject` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Model_specializedsubject`
--

DROP TABLE IF EXISTS `Model_specializedsubject`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Model_specializedsubject` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `spec_sub` varchar(20) NOT NULL,
  `subject` varchar(20) NOT NULL,
  `desc` varchar(512) NOT NULL,
  `courseList` varchar(512) NOT NULL,
  `specId` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Model_specializedsubject`
--

LOCK TABLES `Model_specializedsubject` WRITE;
/*!40000 ALTER TABLE `Model_specializedsubject` DISABLE KEYS */;
INSERT INTO `Model_specializedsubject` VALUES (23,'信息管理与信息系统','管理科学与工程','信管','B2E332030 B2H512030 B2D282030 B3I08111B B3I08221B B1A09204A B3I08222B B3I08336C','major001'),(24,'金融工程','金融工程','金融工程','B2E332030 B2H512030 B2D282030 B3I08111B B1A09204A B3I08222B B3I081140 B3I08333D B3I08336C B3B081150','major002'),(25,'工业工程','管理科学与工程','工业工程','B2E332030 B2H512030 B2D282030 B3I08111B B3I08221B B1A09204A B3I08222B B3I081140 B3B081150','major003'),(26,'工程管理','管理科学与工程','工程管理','B2E332030 B2H512030 B2D282030 B3I08111B B3I08221B B1A09204A B3I08222B B3I081140 B3I08336C B3B081150','major004');
/*!40000 ALTER TABLE `Model_specializedsubject` ENABLE KEYS */;
UNLOCK TABLES;

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
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `model_CourseCategory`
--

LOCK TABLES `model_CourseCategory` WRITE;
/*!40000 ALTER TABLE `model_CourseCategory` DISABLE KEYS */;
INSERT INTO `model_CourseCategory` VALUES (1,'语言类','语言类描述'),(2,'数学与自然科学类',''),(3,'工程基础类',''),(4,'思政类',''),(5,'军理类',''),(7,'体育类',''),(8,'核心通识类',''),(9,'一般通识类',''),(10,'博雅类',''),(11,'核心专业类',''),(12,'一般专业类','');
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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `model_CourseModule`
--

LOCK TABLES `model_CourseModule` WRITE;
/*!40000 ALTER TABLE `model_CourseModule` DISABLE KEYS */;
INSERT INTO `model_CourseModule` VALUES (1,'基础课程','基础课程'),(2,'通识课程','通识课程'),(3,'专业课程','专业课程');
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
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `model_CoursePrevious`
--

LOCK TABLES `model_CoursePrevious` WRITE;
/*!40000 ALTER TABLE `model_CoursePrevious` DISABLE KEYS */;
INSERT INTO `model_CoursePrevious` VALUES (1,'数据结构','离散数学'),(7,'宏观经济学','微观经济学'),(8,'电子商务基础','计算机软件技术基础'),(9,'物流与供应链管理','管理学'),(10,'管理信息系统','电子商务基础'),(11,'管理信息系统','计算机软件技术基础');
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
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `model_Courses`
--

LOCK TABLES `model_Courses` WRITE;
/*!40000 ALTER TABLE `model_Courses` DISABLE KEYS */;
INSERT INTO `model_Courses` VALUES (30,'B2E332030','体育（3）','',0.5,16,16,0,0,'通识课程','体育类','必修课','是','否',''),(31,'B2H512030','博雅课程（文化素质拓展）(3)','',0.5,32,16,0,16,'通识课程','博雅类','必修课','是','否',''),(32,'B2D282030','毛泽东思想与中国特色社会主义概论','',3,48,48,0,0,'通识课程','思政类','必修课','是','否',''),(33,'B3I08111B','管理学','',2,32,32,0,0,'专业课程','核心专业类','必修课','否','是',' ptk'),(34,'B3I08221B','微观经济学','',3,48,48,0,0,'专业课程','核心专业类','必修课','否','是','ptk ptk'),(35,'B1A09204A','概率论','',2,32,32,0,0,'专业课程','核心专业类','必修课','否','是',' ptk'),(36,'B3I08222B','宏观经济学','',3,48,48,0,0,'专业课程','核心专业类','必修课','否','是','rxk'),(37,'B3I081140','c语言程序设计','',2,32,32,0,0,'专业课程','核心专业类','必修课','否','是',' hxk'),(38,'B3I08333D','管理信息系统','',2,32,32,0,0,'专业课程','核心专业类','必修课','否','是','ptk ptk ptk'),(39,'B3I08353D','电子商务基础','',2,32,32,0,0,'专业课程','一般专业类','选修课','否','否','ptk ptk zxk'),(40,'B3I08336C','物流与供应链管理','',2,32,32,0,0,'专业课程','一般专业类','选修课','否','否',' hxk'),(41,'B3B081150','计算机软件技术基础','',2,32,32,0,0,'专业课程','核心专业类','必修课','否','否',' zxk');
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
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `model_EducationCourses`
--

LOCK TABLES `model_EducationCourses` WRITE;
/*!40000 ALTER TABLE `model_EducationCourses` DISABLE KEYS */;
INSERT INTO `model_EducationCourses` VALUES (17,2018,'信息管理与信息系统','B2D282030','毛泽东思想与中国特色社会主义概论',3,48,'二','必修课'),(18,2018,'信息管理与信息系统','B2H512030','博雅课程（文化素质拓展）(3)',0.5,32,'四','必修课'),(19,2017,'信息管理与信息系统','B2D282030','毛泽东思想与中国特色社会主义概论',3,48,'一','必修课'),(20,2018,'信息管理与信息系统','B3B081150','计算机软件技术基础',2,32,'四','必修课'),(27,2018,'信息管理与信息系统','B3I08333D','管理信息系统',2,32,'五','必修课');
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
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `model_EducationMajor`
--

LOCK TABLES `model_EducationMajor` WRITE;
/*!40000 ALTER TABLE `model_EducationMajor` DISABLE KEYS */;
INSERT INTO `model_EducationMajor` VALUES (14,2018,'信息管理与信息系统'),(15,2018,'金融工程'),(16,2018,'工业工程'),(17,2018,'工程管理'),(26,2017,'信息管理与信息系统'),(27,2017,'金融工程'),(28,2017,'工业工程'),(29,2017,'工程管理');
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
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `model_EducationOverview`
--

LOCK TABLES `model_EducationOverview` WRITE;
/*!40000 ALTER TABLE `model_EducationOverview` DISABLE KEYS */;
INSERT INTO `model_EducationOverview` VALUES (5,2018,'2018年度培养方案','已批准'),(7,2017,'2017年度培养方案','未批准');
/*!40000 ALTER TABLE `model_EducationOverview` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `model_EducationPlanCourses`
--

DROP TABLE IF EXISTS `model_EducationPlanCourses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `model_EducationPlanCourses` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `year` int(11) DEFAULT NULL,
  `majorName` varchar(128) DEFAULT NULL,
  `educationPlanId` varchar(128) DEFAULT NULL,
  `courseName` varchar(128) DEFAULT NULL,
  `semester` varchar(45) DEFAULT NULL,
  `status` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `model_EducationPlanCourses`
--

LOCK TABLES `model_EducationPlanCourses` WRITE;
/*!40000 ALTER TABLE `model_EducationPlanCourses` DISABLE KEYS */;
INSERT INTO `model_EducationPlanCourses` VALUES (8,2018,'信息管理与信息系统','','毛泽东思想与中国特色社会主义概论','二',''),(9,2018,'信息管理与信息系统','','博雅课程（文化素质拓展）(3)','四',''),(10,2018,'信息管理与信息系统','','计算机软件技术基础','四',''),(11,2018,'信息管理与信息系统','','管理信息系统','五','');
/*!40000 ALTER TABLE `model_EducationPlanCourses` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-04-27 23:08:22
