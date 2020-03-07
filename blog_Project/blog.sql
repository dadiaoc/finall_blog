/*
Navicat MySQL Data Transfer

Source Server         : mingming
Source Server Version : 50717
Source Host           : localhost:3306
Source Database       : blog

Target Server Type    : MYSQL
Target Server Version : 50717
File Encoding         : 65001

Date: 2020-03-07 01:09:02
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for article
-- ----------------------------
DROP TABLE IF EXISTS `article`;
CREATE TABLE `article` (
  `aid` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(500) NOT NULL,
  `content` varchar(10000) DEFAULT NULL,
  `create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `cid` int(11) DEFAULT NULL,
  `hits` int(11) DEFAULT '0',
  `comments` int(11) DEFAULT '0',
  `picture` varchar(300) DEFAULT NULL,
  `tid` int(11) DEFAULT NULL,
  PRIMARY KEY (`aid`),
  KEY `cid` (`cid`),
  CONSTRAINT `cid` FOREIGN KEY (`cid`) REFERENCES `category` (`cid`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of article
-- ----------------------------
INSERT INTO `article` VALUES ('1', '各游戏头牌主播，DNF是旭旭宝宝，英雄联盟一哥充满争议', '游戏圈与直播圈一直是相辅相成，不可分割的。现在“主播”已经成为大部分人都能够接受的职业，游戏主播更是直播圈的主力军。但在直播圈主播的素质参差不齐，人气更是天差地别。有几千人气仍在坚持的小主播，也有数百万乃至上千万人气的直播一哥。近日各游戏的头牌主播出路，DNF为旭旭宝宝，英雄联盟一哥则是引起玩家热议。', '2020-03-05 11:28:01', '1', '345', '3', '/static/img/xuxubaobao.jpg', '1');
INSERT INTO `article` VALUES ('2', 'LPL训练赛曝TES最大短板，左手独木难支？这位AD或成救命稻草', '因为特殊原因，LPL的开赛已经正式延期，开赛日期还是个未知数。虽然官方表示鼓励线上电竞赛事的举办，但规则和技术等都需要时间，故此近日LPL显然是无法重开春季赛的。为了让粉丝们了解到LPL战队的训练程度，官方也是别出心裁的上线了LPL训练赛的直播。在这个直播中LPL的战队会进行训练赛对决，但因为粉丝数颇多的缘故，也能吸引数以百万的玩家观看。故此大部分战队也会拿出自己的真实实力进行对抗，也算是满足LPL粉丝们观赛的愿望。', '2020-03-05 11:28:02', '1', '453', '3', '/static/img/uzi.jpeg', '2');
INSERT INTO `article` VALUES ('3', '她被称为最美DNF女玩家，因多次与旭旭宝宝搭档而爆红', '在直播圈子里女主播绝对不在少数，但凭借自己出人头地的女主播却非常稀少。大部分女主播都是通过与大牌主播互动籍此上位，这似乎也已经成为直播圈的“潜规则”之一。虽然DNF圈在直播圈算是一个“二流圈子”，但DNF一个却绝对是T0级别的主播。不少人都想搭上旭旭宝宝的', '2020-03-05 11:28:04', '1', '4345343', '3', '/static/img/mantu.jpeg', '1');
INSERT INTO `article` VALUES ('4', 'DNF的CP系统玩不转？多职业护石符文搭配推荐', '奶妈：蓝色符文和绿色符文两个减CD的符文可以将圣歌的冷却时间压缩到最低，在未来的100版本甚至可以做到全程唱歌。\r\n\r\n团长：红色符文和紫色符文选择行刑是现版本较普遍的一种搭配，而剩下的两个符文可根据自己的喜好自由选择。\r\n\r\n龙女：蓝色符文选择百八念珠是因为将CD压缩到20秒内，而紫色符文选择夺命大魂阵是为了打出爆发伤害。\r\n\r\n四姨：如果不喜欢傲慢这个技能，红色符文和紫色符文的技能方面可以更改为暴食也可，蓝色方面没有多大异议，可更改为自己习惯的技能。', '2020-03-05 11:28:05', '1', '345321', '3', '/static/img/naima.jpeg', '1');
INSERT INTO `article` VALUES ('5', 'DNF百级版本疲劳别全刷深渊，这两个副本必须去，还有魔界大战', '首先是痛苦的地下室以及暗黑神殿这两个副本，就重要性而言，跟智慧的引导（100级副本）不相上下。这也是不少回归玩家容易忽略的两个副本，可能不少人会问：为什么说这两个副本很重要呢？因为在这里玩家可以获得史诗或者是神话装备，而且不需要消耗任何的票，可以说是白嫖。', '2020-03-05 11:28:06', '1', '3123', '3', '/static/img/hhhh.jpeg', '1');
INSERT INTO `article` VALUES ('6', '继厂长跟李哥后，谁是最有可能获得股份的职业选手？乌兹真的行', 'Hello各位小伙伴们，不知道你们是否记得，在前几日李哥接受了来自sktt1的一份礼物，价值极高的战队股份，这也引发了网友们一系列的讨论，那就是目前我们已知的知名选手中，厂长跟李哥是受到了来自战队的股份赠送，而出他们之外，最有可能获得股份的是？', '2020-03-05 11:28:07', '1', '3678', '3', '/static/img/xiaoyang.jpeg', '2');
INSERT INTO `article` VALUES ('7', '为何诺手是lol上单唯一质检员？连他都打不过你还想打过谁！', 'Hello各位小伙伴们，众所周知在英雄联盟中，诺手是一个非常奇怪的英雄，在高玩看来这个英雄非常的容易被针对，q可以进内圈骗，e可以小技能躲，腿短还容易被秀，特别是瑞文高玩，每次看他们对线诺手，就跟打啥一样轻松无压力；但是在另一边诺手却是普通玩家最头疼的英雄，基础面板高，血怒加攻击，q还有回复，所以诺手这名英雄也被称为上单玩家的质检员。', '2020-03-05 11:28:09', '1', '7865', '3', '/static/img/nuoshou.jpeg', '2');

-- ----------------------------
-- Table structure for category
-- ----------------------------
DROP TABLE IF EXISTS `category`;
CREATE TABLE `category` (
  `cid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `num` int(11) DEFAULT '0',
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of category
-- ----------------------------
INSERT INTO `category` VALUES ('1', '游戏', '7');
INSERT INTO `category` VALUES ('2', '音乐', '0');
INSERT INTO `category` VALUES ('3', '运动', '0');
INSERT INTO `category` VALUES ('4', '电影', '0');

-- ----------------------------
-- Table structure for mark
-- ----------------------------
DROP TABLE IF EXISTS `mark`;
CREATE TABLE `mark` (
  `mid` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(1000) DEFAULT NULL,
  `creat_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `uid` int(11) DEFAULT NULL,
  PRIMARY KEY (`mid`),
  KEY `uid` (`uid`),
  CONSTRAINT `uid` FOREIGN KEY (`mid`) REFERENCES `user` (`uid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of mark
-- ----------------------------
INSERT INTO `mark` VALUES ('1', '大马猴66666', '2020-03-04 00:43:42', '1');
INSERT INTO `mark` VALUES ('2', '真是人间将太重', '2020-03-04 00:44:04', '1');
INSERT INTO `mark` VALUES ('3', '哈哈哈啊哈哈哈', '2020-03-05 09:41:24', '1');

-- ----------------------------
-- Table structure for tag
-- ----------------------------
DROP TABLE IF EXISTS `tag`;
CREATE TABLE `tag` (
  `tid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `aid` int(11) DEFAULT NULL,
  PRIMARY KEY (`tid`),
  KEY `aid` (`aid`),
  CONSTRAINT `aid` FOREIGN KEY (`aid`) REFERENCES `article` (`aid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tag
-- ----------------------------
INSERT INTO `tag` VALUES ('1', 'DNF', '1');
INSERT INTO `tag` VALUES ('2', 'LOL', '2');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `password` varchar(128) NOT NULL,
  `phone` varchar(11) NOT NULL,
  `email` varchar(200) DEFAULT NULL,
  `portrait` varchar(300) DEFAULT NULL,
  `regtime` datetime DEFAULT NULL,
  `isforbid` tinyint(4) DEFAULT '0',
  PRIMARY KEY (`uid`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1', 'ming', '123', '88888888888', 'ming@163.com', null, '2020-03-01 15:59:28', '0');
INSERT INTO `user` VALUES ('2', 'aehtsryj', '963852741', '13473586735', null, null, null, '0');
INSERT INTO `user` VALUES ('3', 'chenbin', '12345678', '13473586735', null, null, null, '0');
INSERT INTO `user` VALUES ('4', 'chenbinb', 'chenbin1997', '18730289787', null, null, null, '0');
INSERT INTO `user` VALUES ('5', 'sdafojaw', 'qwertyuiop', '18730289787', null, null, null, '0');
INSERT INTO `user` VALUES ('6', 'mingggg', 'qazwsxedc', '18730289787', null, null, null, '0');
INSERT INTO `user` VALUES ('7', '963258741', '789456123', '18730289787', null, null, null, '0');
