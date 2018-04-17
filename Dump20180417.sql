-- MySQL dump 10.13  Distrib 5.7.12, for osx10.9 (x86_64)
--
-- Host: localhost    Database: uepp
-- ------------------------------------------------------
-- Server version	5.7.17

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
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Model_corecoursesinspecializedsubject`
--

LOCK TABLES `Model_corecoursesinspecializedsubject` WRITE;
/*!40000 ALTER TABLE `Model_corecoursesinspecializedsubject` DISABLE KEYS */;
INSERT INTO `Model_corecoursesinspecializedsubject` VALUES (1,'信管','运筹学');
/*!40000 ALTER TABLE `Model_corecoursesinspecializedsubject` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Model_coursecategory`
--

DROP TABLE IF EXISTS `Model_coursecategory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Model_coursecategory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `courseCategory` varchar(45) NOT NULL,
  `description` varchar(180) NOT NULL,
  `course` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Model_coursecategory`
--

LOCK TABLES `Model_coursecategory` WRITE;
/*!40000 ALTER TABLE `Model_coursecategory` DISABLE KEYS */;
/*!40000 ALTER TABLE `Model_coursecategory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Model_coursemodule`
--

DROP TABLE IF EXISTS `Model_coursemodule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Model_coursemodule` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `courseModule` varchar(45) NOT NULL,
  `description` varchar(180) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Model_coursemodule`
--

LOCK TABLES `Model_coursemodule` WRITE;
/*!40000 ALTER TABLE `Model_coursemodule` DISABLE KEYS */;
/*!40000 ALTER TABLE `Model_coursemodule` ENABLE KEYS */;
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
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=124 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Model_coursesindisciplines`
--

LOCK TABLES `Model_coursesindisciplines` WRITE;
/*!40000 ALTER TABLE `Model_coursesindisciplines` DISABLE KEYS */;
INSERT INTO `Model_coursesindisciplines` VALUES (1,'管科','运筹学');
/*!40000 ALTER TABLE `Model_coursesindisciplines` ENABLE KEYS */;
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
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Model_electivecourses`
--

LOCK TABLES `Model_electivecourses` WRITE;
/*!40000 ALTER TABLE `Model_electivecourses` DISABLE KEYS */;
INSERT INTO `Model_electivecourses` VALUES (1,'人因工程');
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
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Model_electivecoursesinspecializedsubject`
--

LOCK TABLES `Model_electivecoursesinspecializedsubject` WRITE;
/*!40000 ALTER TABLE `Model_electivecoursesinspecializedsubject` DISABLE KEYS */;
INSERT INTO `Model_electivecoursesinspecializedsubject` VALUES (1,'信管','管理学');
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
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Model_specializedsubject`
--

