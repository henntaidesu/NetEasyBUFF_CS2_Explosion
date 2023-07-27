CREATE TABLE `assets` (
  `type` varchar(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `name` varchar(12) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `sum` int DEFAULT NULL,
  `value` int DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  KEY `1` (`type`,`name`,`sum`,`value`,`date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `BuffBuyHistory` (
  `weapon_name` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `item_name` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `weapon_float` double DEFAULT NULL,
  `float_range` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `price` float DEFAULT NULL,
  `bargain_price` float DEFAULT NULL,
  `seller_name` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `order_time` datetime(6) DEFAULT NULL,
  `status` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `storage_time` datetime(6) DEFAULT NULL,
  KEY `T` (`weapon_name`,`item_name`,`weapon_float`,`float_range`,`price`,`bargain_price`,`seller_name`,`order_time`,`status`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `BuffSellRecord` (
  `weapon_name` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `item_name` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `weapon_float` double DEFAULT NULL,
  `float_range` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `price` float DEFAULT NULL,
  `bargain_price` float DEFAULT NULL,
  `buyer_name` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `order_time` datetime DEFAULT NULL,
  `status` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `storage_time` datetime(6) DEFAULT NULL,
  KEY `T` (`weapon_name`,`item_name`,`weapon_float`,`float_range`,`price`,`bargain_price`,`buyer_name`,`order_time`,`status`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `funds` (
  `sources_of_funds` varchar(12) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT 'aliplay or wechatplay or steamplay',
  `type` varchar(3) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `amount` float DEFAULT NULL,
  `date` datetime(6) DEFAULT NULL,
  KEY `1` (`sources_of_funds`,`type`,`amount`,`date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
