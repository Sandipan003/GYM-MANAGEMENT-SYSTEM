
-- MySQL dump 10.13  Distrib 8.0.44, for macos12.7 (arm64)
--
-- Host: localhost    Database: kinetic_pulse_db
-- ------------------------------------------------------
-- Server version	8.0.44

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `attendance_attendance`
--

DROP TABLE IF EXISTS `attendance_attendance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `attendance_attendance` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `check_in` datetime(6) NOT NULL,
  `check_out` datetime(6) DEFAULT NULL,
  `zone` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `activity` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `notes` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `member_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `attendance_attendance_member_id_9777e18b_fk_members_member_id` (`member_id`),
  CONSTRAINT `attendance_attendance_member_id_9777e18b_fk_members_member_id` FOREIGN KEY (`member_id`) REFERENCES `members_member` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attendance_attendance`
--

LOCK TABLES `attendance_attendance` WRITE;
/*!40000 ALTER TABLE `attendance_attendance` DISABLE KEYS */;
INSERT INTO `attendance_attendance` VALUES (1,'2026-03-29 20:55:07.258537','2026-03-29 22:34:07.258537','weight_room','cardio','','2026-03-30 09:01:07.259133',1),(2,'2026-03-30 08:36:07.258537',NULL,'zone_b','upper_body','','2026-03-30 09:01:07.260067',1),(3,'2026-03-29 14:27:07.258537','2026-03-29 15:35:07.258537','yoga_room','upper_body','','2026-03-30 09:01:07.261119',2),(4,'2026-03-28 22:44:07.258537','2026-03-29 01:17:07.258537','cardio_zone','yoga','','2026-03-30 09:01:07.261708',2),(5,'2026-03-27 12:46:07.258537','2026-03-27 15:26:07.258537','weight_room','leg_day','','2026-03-30 09:01:07.262314',2),(6,'2026-03-26 22:43:07.258537','2026-03-27 00:15:07.258537','zone_b','powerlifting','','2026-03-30 09:01:07.262980',2),(7,'2026-03-26 02:45:07.258537','2026-03-26 04:55:07.258537','yoga_room','leg_day','','2026-03-30 09:01:07.263536',2),(8,'2026-03-24 17:01:07.258537','2026-03-24 18:33:07.258537','cardio_zone','yoga','','2026-03-30 09:01:07.264034',2),(9,'2026-03-30 01:04:07.258537','2026-03-30 02:35:07.258537','cardio_zone','powerlifting','','2026-03-30 09:01:07.264731',5),(10,'2026-03-28 13:47:07.258537','2026-03-28 15:11:07.258537','cardio_zone','general','','2026-03-30 09:01:07.265786',5),(11,'2026-03-27 16:53:07.258537','2026-03-27 18:09:07.258537','yoga_room','cardio','','2026-03-30 09:01:07.267174',5),(12,'2026-03-29 16:17:07.258537','2026-03-29 17:59:07.258537','weight_room','cardio','','2026-03-30 09:01:07.268140',6),(13,'2026-03-28 16:33:07.258537','2026-03-28 18:07:07.258537','yoga_room','hiit','','2026-03-30 09:01:07.270490',6),(14,'2026-03-27 12:40:07.258537','2026-03-27 13:46:07.258537','zone_b','general','','2026-03-30 09:01:07.271264',6),(15,'2026-03-27 02:43:07.258537','2026-03-27 04:50:07.258537','main_hall','leg_day','','2026-03-30 09:01:07.272095',6),(16,'2026-03-30 08:43:07.258537',NULL,'cardio_zone','cardio','','2026-03-30 09:01:07.272925',6),(17,'2026-03-29 15:17:07.258537','2026-03-29 16:55:07.258537','weight_room','cardio','','2026-03-30 09:01:07.273579',7),(18,'2026-03-28 13:55:07.258537','2026-03-28 16:23:07.258537','cardio_zone','hiit','','2026-03-30 09:01:07.274285',7),(19,'2026-03-29 18:26:07.258537','2026-03-29 19:53:07.258537','main_hall','yoga','','2026-03-30 09:01:07.275384',8),(20,'2026-03-30 08:24:07.258537',NULL,'zone_b','hiit','','2026-03-30 09:01:07.276086',8),(21,'2026-03-29 18:54:07.258537','2026-03-29 20:37:07.258537','weight_room','powerlifting','','2026-03-30 09:01:07.276678',10),(22,'2026-03-28 16:35:07.258537','2026-03-28 19:03:07.258537','zone_b','hiit','','2026-03-30 09:01:07.277245',10),(23,'2026-03-30 07:43:07.258537',NULL,'weight_room','cardio','','2026-03-30 09:01:07.277937',10);
/*!40000 ALTER TABLE `attendance_attendance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add member',7,'add_member'),(26,'Can change member',7,'change_member'),(27,'Can delete member',7,'delete_member'),(28,'Can view member',7,'view_member'),(29,'Can add membership plan',8,'add_membershipplan'),(30,'Can change membership plan',8,'change_membershipplan'),(31,'Can delete membership plan',8,'delete_membershipplan'),(32,'Can view membership plan',8,'view_membershipplan'),(33,'Can add payment',9,'add_payment'),(34,'Can change payment',9,'change_payment'),(35,'Can delete payment',9,'delete_payment'),(36,'Can view payment',9,'view_payment'),(37,'Can add attendance',10,'add_attendance'),(38,'Can change attendance',10,'change_attendance'),(39,'Can delete attendance',10,'delete_attendance'),(40,'Can view attendance',10,'view_attendance');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$600000$qV4R6TzGVOx6eO16CB6MDU$nSMh+IbDAsdF6qGNqjswWEoKi3wa5BSNxm864BMxp4Y=','2026-03-30 09:09:34.947447',1,'admin','','','admin@kineticpulse.com',1,1,'2026-03-30 09:01:13.102704');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8mb4_unicode_ci,
  `object_repr` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(10,'attendance','attendance'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(7,'members','member'),(9,'payments','payment'),(8,'plans','membershipplan'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2026-03-30 09:01:00.689958'),(2,'auth','0001_initial','2026-03-30 09:01:00.753130'),(3,'admin','0001_initial','2026-03-30 09:01:00.769733'),(4,'admin','0002_logentry_remove_auto_add','2026-03-30 09:01:00.772378'),(5,'admin','0003_logentry_add_action_flag_choices','2026-03-30 09:01:00.774837'),(6,'plans','0001_initial','2026-03-30 09:01:00.778617'),(7,'members','0001_initial','2026-03-30 09:01:00.790795'),(8,'attendance','0001_initial','2026-03-30 09:01:00.799325'),(9,'contenttypes','0002_remove_content_type_name','2026-03-30 09:01:00.812902'),(10,'auth','0002_alter_permission_name_max_length','2026-03-30 09:01:00.821150'),(11,'auth','0003_alter_user_email_max_length','2026-03-30 09:01:00.825962'),(12,'auth','0004_alter_user_username_opts','2026-03-30 09:01:00.828321'),(13,'auth','0005_alter_user_last_login_null','2026-03-30 09:01:00.834844'),(14,'auth','0006_require_contenttypes_0002','2026-03-30 09:01:00.835412'),(15,'auth','0007_alter_validators_add_error_messages','2026-03-30 09:01:00.837832'),(16,'auth','0008_alter_user_username_max_length','2026-03-30 09:01:00.847186'),(17,'auth','0009_alter_user_last_name_max_length','2026-03-30 09:01:00.854770'),(18,'auth','0010_alter_group_name_max_length','2026-03-30 09:01:00.858938'),(19,'auth','0011_update_proxy_permissions','2026-03-30 09:01:00.862116'),(20,'auth','0012_alter_user_first_name_max_length','2026-03-30 09:01:00.870106'),(21,'payments','0001_initial','2026-03-30 09:01:00.884645'),(22,'sessions','0001_initial','2026-03-30 09:01:00.888989');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('ao12chcwpt65a8t7syrh02t5sd0oy5it','.eJxVjEEOwiAQRe_C2pAOU0Bcuu8ZyMAwUjVtUtqV8e7apAvd_vfef6lI21rj1soSR1YXBer0uyXKjzLtgO803Wad52ldxqR3RR-06WHm8rwe7t9BpVa_dSfiWCQHAHMm9KnvkTKAWAtigkfuWQJSEIfZICMROMudZ-Nc8KzeH-yzN9Y:1w78Wu:rkCF0zuljF0fmwHVY9h-GGQ-Yw2NqPqAaN06oEPmYV8','2026-04-13 09:03:28.001263'),('w32azewikqka0swlrf1fg4yvakc08a17','.eJxVjEEOwiAQRe_C2pAOU0Bcuu8ZyMAwUjVtUtqV8e7apAvd_vfef6lI21rj1soSR1YXBer0uyXKjzLtgO803Wad52ldxqR3RR-06WHm8rwe7t9BpVa_dSfiWCQHAHMm9KnvkTKAWAtigkfuWQJSEIfZICMROMudZ-Nc8KzeH-yzN9Y:1w78co:Td_qZv8lrdKpniO-bL5mRNmNEs50rF1E8WgvmbR1l7w','2026-04-13 09:09:34.948662');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `members_member`
--

DROP TABLE IF EXISTS `members_member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `members_member` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `member_id` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `first_name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_unicode_ci NOT NULL,
  `phone` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `photo` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `status` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `join_date` date NOT NULL,
  `membership_expiry` date DEFAULT NULL,
  `address` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `emergency_contact` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `notes` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `plan_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `member_id` (`member_id`),
  UNIQUE KEY `email` (`email`),
  KEY `members_member_plan_id_5cd18dd9_fk_plans_membershipplan_id` (`plan_id`),
  CONSTRAINT `members_member_plan_id_5cd18dd9_fk_plans_membershipplan_id` FOREIGN KEY (`plan_id`) REFERENCES `plans_membershipplan` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `members_member`
--

LOCK TABLES `members_member` WRITE;
/*!40000 ALTER TABLE `members_member` DISABLE KEYS */;
INSERT INTO `members_member` VALUES (1,'KP-0001','Marcus','Thorne','marcus.thorne@email.com','+91 9876543210','','active','2026-03-25','2026-04-24','','','','2026-03-30 09:01:07.230250','2026-03-30 09:01:07.230258',3),(2,'KP-0002','Elena','Rodriguez','elena.r@email.com','+91 9876543211','','active','2026-03-28','2026-04-27','','','','2026-03-30 09:01:07.232138','2026-03-30 09:01:07.232145',2),(3,'KP-0003','Jordan','Smith','jordan.smith@email.com','+91 9876543212','','expired','2026-02-13','2026-03-15','','','','2026-03-30 09:01:07.233293','2026-03-30 09:01:07.233299',1),(4,'KP-0004','Sarah','Jenkins','sarah.j@email.com','+91 9876543213','','pending','2026-03-29','2026-04-28','','','','2026-03-30 09:01:07.234647','2026-03-30 09:01:07.234655',2),(5,'KP-0005','David','Rossi','david.rossi@email.com','+91 9876543214','','active','2026-03-20','2026-04-19','','','','2026-03-30 09:01:07.235891','2026-03-30 09:01:07.235900',3),(6,'KP-0006','Aisha','Patel','aisha.patel@email.com','+91 9876543215','','active','2026-03-10','2026-04-09','','','','2026-03-30 09:01:07.237100','2026-03-30 09:01:07.237108',1),(7,'KP-0007','Ryan','Nakamura','ryan.n@email.com','+91 9876543216','','active','2025-12-30','2026-12-25','','','','2026-03-30 09:01:07.238418','2026-03-30 09:01:07.238426',4),(8,'KP-0008','Priya','Mehta','priya.m@email.com','+91 9876543217','','active','2026-03-15','2026-04-14','','','','2026-03-30 09:01:07.239824','2026-03-30 09:01:07.239830',2),(9,'KP-0009','Lucas','Wade','lucas.w@email.com','+91 9876543218','','expired','2026-01-29','2026-02-28','','','','2026-03-30 09:01:07.241169','2026-03-30 09:01:07.241174',1),(10,'KP-0010','Sofia','Chen','sofia.chen@email.com','+91 9876543219','','active','2026-03-27','2026-04-26','','','','2026-03-30 09:01:07.242504','2026-03-30 09:01:07.242509',3);
/*!40000 ALTER TABLE `members_member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payments_payment`
--

DROP TABLE IF EXISTS `payments_payment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payments_payment` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `amount` decimal(10,2) NOT NULL,
  `payment_date` date NOT NULL,
  `payment_method` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `status` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `transaction_id` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `notes` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `member_id` bigint NOT NULL,
  `plan_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `payments_payment_member_id_2ea62bf9_fk_members_member_id` (`member_id`),
  KEY `payments_payment_plan_id_5d571f5a_fk_plans_membershipplan_id` (`plan_id`),
  CONSTRAINT `payments_payment_member_id_2ea62bf9_fk_members_member_id` FOREIGN KEY (`member_id`) REFERENCES `members_member` (`id`),
  CONSTRAINT `payments_payment_plan_id_5d571f5a_fk_plans_membershipplan_id` FOREIGN KEY (`plan_id`) REFERENCES `plans_membershipplan` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payments_payment`
--

LOCK TABLES `payments_payment` WRITE;
/*!40000 ALTER TABLE `payments_payment` DISABLE KEYS */;
INSERT INTO `payments_payment` VALUES (1,4999.00,'2026-03-28','upi','paid','TXN292302','','2026-03-30 09:01:07.245061',1,3),(2,4999.00,'2026-02-26','online','paid','TXN343492','','2026-03-30 09:01:07.245905',1,3),(3,2499.00,'2026-03-29','upi','paid','TXN570666','','2026-03-30 09:01:07.246931',2,2),(4,4999.00,'2026-03-27','upi','paid','TXN400177','','2026-03-30 09:01:07.247901',5,3),(5,999.00,'2026-03-27','cash','paid','TXN855679','','2026-03-30 09:01:07.248858',6,1),(6,999.00,'2026-02-25','online','paid','TXN654921','','2026-03-30 09:01:07.249855',6,1),(7,8999.00,'2026-03-28','online','paid','TXN894419','','2026-03-30 09:01:07.250802',7,4),(8,2499.00,'2026-03-26','upi','paid','TXN796304','','2026-03-30 09:01:07.251754',8,2),(9,4999.00,'2026-03-25','online','paid','TXN496313','','2026-03-30 09:01:07.253022',10,3),(10,4999.00,'2026-02-23','cash','paid','TXN930120','','2026-03-30 09:01:07.257069',10,3);
/*!40000 ALTER TABLE `payments_payment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `plans_membershipplan`
--

DROP TABLE IF EXISTS `plans_membershipplan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `plans_membershipplan` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `slug` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `duration_months` int unsigned NOT NULL,
  `description` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `features` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_featured` tinyint(1) NOT NULL,
  `color_label` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`),
  CONSTRAINT `plans_membershipplan_chk_1` CHECK ((`duration_months` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `plans_membershipplan`
--

LOCK TABLES `plans_membershipplan` WRITE;
/*!40000 ALTER TABLE `plans_membershipplan` DISABLE KEYS */;
INSERT INTO `plans_membershipplan` VALUES (1,'Standard','standard',999.00,1,'Perfect for beginners','24/7 Access\nStandard Equipment\nLocker Room Access',0,'outline',1,'2026-03-30 09:01:07.225197','2026-03-30 09:01:07.225212'),(2,'Premium','premium',2499.00,1,'Best value for regular members','24/7 Access\nAll Equipment\nPersonal Training (2x/mo)\nRecovery Zone\nLocker Room',1,'primary',1,'2026-03-30 09:01:07.226881','2026-03-30 09:01:07.226889'),(3,'Elite Performance','elite',4999.00,1,'The ultimate gym experience','24/7 VIP Access\nUnlimited Personal Training\nSpa & Cryotherapy\nNutrition Coaching\nBiometric Tracking\nGuest Passes (2/mo)',0,'secondary',1,'2026-03-30 09:01:07.227713','2026-03-30 09:01:07.227719'),(4,'Annual Standard','annual-standard',8999.00,12,'Best price per month — commit yearly','24/7 Access\nStandard Equipment\nLocker Room\n2 Months Free',0,'tertiary',1,'2026-03-30 09:01:07.228735','2026-03-30 09:01:07.228744');
/*!40000 ALTER TABLE `plans_membershipplan` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-03-30 14:39:43