LOCK TABLES `Model_specializedsubject` WRITE;
/*!40000 ALTER TABLE `Model_specializedsubject` DISABLE KEYS */;
INSERT INTO `Model_specializedsubject` VALUES (1,'信管','管科','cs'),(2,'工业工程','管理科学与工程','ee');
/*!40000 ALTER TABLE `Model_specializedsubject` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Model_uepp`
--

DROP TABLE IF EXISTS `Model_uepp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Model_uepp` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `courseId` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Model_uepp`
--

LOCK TABLES `Model_uepp` WRITE;
/*!40000 ALTER TABLE `Model_uepp` DISABLE KEYS */;
/*!40000 ALTER TABLE `Model_uepp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TestModel_test`
--

DROP TABLE IF EXISTS `TestModel_test`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TestModel_test` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TestModel_test`
--

LOCK TABLES `TestModel_test` WRITE;
/*!40000 ALTER TABLE `TestModel_test` DISABLE KEYS */;
/*!40000 ALTER TABLE `TestModel_test` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add test',7,'add_test'),(20,'Can change test',7,'change_test'),(21,'Can delete test',7,'delete_test'),(22,'Can add uepp',8,'add_uepp'),(23,'Can change uepp',8,'change_uepp'),(24,'Can delete uepp',8,'delete_uepp'),(25,'Can add course',9,'add_course'),(26,'Can change course',9,'change_course'),(27,'Can delete course',9,'delete_course'),(28,'Can add disciplines',10,'add_disciplines'),(29,'Can change disciplines',10,'change_disciplines'),(30,'Can delete disciplines',10,'delete_disciplines'),(31,'Can add specialized subject',11,'add_specializedsubject'),(32,'Can change specialized subject',11,'change_specializedsubject'),(33,'Can delete specialized subject',11,'delete_specializedsubject'),(34,'Can add core courses in specialized subject',12,'add_corecoursesinspecializedsubject'),(35,'Can change core courses in specialized subject',12,'change_corecoursesinspecializedsubject'),(36,'Can delete core courses in specialized subject',12,'delete_corecoursesinspecializedsubject'),(37,'Can add courses in disciplines',13,'add_coursesindisciplines'),(38,'Can change courses in disciplines',13,'change_coursesindisciplines'),(39,'Can delete courses in disciplines',13,'delete_coursesindisciplines'),(40,'Can add elective courses',14,'add_electivecourses'),(41,'Can change elective courses',14,'change_electivecourses'),(42,'Can delete elective courses',14,'delete_electivecourses'),(43,'Can add elective courses in specialized subject',15,'add_electivecoursesinspecializedsubject'),(44,'Can change elective courses in specialized subject',15,'change_electivecoursesinspecializedsubject'),(45,'Can delete elective courses in specialized subject',15,'delete_electivecoursesinspecializedsubject'),(46,'Can add course category',16,'add_coursecategory'),(47,'Can change course category',16,'change_coursecategory'),(48,'Can delete course category',16,'delete_coursecategory'),(49,'Can add course module',17,'add_coursemodule'),(50,'Can change course module',17,'change_coursemodule'),(51,'Can delete course module',17,'delete_coursemodule');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(12,'Model','corecoursesinspecializedsubject'),(9,'Model','course'),(16,'Model','coursecategory'),(17,'Model','coursemodule'),(13,'Model','coursesindisciplines'),(10,'Model','disciplines'),(14,'Model','electivecourses'),(15,'Model','electivecoursesinspecializedsubject'),(11,'Model','specializedsubject'),(8,'Model','uepp'),(6,'sessions','session'),(7,'TestModel','test');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'TestModel','0001_initial','2018-04-01 05:31:27.992123'),(2,'contenttypes','0001_initial','2018-04-01 05:31:28.024601'),(3,'auth','0001_initial','2018-04-01 05:31:28.298552'),(4,'admin','0001_initial','2018-04-01 05:31:28.361419'),(5,'admin','0002_logentry_remove_auto_add','2018-04-01 05:31:28.381145'),(6,'contenttypes','0002_remove_content_type_name','2018-04-01 05:31:28.425423'),(7,'auth','0002_alter_permission_name_max_length','2018-04-01 05:31:28.443154'),(8,'auth','0003_alter_user_email_max_length','2018-04-01 05:31:28.466918'),(9,'auth','0004_alter_user_username_opts','2018-04-01 05:31:28.476271'),(10,'auth','0005_alter_user_last_login_null','2018-04-01 05:31:28.500551'),(11,'auth','0006_require_contenttypes_0002','2018-04-01 05:31:28.502216'),(12,'auth','0007_alter_validators_add_error_messages','2018-04-01 05:31:28.517232'),(13,'auth','0008_alter_user_username_max_length','2018-04-01 05:31:28.574530'),(14,'auth','0009_alter_user_last_name_max_length','2018-04-01 05:31:28.607419'),(15,'sessions','0001_initial','2018-04-01 05:31:28.631592'),(16,'Model','0001_initial','2018-04-03 06:21:33.455746'),(17,'Model','0002_specializedsubject','2018-04-16 02:27:45.560833'),(18,'Model','0003_corecoursesinspecializedsubject_coursesindisciplines_electivecourses_electivecoursesinspecializedsub','2018-04-16 05:04:03.915179'),(19,'Model','0004_coursecategory_coursemodule','2018-04-17 01:58:20.675477');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `model_course`
--

DROP TABLE IF EXISTS `model_course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `model_course` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `courseId` varchar(20) NOT NULL,
  `courseName` varchar(45) NOT NULL,
  `courseAttribute` varchar(20) DEFAULT NULL COMMENT '课程性质',
  `courseModule` varchar(45) DEFAULT NULL COMMENT '课程所属模块\n',
  `courseType` varchar(45) DEFAULT NULL,
  `credit` float DEFAULT NULL COMMENT '学分',
  `creditHour` float DEFAULT NULL COMMENT '学时',
  `introduction` varchar(180) DEFAULT NULL COMMENT '课程介绍',
  `pCourseId` varchar(20) DEFAULT NULL COMMENT '先行课程编号\n',
  `boundCourseId` varchar(20) DEFAULT NULL COMMENT '绑定课程编号',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `model_course`
--

LOCK TABLES `model_course` WRITE;
/*!40000 ALTER TABLE `model_course` DISABLE KEYS */;
INSERT INTO `model_course` VALUES (1,'c001','电子商务','必修课','基础课程','工程课',12,12,'12','21','12');
/*!40000 ALTER TABLE `model_course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `model_disciplines`
--

DROP TABLE IF EXISTS `model_disciplines`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `model_disciplines` (
  `id` int(11) NOT NULL,
  `subjectName` varchar(20) DEFAULT NULL,
  `subjectDes` varchar(512) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `model_disciplines`
--

LOCK TABLES `model_disciplines` WRITE;
/*!40000 ALTER TABLE `model_disciplines` DISABLE KEYS */;
INSERT INTO `model_disciplines` VALUES (1,'管理科学与工程','管科赞');
/*!40000 ALTER TABLE `model_disciplines` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `model_major`
--

DROP TABLE IF EXISTS `model_major`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `model_major` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `majorId` varchar(20) NOT NULL,
  `majorName` varchar(45) DEFAULT NULL,
  `introduction` varchar(45) DEFAULT NULL COMMENT '专业介绍',
  PRIMARY KEY (`id`,`majorId`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `model_major`
--

LOCK TABLES `model_major` WRITE;
/*!40000 ALTER TABLE `model_major` DISABLE KEYS */;
INSERT INTO `model_major` VALUES (1,'m001','信息管理与信息系统','信息管理与信息系统');
/*!40000 ALTER TABLE `model_major` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `model_syllabusOverview`
--

DROP TABLE IF EXISTS `model_syllabusOverview`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `model_syllabusOverview` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `syllabusOverviewId` varchar(20) NOT NULL,
  `majorId` varchar(20) DEFAULT NULL,
  `grade` varchar(45) DEFAULT NULL COMMENT '对应年级',
  `publishDate` date DEFAULT NULL COMMENT '发布时间',
  `eduSystem` varchar(45) DEFAULT NULL COMMENT '基本学制',
  `totalCredit` float DEFAULT NULL COMMENT '最低总学分',
  `degree` varchar(45) DEFAULT NULL COMMENT '授予学位',
  `courseModule` varchar(45) DEFAULT NULL COMMENT '课程包括模块',
  `coursetype` varchar(45) DEFAULT NULL COMMENT '课程包括类别',
  `status` varchar(20) DEFAULT NULL COMMENT '状态',
  PRIMARY KEY (`id`,`syllabusOverviewId`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `model_syllabusOverview`
--

LOCK TABLES `model_syllabusOverview` WRITE;
/*!40000 ALTER TABLE `model_syllabusOverview` DISABLE KEYS */;
/*!40000 ALTER TABLE `model_syllabusOverview` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `model_teacher`
--

DROP TABLE IF EXISTS `model_teacher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `model_teacher` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `teacherId` varchar(20) NOT NULL,
  `teacherName` varchar(45) DEFAULT NULL,
  `majorId` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`,`teacherId`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `model_teacher`
--

LOCK TABLES `model_teacher` WRITE;
/*!40000 ALTER TABLE `model_teacher` DISABLE KEYS */;
INSERT INTO `model_teacher` VALUES (1,'t001','闪老师','信息管理与信息系统');
/*!40000 ALTER TABLE `model_teacher` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-04-17  9:59:34
