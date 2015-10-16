-- MySQL dump 10.13  Distrib 5.6.22, for osx10.9 (x86_64)
--
-- Host: localhost    Database: nfl
-- ------------------------------------------------------
-- Server version	5.6.22

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
-- Table structure for table `games`
--

DROP TABLE IF EXISTS `games`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `games` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `player_id` int(10) unsigned DEFAULT NULL,
  `week` varchar(11) DEFAULT NULL,
  `year` varchar(11) DEFAULT NULL,
  `game_num` int(11) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  `age` varchar(11) DEFAULT NULL,
  `team` varchar(11) NOT NULL DEFAULT '',
  `away` varchar(1) DEFAULT NULL,
  `opp` varchar(11) DEFAULT NULL,
  `result` varchar(11) DEFAULT NULL,
  `rec_tgt` int(11) DEFAULT NULL,
  `rec_rec` int(11) DEFAULT NULL,
  `rec_yds_rec` int(11) DEFAULT NULL,
  `rec_ypr` float DEFAULT NULL,
  `rec_td` int(11) DEFAULT NULL,
  `rush_att` int(11) DEFAULT NULL,
  `rush_yds` int(11) DEFAULT NULL,
  `rush_ypa` float DEFAULT NULL,
  `rush_td` int(11) DEFAULT NULL,
  `pass_cmp` int(11) DEFAULT NULL,
  `pass_att` int(11) DEFAULT NULL,
  `pass_cmp_pct` float DEFAULT NULL,
  `pass_yds` int(11) DEFAULT NULL,
  `pass_td` int(11) DEFAULT NULL,
  `pass_int` int(11) DEFAULT NULL,
  `pass_rate` float DEFAULT NULL,
  `pass_ypa` float DEFAULT NULL,
  `pass_adjusted_ypa` float DEFAULT NULL,
  `kick_ret` int(11) DEFAULT NULL,
  `kick_ret_yds` int(11) DEFAULT NULL,
  `kick_ret_ypa` float DEFAULT NULL,
  `kick_ret_td` int(11) DEFAULT NULL,
  `punt_ret` int(11) DEFAULT NULL,
  `punt_ret_yds` int(11) DEFAULT NULL,
  `punt_ret_ypa` float DEFAULT NULL,
  `punt_ret_td` int(11) DEFAULT NULL,
  `two_pt_con` int(11) DEFAULT NULL,
  `pts` int(11) DEFAULT NULL,
  `sack` int(11) DEFAULT NULL,
  `tackle` int(11) DEFAULT NULL,
  `ast_tackle` int(11) DEFAULT NULL,
  `games_started` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `player_games` (`player_id`),
  CONSTRAINT `player_games` FOREIGN KEY (`player_id`) REFERENCES `players` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=36493 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `players`
--

DROP TABLE IF EXISTS `players`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `players` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `first_name` varchar(20) NOT NULL DEFAULT '',
  `last_name` varchar(20) NOT NULL DEFAULT '',
  `position` varchar(11) DEFAULT NULL,
  `url` varchar(70) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=861 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-10-16 14:54:28
