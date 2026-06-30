-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Feb 20, 2025 at 03:14 AM
-- Server version: 5.7.26
-- PHP Version: 7.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `jewellery_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin_tb`
--

DROP TABLE IF EXISTS `admin_tb`;
CREATE TABLE IF NOT EXISTS `admin_tb` (
  `a_id` int(11) NOT NULL AUTO_INCREMENT,
  `a_username` varchar(20) NOT NULL,
  `a_password` varchar(20) NOT NULL,
  `a_image` varchar(100) NOT NULL,
  `a_lastseen` datetime NOT NULL,
  PRIMARY KEY (`a_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin_tb`
--

INSERT INTO `admin_tb` (`a_id`, `a_username`, `a_password`, `a_image`, `a_lastseen`) VALUES
(1, 'Riddhi', '263', 'user8-128x128.jpg', '2025-02-19 12:09:21');

-- --------------------------------------------------------

--
-- Table structure for table `cart_tb`
--

DROP TABLE IF EXISTS `cart_tb`;
CREATE TABLE IF NOT EXISTS `cart_tb` (
  `cart_id` int(11) NOT NULL AUTO_INCREMENT,
  `o_id` int(11) NOT NULL,
  `cat_id` int(11) NOT NULL,
  `sub_id` int(11) NOT NULL,
  `p_id` int(11) NOT NULL,
  `cart_price` int(11) NOT NULL,
  `cart_quantity` int(11) NOT NULL,
  `cart_totalprice` int(11) NOT NULL,
  `cart_status` enum('Active','Deactive') NOT NULL,
  `cart_cdate` datetime NOT NULL,
  `cart_udate` datetime NOT NULL,
  PRIMARY KEY (`cart_id`)
) ENGINE=MyISAM AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cart_tb`
--

INSERT INTO `cart_tb` (`cart_id`, `o_id`, `cat_id`, `sub_id`, `p_id`, `cart_price`, `cart_quantity`, `cart_totalprice`, `cart_status`, `cart_cdate`, `cart_udate`) VALUES
(1, 1, 6, 12, 55, 1899, 1, 1899, 'Deactive', '2025-02-12 12:07:36', '2025-02-12 12:08:29'),
(2, 1, 6, 14, 54, 3099, 2, 6198, 'Deactive', '2025-02-12 12:07:47', '2025-02-12 12:08:29'),
(3, 1, 2, 14, 42, 10099, 1, 10099, 'Deactive', '2025-02-12 12:07:56', '2025-02-12 12:08:29'),
(4, 3, 5, 12, 51, 1099, 2, 2198, 'Deactive', '2025-02-12 15:11:19', '2025-02-12 15:14:00'),
(5, 3, 5, 13, 49, 1599, 2, 3198, 'Deactive', '2025-02-12 15:11:28', '2025-02-12 15:14:00'),
(6, 4, 2, 14, 74, 2199, 2, 4398, 'Deactive', '2025-02-12 17:54:07', '2025-02-12 17:54:36'),
(7, 5, 2, 14, 74, 2199, 2, 4398, 'Deactive', '2025-02-13 09:29:28', '2025-02-13 09:30:03'),
(8, 6, 2, 14, 73, 1799, 2, 3598, 'Deactive', '2025-02-13 11:51:32', '2025-02-13 11:52:13'),
(9, 7, 1, 11, 67, 1799, 2, 3598, 'Deactive', '2025-02-13 14:25:59', '2025-02-13 14:27:20'),
(10, 8, 2, 14, 74, 2199, 3, 6597, 'Deactive', '2025-02-14 12:15:50', '2025-02-14 15:45:55'),
(11, 8, 2, 14, 42, 10099, 1, 10099, 'Deactive', '2025-02-14 15:40:59', '2025-02-14 15:45:55'),
(12, 9, 2, 12, 70, 2640, 1, 2640, 'Deactive', '2025-02-14 21:09:30', '2025-02-14 21:09:42'),
(13, 10, 1, 11, 67, 1799, 1, 1799, 'Deactive', '2025-02-15 11:58:00', '2025-02-15 11:58:52'),
(14, 11, 1, 11, 67, 1799, 2, 3598, 'Deactive', '2025-02-19 11:39:53', '2025-02-19 11:40:31'),
(15, 12, 2, 14, 74, 2199, 1, 2199, 'Deactive', '2025-02-19 11:54:35', '2025-02-19 11:54:45'),
(16, 13, 1, 11, 65, 15126, 1, 15126, 'Deactive', '2025-02-19 12:18:44', '2025-02-19 14:44:10'),
(17, 14, 2, 14, 74, 2199, 2, 4398, 'Deactive', '2025-02-19 12:20:44', '2025-02-19 12:21:19'),
(18, 15, 2, 14, 42, 10099, 1, 10099, 'Deactive', '2025-02-19 13:10:07', '2025-02-19 13:10:18'),
(19, 13, 2, 14, 74, 2199, 1, 2199, 'Deactive', '2025-02-19 14:30:16', '2025-02-19 14:44:10'),
(20, 16, 2, 12, 70, 2640, 1, 2640, 'Deactive', '2025-02-19 22:27:14', '2025-02-19 22:27:24'),
(21, 17, 2, 14, 74, 2199, 2, 4398, 'Active', '2025-02-20 00:07:48', '2025-02-20 00:18:19'),
(22, 17, 2, 12, 69, 2699, 1, 2699, 'Active', '2025-02-20 00:18:48', '2025-02-20 00:18:48');

-- --------------------------------------------------------

--
-- Table structure for table `category_tb`
--

DROP TABLE IF EXISTS `category_tb`;
CREATE TABLE IF NOT EXISTS `category_tb` (
  `cat_id` int(11) NOT NULL AUTO_INCREMENT,
  `cat_name` varchar(50) NOT NULL,
  `cat_image` varchar(100) NOT NULL,
  `cat_status` enum('Active','Deactive') NOT NULL,
  `cat_cdate` datetime NOT NULL,
  `cat_udate` datetime NOT NULL,
  PRIMARY KEY (`cat_id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `category_tb`
--

INSERT INTO `category_tb` (`cat_id`, `cat_name`, `cat_image`, `cat_status`, `cat_cdate`, `cat_udate`) VALUES
(1, 'Ring', 'cat5_lc7zJZ2.jpg', 'Active', '2024-12-16 17:01:50', '2025-01-31 13:31:17'),
(2, 'Necklace', 'cat1_PHcPxaS.jpg', 'Active', '2024-12-16 17:02:08', '2025-01-31 13:05:20'),
(3, 'Pendant', 'pendant.webp', 'Deactive', '2024-12-16 17:02:19', '2024-12-16 17:02:19'),
(4, 'Bracelet', 'cat2_tg7C5V3.jpg', 'Active', '2024-12-16 17:02:35', '2025-01-31 13:05:01'),
(5, 'Earring', 'cat3_VZJyhJ8.jpg', 'Active', '2024-12-16 17:02:47', '2025-01-31 13:07:32'),
(6, 'Anklet', 'cat4_GZrwdox.jpg', 'Active', '2024-12-16 17:03:11', '2025-01-31 13:04:28'),
(7, 'Bangle', 'cat6_ULTdAko.jpg', 'Deactive', '2024-12-16 17:03:33', '2025-01-31 13:32:17'),
(8, 'Chain', 'chain.webp', 'Deactive', '2024-12-16 17:03:51', '2024-12-16 17:03:51');

-- --------------------------------------------------------

--
-- Table structure for table `feedback_tb`
--

DROP TABLE IF EXISTS `feedback_tb`;
CREATE TABLE IF NOT EXISTS `feedback_tb` (
  `f_id` int(11) NOT NULL AUTO_INCREMENT,
  `f_name` varchar(50) NOT NULL,
  `f_contact` bigint(20) NOT NULL,
  `f_message` text NOT NULL,
  `f_status` enum('Show','Hide') NOT NULL,
  `f_cdate` datetime NOT NULL,
  `f_udate` datetime NOT NULL,
  PRIMARY KEY (`f_id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `feedback_tb`
--

INSERT INTO `feedback_tb` (`f_id`, `f_name`, `f_contact`, `f_message`, `f_status`, `f_cdate`, `f_udate`) VALUES
(9, 'Raval Riddhi', 9537074551, 'Beautifully crafted jewelry at reasonable prices. The product images and descriptions were spot on.', 'Show', '2025-01-31 12:11:42', '2025-01-31 12:11:42'),
(10, 'Raval Archana', 9909869820, 'Fast delivery and exceptional packaging. The jewelry looks even better in person.', 'Show', '2025-01-31 12:15:18', '2025-01-31 12:15:18'),
(8, 'Patel Dhruvi', 7572890125, 'Absolutely loved the collection. The designs are elegant and the craftsmanship is remarkable. Will definitely shop again.', 'Show', '2025-01-31 12:06:28', '2025-01-31 12:06:28');

-- --------------------------------------------------------

--
-- Table structure for table `order_tb`
--

DROP TABLE IF EXISTS `order_tb`;
CREATE TABLE IF NOT EXISTS `order_tb` (
  `o_id` int(11) NOT NULL AUTO_INCREMENT,
  `u_id` int(11) NOT NULL,
  `s_id` int(11) DEFAULT NULL,
  `p_id` int(11) DEFAULT NULL,
  `o_pincode` int(11) DEFAULT NULL,
  `o_quantity` int(11) NOT NULL,
  `o_total` int(11) NOT NULL,
  `o_shippingaddress` text,
  `o_status` enum('Pending','Confirm','Complete','Cancel','Cart') NOT NULL,
  `o_cdate` datetime NOT NULL,
  `o_udate` datetime NOT NULL,
  PRIMARY KEY (`o_id`)
) ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `order_tb`
--

INSERT INTO `order_tb` (`o_id`, `u_id`, `s_id`, `p_id`, `o_pincode`, `o_quantity`, `o_total`, `o_shippingaddress`, `o_status`, `o_cdate`, `o_udate`) VALUES
(1, 13, 8, NULL, 382021, 4, 18196, 'Plot no.212/F6 Harinam Flat sector-20', 'Confirm', '2025-02-12 12:07:36', '2025-02-12 12:08:29'),
(3, 14, 9, NULL, 382021, 4, 5396, 'Tulsingar Society Vijapur', 'Cancel', '2025-02-12 15:11:19', '2025-02-12 15:14:00'),
(4, 13, NULL, NULL, 382820, 2, 4398, 'Gandhinagar ', 'Pending', '2025-02-12 17:54:07', '2025-02-12 17:54:36'),
(5, 14, NULL, NULL, 382820, 2, 4398, 'Vijapur', 'Cancel', '2025-02-13 09:29:28', '2025-02-13 09:30:03'),
(6, 14, NULL, NULL, 382820, 2, 3598, 'Surat', 'Pending', '2025-02-13 11:51:32', '2025-02-13 11:52:13'),
(7, 14, NULL, NULL, 382820, 2, 3598, 'Vijapur,dghsavbdk9', 'Confirm', '2025-02-13 14:25:59', '2025-02-13 14:27:20'),
(8, 14, NULL, NULL, 382820, 4, 16696, 'ghsdb', 'Cancel', '2025-02-14 12:15:50', '2025-02-14 15:45:55'),
(9, 14, NULL, NULL, 382820, 1, 2640, 'Vijapur', 'Pending', '2025-02-14 21:09:30', '2025-02-14 21:09:42'),
(10, 14, NULL, NULL, 382820, 1, 1799, 'gfhjmyul', 'Cancel', '2025-02-15 11:58:00', '2025-02-15 11:58:52'),
(11, 14, NULL, NULL, 382820, 2, 3598, 'DEHGAM', 'Pending', '2025-02-19 11:39:53', '2025-02-19 11:40:31'),
(12, 14, NULL, NULL, 382820, 1, 2199, 'cgfuhij', 'Pending', '2025-02-19 11:54:35', '2025-02-19 11:54:45'),
(13, 14, NULL, NULL, 382820, 2, 17325, 'ygsalJ', 'Pending', '2025-02-19 12:18:44', '2025-02-19 14:44:10'),
(14, 13, NULL, NULL, 382820, 2, 4398, 'ertyu', 'Cancel', '2025-02-19 12:20:44', '2025-02-19 12:21:19'),
(15, 16, NULL, NULL, 382820, 1, 10099, 'Dehgaam ', 'Pending', '2025-02-19 13:10:07', '2025-02-19 13:10:18'),
(16, 14, NULL, NULL, 382820, 1, 2640, 'Mumbai', 'Cancel', '2025-02-19 22:27:14', '2025-02-19 22:27:24'),
(17, 14, NULL, NULL, NULL, 1, 2199, NULL, 'Cart', '2025-02-20 00:07:48', '2025-02-20 00:07:48');

-- --------------------------------------------------------

--
-- Table structure for table `payment_tb`
--

DROP TABLE IF EXISTS `payment_tb`;
CREATE TABLE IF NOT EXISTS `payment_tb` (
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `o_id` int(11) NOT NULL,
  `p_amount` int(11) NOT NULL,
  `p_status` enum('Success','Fail') NOT NULL,
  `p_cdate` datetime NOT NULL,
  PRIMARY KEY (`p_id`)
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `payment_tb`
--

INSERT INTO `payment_tb` (`p_id`, `o_id`, `p_amount`, `p_status`, `p_cdate`) VALUES
(1, 1, 18196, 'Success', '2025-02-12 12:08:29'),
(2, 3, 5396, 'Success', '2025-02-12 15:14:00'),
(3, 4, 4398, 'Success', '2025-02-12 17:54:36'),
(4, 5, 4398, 'Success', '2025-02-13 09:30:03'),
(5, 6, 3598, 'Success', '2025-02-13 11:52:13'),
(6, 7, 3598, 'Success', '2025-02-13 14:27:20'),
(7, 8, 16696, 'Success', '2025-02-14 15:45:55'),
(8, 9, 2640, 'Success', '2025-02-14 21:09:42'),
(9, 10, 1799, 'Success', '2025-02-15 11:58:52'),
(10, 11, 3598, 'Success', '2025-02-19 11:40:31'),
(11, 12, 2199, 'Success', '2025-02-19 11:54:45'),
(12, 14, 4398, 'Success', '2025-02-19 12:21:19'),
(13, 15, 10099, 'Success', '2025-02-19 13:10:18'),
(14, 13, 17325, 'Success', '2025-02-19 14:44:10'),
(15, 16, 2640, 'Success', '2025-02-19 22:27:24');

-- --------------------------------------------------------

--
-- Table structure for table `product_tb`
--

DROP TABLE IF EXISTS `product_tb`;
CREATE TABLE IF NOT EXISTS `product_tb` (
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `cat_id` int(11) NOT NULL,
  `sub_id` int(11) NOT NULL,
  `s_id` int(11) NOT NULL,
  `p_name` varchar(100) NOT NULL,
  `p_image` varchar(100) NOT NULL,
  `p_price` int(11) NOT NULL,
  `p_offerprice` int(11) NOT NULL,
  `p_details` text NOT NULL,
  `p_disclamier` text NOT NULL,
  `p_size` varchar(20) NOT NULL,
  `p_color` varchar(20) NOT NULL,
  `p_material` varchar(100) NOT NULL,
  `p_status` enum('Active','Deactive') NOT NULL,
  `p_cdate` datetime NOT NULL,
  `p_udate` datetime NOT NULL,
  PRIMARY KEY (`p_id`)
) ENGINE=MyISAM AUTO_INCREMENT=75 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `product_tb`
--

INSERT INTO `product_tb` (`p_id`, `cat_id`, `sub_id`, `s_id`, `p_name`, `p_image`, `p_price`, `p_offerprice`, `p_details`, `p_disclamier`, `p_size`, `p_color`, `p_material`, `p_status`, `p_cdate`, `p_udate`) VALUES
(2, 2, 2, 2, 'b', '', 450, 50, 'nothing', 'nooo', '2', 'red', 'gold', 'Deactive', '2024-12-08 00:00:00', '2024-12-08 00:00:00'),
(4, 2, 2, 2, 'Ring', '', 10000, 100, 'Noo', 'nothing', '2', 'gold', 'silver', 'Active', '2024-12-02 00:00:00', '2024-12-03 00:00:00'),
(13, 6, 12, 1, 'Silver Anklet', 'anklets1_Lry9RfN.webp', 3099, 10, 'We want to bring you jewellery that matches your charm Inspired by YOU this adorable Silver Zircon Charm Anklet is here to make you all the more enchanting.', 'This Silver Zircon Charm Anklet has been handcrafted with love, especially for YOU! With dragonflies, angel wings and other little trinkets on a silver body, this anklet a cute mix of old and new!\r\n\r\nThe Styling:\r\nCarry your charm around with you, always!\r\n\r\n21cm length+ 3cm adjustable portion\r\n925 Sterling Silver \r\nAnti-tarnish e-coated (with rhodium) \r\nComes with the GIVA Jewellery kit and authenticity certificate', '16', 'Silver', 'Metal', 'Active', '2025-01-18 15:48:39', '2025-01-18 16:37:04'),
(14, 7, 12, 1, 'Silver Cozy In Love Bracelet', 'bangle1_B2YxxDu.webp', 6699, 10, 'The Silver Cozy In Love Bracelet is inspired by the fuzzy feeling of being in love.', 'The silver bangle bracelet has a curvy design that meets at the centre forming an elegant design.\r\n925 Silver \r\nHypoallergenic - Perfect for sensitive skin\r\nDiameter of bracelet is 5.78 cm\r\nCharm dimensions: \r\nComes with the GIVA Jewellery kit and authenticity certificate\r\nNet Qty- 1 piece', '3', 'Silver', 'Silver', 'Active', '2025-01-18 15:53:25', '2025-01-18 16:40:56'),
(15, 8, 15, 1, 'The Shravya Gold Chain', 'chain1_QBA0kwp.webp', 101816, 10, 'The Rose Gold Elongated Link Chain Necklace is inspired by various bonds we make as human beings.', 'The rose gold necklace has elongated chain links as opposed to the conventional round ones.\r\n\r\n925 Silver with Rose Gold Plating\r\nLength: 40 cm + 5 Adjustable\r\nComes with the GIVA jewellery kit and authenticity certificate', '16', 'Yellow Gold', 'Metal', 'Active', '2025-01-18 15:56:50', '2025-01-18 16:09:02'),
(16, 5, 14, 1, 'Rose Gold Made for Each Other Stud Earrings', 'earring1_V89uaYs.webp', 1199, 20, 'Invoke the desires that are deeply set in your heart. These earrings are sure to make a delightful impression.', 'These rose gold earrings feature a heart motif with one-half adorning zircons.\r\n925 Silver with Rose Gold Plating\r\nPerfect for sensitive skin\r\nEarring Size: Height - 0.9 cm, Width - 1.2 cm\r\nComes with the GIVA Jewellery kit and authenticity certificate\r\nContent: Earrings\r\nNet Qty- 1 pair', '1', 'Baby Pink', 'Rose Gold', 'Active', '2025-01-18 15:59:19', '2025-01-18 16:28:35'),
(17, 4, 12, 1, 'Silver Infinity Heart Bracelet', 'bracelet1_MRize1P.webp', 2099, 10, 'The Silver Infinity Heart Bracelet is inspired by every second you spend with your soulmate every second that seems to encapsulate the whole of eternity.', 'The silver bracelet has a very elegant design of an infinity shape - studded with zircons and 3 smaller hearts juxtaposed into the shape.925 Silver\r\nPerfect for sensitive skin\r\nMotif Height: 0.9 cm , Width: 2.8 cm\r\nLength of chain: 15 cm + 4 cm Adjustable\r\nComes with the GIVA Jewellery kit and authenticity certificate\r\nContent: Bracelet\r\nNet Qty- 1 unit', '4', 'Silver', 'Metal', 'Active', '2025-01-18 16:01:28', '2025-01-18 16:39:41'),
(18, 4, 14, 1, 'Anushka Sharma Rose Gold Deer Bracelet', 'b2_bBjq3ZU.jpg', 2399, 20, 'The allure of the deer cannot go unappreciated hence this bracelet. You would love to try this.', 'This rose gold bracelet has a deer motif with zircon studded in it.\r\n\r\n925 Silver with Rose Gold Plating\r\nPerfect for sensitive skin\r\nDimension: 1.4 cm x 2.7 cm\r\nLength of chain: 17.5 cm + 3.5 cm Adjustable\r\nComes with the GIVA Jewellery kit and authenticity certificate\r\nContent: Bracelet\r\nNet Qty- 1 unit', '4', 'rose ', 'Rose Gold', 'Active', '2025-01-18 16:46:13', '2025-01-18 16:46:13'),
(19, 4, 13, 1, 'Made With 18K Gold And Lab-Grown ', 'b3_Grn6Ac9.webp', 59845, 10, 'This bracelet is a circle of affection embracing your wrist with charm. Ideal for wearing it every day', 'Featuring tiny lab diamond-studded stars this gold bracelet is pure magic\r\n', '4', 'Silver', 'Metal', 'Active', '2025-01-18 16:50:34', '2025-01-18 16:50:34'),
(20, 4, 11, 1, 'Made With 14K Gold And Lab-Grown Diamonds', 'b4_GYnTB9E.webp', 58249, 20, 'This pure gold cuff bracelet features an arrow-like design with lab-grown diamonds.', 'Our 14K solid gold pieces are made to last forever. It doesnt discolour so go ahead wear it every day.\r\n', '4', 'Yellow ', 'Gold', 'Active', '2025-01-18 16:53:49', '2025-01-18 16:53:49'),
(21, 5, 12, 1, 'Silver Pop Pink Studded Butterfly Studs', 'e1_ICt2HKT.webp', 1099, 20, 'We got something perfect for the colour enthusiasts! Gift these studs to make their day special.', 'These silver studs feature a butterfly motif with a pink coloured stone placed at the centre and butterfly wings studded with zircons.', '3', 'silver', 'Silver', 'Active', '2025-01-18 16:56:41', '2025-01-18 16:56:41'),
(22, 5, 13, 1, 'Silver Diamond Quad Stud Earrings', 'e2_WhgYWaA.webp', 8999, 20, 'The Silver Diamond Quad Stud Earrings are inspired by the sparkling symmetry amping up your looks.', 'Style these with a sheer floral blouse and blue denim.', '1', 'Silver', 'Metal', 'Active', '2025-01-18 16:58:26', '2025-01-18 16:58:26'),
(23, 5, 11, 1, 'Golden Trifecta Earrings', 'e3_dNaiKbD.webp', 1299, 10, 'The carefully designed trinity of elements creates an eye catching symphony making these earrings a standout choice for any occasion.', 'These golden earrings have a triple loop design set with zircons.', '1', 'Yellow ', 'Gold', 'Active', '2025-01-18 17:00:26', '2025-01-18 17:00:26'),
(24, 6, 14, 1, 'Rose Gold And Golden Cable Chain Anklet', 'a1_6AgcuGj.webp', 1799, 10, 'A dance of hues and links that whispers tales of glamour and grace. Indulge in the luxury of self expression.', 'This dual tone anklet has a rose gold and golden plating featuring cable chain design.', '4', 'rose ', 'Gold', 'Active', '2025-01-18 17:02:41', '2025-01-18 17:02:41'),
(25, 6, 11, 1, 'Rose Gold Geometric Anklet', 'a2_oXXRAUZ.webp', 6499, 20, 'The Rose Gold Geometric Anklet is inspired by the beauty of the setting sun behind snow capped mountains.', 'This anklet has a unique design of alternating circles and squares.', '4', 'Yellow ', 'Gold', 'Active', '2025-01-18 17:05:08', '2025-01-18 17:05:08'),
(26, 7, 11, 1, 'Made With 14K Gold', 'b1_JHiohi0.webp', 63631, 20, 'Adorned with diamonds inspired by the perfect harmony of strength and brilliance just like you.', 'This rose gold bracelet follows an open bangle design. The ends have a mesh like design accentuated with smaller lab diamonds and a bigger one at the top.', '4', 'Yellow ', 'Gold', 'Active', '2025-01-18 17:07:41', '2025-01-18 17:07:41'),
(27, 8, 14, 1, 'Rose Gold Sparkling Infinity Necklace', 'c1_PZxIuTI.webp', 1999, 10, 'This necklace can be a great way of telling your sweetheart that you love her to infinity and beyond. It sure will be a special gift.\r\n', 'This rose gold necklace features a heart motif studded with zircons and an infinity motif interconnected.', '4', 'rose ', 'Metal', 'Active', '2025-01-18 17:09:42', '2025-01-18 17:09:42'),
(28, 2, 12, 1, 'Silver Glittering Hexagon Necklace', 'n1_C1YvRj3.webp', 4999, 10, 'Add a touch of modern elegance to your style with this Silver Glittering Hexagon Necklace where sophistication meets sparkle in every facet.', 'This silver necklace has a knotted chain design with zircons.\r\n925 Silver \r\nPerfect for sensitive skin\r\nLength of chain: 40 cm + 7 cm Adjustable\r\nComes with the GIVA Jewellery kit and authenticity certificate\r\nContent: Necklace\r\nNet Qty- 1 unit', '4', 'Silver', ' Bottle green', 'Active', '2025-01-31 13:39:09', '2025-01-31 13:39:09'),
(29, 2, 14, 1, 'Rose Gold Floral Splurge Necklace', 'n2_Wh9pmdl.webp', 10099, 10, 'Embrace the splendour of the floral beauty with this necklace. A perfect accessory for your special occasions from daytime events to glamorous evenings.', 'This rose gold necklace has floral motifs with a pear drop dangler in the centre, all studded with zircons.\r\n\r\n925 Silver with Rose Gold Plating\r\nPerfect for sensitive skin\r\nLength of chain: 40.5 cm + 8 cm Adjustable\r\nComes with the GIVA Jewellery kit and authenticity certificate\r\nContent: Necklace\r\nNet Qty- 1 unit', '4', ' Pink', ' Red palazzo', 'Active', '2025-01-31 13:42:02', '2025-01-31 13:42:02'),
(30, 2, 13, 1, 'Solitaire Necklace', 'n3_balk2FI.webp', 7699, 10, 'Solitaire Set Necklace is inspired by the unbreakable bond between two friends.\r\n', 'The silver necklace is entirely studded with American diamonds\r\n\r\nIncludes 18\" + 1\" adjustable 925 Silver Chain\r\nAAA+ Quality Zircons\r\nRhodium finish to prevent tarnish \r\nComes with the GIVA Jewellery kit and authenticity certificate\r\n', '4', 'Silver', 'Platanium', 'Active', '2025-01-31 13:45:50', '2025-01-31 13:45:50'),
(31, 2, 11, 1, 'Golden Zircon Shine Elegant Necklace', 'n4_DcuRvRf.webp', 7299, 10, 'The Golden Zircon Shine Elegant Necklace is inspired by the delicate facets of glittering lights during festivals.', 'The golden necklace has a beautiful design that features marquise-shaped structures studded with zircons and a pear-shaped charm dangling from the centre.\r\n925 Silver with Gold Plating\r\nPerfect for sensitive skin\r\nDimensions: 1.8 cm x 0.8 cm\r\nThe necklace size is 42 cm and the adjustable chain is 5 cm\r\nComes with the GIVA Jewellery kit and authenticity certificate\r\nNet Qty- 1 piece\r\n', '4', 'Yellow', 'Gold', 'Active', '2025-01-31 13:49:17', '2025-01-31 13:49:17'),
(32, 1, 12, 1, 'Silver Zircon Layered Ring', 'r1_lrumQef.webp', 1799, 5, 'This ring is a perfect blend of class and trend exclusively made for ring lovers. It is an ideal treat for yourself.\r\n', 'This silver ring has a zircon centrepiece nestled in alternating layers adorned with zircons.\r\n\r\n925 Silver \r\nPerfect for sensitive skin\r\nAdjustable size to ensure no fitting issues', '5', 'Metal', 'Silver', 'Active', '2025-01-31 13:55:35', '2025-01-31 13:55:35'),
(33, 1, 14, 1, 'Rose Gold Flamme Ring', 'r2_UHYfnz5.webp', 799, 5, 'This ring embodies brightness  boldness and beauty offering you the perfect combination of all three.', 'This rose gold ring features a rhombus motif at the centre with two oval designs on both sides studded with zircons.\r\n925 Silver with Rose Gold Plating\r\nDiameter: 1.62 cm \r\nFixed Size\r\nRing size: Indian - 11\r\nComes with the GIVA Jewellery kit and authenticity certificate\r\nContent: Ring\r\nNet Qty- 1', '5', 'Pink', 'Rose Gold', 'Active', '2025-01-31 13:58:42', '2025-01-31 13:58:42'),
(34, 1, 13, 1, 'Platanium Flower design ring', 'r3_AxWHMLP.webp', 26207, 10, 'The White Platanium Tender Romance Ring is inspired by the blush of a first romance.', 'This ring features a flower motif set .\r\n\r\nBIS-Hallmarked Platanium Jewellery\r\nOur 14K solid platanium pieces are made to last forever. 14K gold will not oxidise or discolour so you can wear your jewellery daily.\r\n', '5', 'Metal', 'Silver', 'Active', '2025-01-31 14:03:55', '2025-01-31 14:03:55'),
(35, 1, 11, 1, 'Made With 18K Gold And Lab-Grown Diamonds', 'r4_vVUw2gc.webp', 17145, 10, 'Gold and diamonds darling  because ordinary just is not your style. Make this stunning ring yours today', 'Featuring an open design the gold ring band meets itself in the form of a wave. One side of the band features lab diamonds.\r\n\r\nBIS-Hallmarked Gold Jewellery\r\nLab-grown diamonds\r\nOur 18K solid gold pieces are made to last forever. It does not discolour so go ahead ear it every day.\r\nRing Diameter: 1.62 cm\r\nRing size: Indian - 11\r\nFixed Size\r\nContent: Ring\r\nNet Qty- 1 unit\r\n', '5', 'Yellow', 'Gold', 'Active', '2025-01-31 14:06:24', '2025-01-31 14:06:24'),
(36, 1, 11, 8, ' Lab-Grown Diamonds', 'r4_U1sRInc.webp', 17145, 10, 'Gold and diamonds darling  because ordinary just is not your style. Make this stunning ring yours today\r\n', 'Featuring an open design the gold ring band meets itself in the form of a wave. One side of the band features lab diamonds.\r\n\r\nBIS Hallmarked Gold Jewellery\r\nLab-grown diamonds\r\nOur 18K solid gold pieces are made to last forever. It does not discolour so go ahead wear it every day.\r\nRing Diameter: 1.62 cm\r\nRing size: Indian - 11\r\nFixed Size\r\nComes with the GIVA Jewellery kit and authenticity certificate\r\nContent: Ring\r\nNet Qty- 1 unit', '5', 'Yellow ', 'Gold', 'Active', '2025-01-31 14:16:28', '2025-01-31 14:25:32'),
(37, 1, 13, 8, 'Platanium Flower design ring', 'r3_FCV9tMy.webp', 26207, 10, 'The White Platanium Tender Romance  Ring is inspired by the blush of a first romance.', 'This ring features a flower motif set with platanium.\r\n\r\nBIS Hallmarked Gold Jewellery\r\nLab silver\r\nOur 14K solid platanium pieces are made to last forever. 14K will not oxidise or discolour so you can wear your jewellery daily.', '5', 'Metal', 'Silver', 'Active', '2025-01-31 14:19:11', '2025-01-31 14:19:11'),
(38, 1, 14, 8, 'Rose Gold Flamme Ring', 'r2_Aq4T8SE.webp', 799, 5, 'This ring embodies brightness boldness and beauty offering you the perfect combination of all three.', 'This rose gold ring features a rhombus motif at the centre with two oval designs on both sides studded with zircons.\r\n925 Silver with Rose Gold Plating\r\nDiameter: 1.62 cm \r\nFixed Size\r\nRing size: Indian 11\r\nComes with the  Jewellery kit and authenticity certificate\r\nContent: Ring\r\nNet Qty- 1', '5', 'Baby Pink', 'Rose Gold', 'Active', '2025-01-31 14:21:36', '2025-01-31 14:21:36'),
(39, 1, 12, 8, 'Silver Zircon Layered Ring', 'r1_WuNd1Mb.webp', 1799, 5, 'This ring is a perfect blend of class and trend exclusively made for ring lovers. It is  an ideal treat for yourself.', 'This silver ring has a zircon centrepiece nestled in alternating layers adorned with zircons.\r\n\r\n925 Silver \r\nPerfect for sensitive skin\r\nAdjustable size to ensure no fitting issues\r\nRing Diameter: 1.8 cm Adjustable\r\nComes with the  Jewellery kit and authenticity certificate\r\nContent: Ring\r\nNet Qty  1 unit', '5', 'Metal', 'Silver', 'Active', '2025-01-31 14:24:35', '2025-01-31 14:24:35'),
(40, 2, 11, 8, 'Shine Elegant Necklace', 'n4_e2WSGw2.webp', 7299, 5, 'The Golden Zircon Shine Elegant Necklace is inspired by the delicate facets of glittering lights during festivals.', 'The golden necklace has a beautiful design that features marquise shaped structures studded with zircons and a pear shaped charm dangling from the centre.\r\n925 Silver with Gold Plating\r\nPerfect for sensitive skin\r\nDimensions: 1.8 cm  0.8 cm\r\nThe necklace size is 42 cm and the adjustable chain is 5 cm\r\nComes with the  Jewellery kit and authenticity certificate\r\nNet Qty 1 piece', '5', 'Yellow ', 'Gold', 'Active', '2025-01-31 14:28:04', '2025-01-31 14:39:10'),
(41, 2, 13, 8, ' Solitaire Necklace', 'n3_QrUR9Oj.webp', 7699, 5, 'Solitaire Set Necklace is inspired by the unbreakable bond between two friends.\r\n', 'The silver necklace is entirely studded with American diamonds\r\n\r\nIncludes 18 1 adjustable 925 Silver Chain\r\nAAA  Quality Zircons\r\nRhodium finish to prevent tarnish', '2', 'Metal', 'Platanium', 'Active', '2025-01-31 14:31:59', '2025-01-31 14:38:34'),
(42, 2, 14, 8, 'Floral Splurge Necklace', 'n2_MQcTN4E.webp', 10099, 10, 'Embrace the splendour of the floral beauty with this necklace. A perfect accessory for your special occasions from daytime events to glamorous evenings.', 'This rose gold necklace has floral motifs with a pear drop dangler in the centre all studded with zircons.\r\n\r\n925 Silver with Rose Gold Plating\r\nPerfect for sensitive skin\r\nLength of chain: 40.5 cm  8 cm Adjustable', '2', 'Baby Pink', 'Rose Gold', 'Active', '2025-01-31 14:35:20', '2025-01-31 14:39:32'),
(43, 2, 12, 8, ' Hexagon Necklace', 'n1_SbPXXq4.webp', 4999, 5, 'Add a touch of modern elegance to your style with this Silver Glittering Hexagon Necklace where sophistication meets sparkle in every facet.', 'This silver necklace has a knotted chain design with zircons.\r\n925 Silver \r\nPerfect for sensitive skin\r\nLength of chain: 40 cm  7 cm Adjustable\r\n', '2', 'Metal', 'Silver', 'Active', '2025-01-31 14:37:32', '2025-01-31 14:39:51'),
(44, 4, 11, 8, 'Lab-Grown Diamonds', 'b4_4wT8k8J.webp', 58804, 10, 'This pure gold cuff bracelet features an arrow-like design with lab-grown diamonds.', 'BIS Hallmarked Gold Jewellery\r\nLab grown diamonds\r\nOur 14K solid gold pieces are made to last forever. It do not discolour so go ahead wear it every day.\r\nDiameter: 6 cm\r\nComes with the  Jewellery kit and authenticity certificate\r\nContent: Bracelet\r\nNet Qtyn1 unit', '4', 'Yellow ', 'Gold', 'Active', '2025-01-31 21:25:58', '2025-01-31 21:25:58'),
(45, 4, 13, 8, 'Platinum Bracelet', 'b3_0JAUWTH.webp', 2699, 5, 'Treat yourself or surprise someone special with this timeless and beautiful bracelet that is sure to be cherished for years to come.\r\n', 'This silver tennis bracelet features three flower motifs each with a blue coloured stone while the chain is studded with zircons.\r\n925 Silver \r\nPerfect for sensitive skin\r\nLength of chain: 15 cm  4 cm Adjustable\r\nComes with the  Jewellery kit and authenticity certificate\r\nContent: Bracelet\r\nNet Qty 1 unit', '2', 'Silver', 'Platinum', 'Active', '2025-01-31 21:29:45', '2025-01-31 21:44:08'),
(46, 4, 14, 8, 'Rose Gold Bracelet', 'b2_3XZUcdR.webp', 1699, 5, 'Flaunt a versatile bracelet that complements your every mood. Wear it alone or stack it the choice is yours', 'This rose gold bracelet features a link chain motif.\r\n\r\n925 Silver with Rose Gold Plating\r\nPerfect for sensitive skin\r\nLength of Chain: 15 cm  5 cm Adjustable\r\nComes with the  Jewellery kit and authenticity certificate\r\nContent: Bracelet\r\nNet Qty 1 unit', '2', 'Baby Pink', 'Rose Gold', 'Active', '2025-01-31 21:31:37', '2025-01-31 21:43:46'),
(47, 4, 12, 8, 'Silver Falling Dew Bracelet', 'b1_XaU6yBZ.webp', 1299, 5, 'The Silver Falling Dew Bracelet is inspired by shiny dew drops that nestle on flower petals in the early morning.', 'This silver bracelet has a dew drop design with a zircon placed at the centre.\r\n925 Silver \r\nPerfect for sensitive skin\r\nLength of chain: 15 cm  4 cm Adjustable\r\nMotif Height: 0.7 cm, Width: 1.7 cm\r\nComes with the  Jewellery kit and authenticity certificate\r\nContent: Bracelet\r\nNet Qty 1 unit', '2', 'Metal', 'Silver', 'Active', '2025-01-31 21:33:19', '2025-01-31 21:33:19'),
(48, 5, 11, 9, 'Lab-Grown Diamonds', 'e4_8cCb0OZ.webp', 23809, 10, 'These earrings are inspired by natures caress and are a classic piece with an elegant design', 'These gold earrings feature an interconnected dual drop motif  one of gold and one set in diamonds.\r\n\r\nBIS Hallmarked Gold Jewellery\r\nLab grown diamonds\r\nOur 14K solid gold pieces are made to last forever. It do not discolour so go ahead wear it every day.\r\nEarring Size: Height - 1.17 cm Earring Width - 0.78 cm\r\nComes with the  Jewellery kit and authenticity certificate\r\nContent: Earrings\r\nNet Qty 1 pair', '2', 'Yellow ', 'Gold', 'Active', '2025-02-01 09:24:27', '2025-02-01 09:25:34'),
(49, 5, 13, 9, 'Platinum Glistening Earrings', 'e3_fzv92oV.webp', 1599, 10, 'These Platinum Diamond Studs are handcrafted with love especially for you The design is fashionable and charming just like the gent meant to wear them.', 'AAA Quality Zircon Stones\r\n925 Sterling Platinum \r\nRhodium e coat to prevent tarnish \r\nComes with the  Jewellery kit and authenticity certificate', '2', 'Silver', 'Platinum', 'Active', '2025-02-01 09:27:59', '2025-02-01 09:33:20'),
(50, 5, 14, 9, 'Rose Gold Made earring', 'e2_t6Mjcjn.webp', 1199, 10, 'Invoke the desires that are deeply set in your heart. These earrings are sure to make a delightful impression.', 'These rose gold earrings feature a heart motif with one-half adorning zircons.\r\n925 Silver with Rose Gold Plating\r\nPerfect for sensitive skin\r\nEarring Size: Height 0.9 m Width  1.2 cm\r\nComes with the Jewellery kit and authenticity certificate', '2', 'Baby Pink', 'Rose Gold', 'Active', '2025-02-01 09:29:43', '2025-02-01 09:29:43'),
(51, 5, 12, 9, 'Silver Zircon  Earrings', 'e1_987VB1u.webp', 1099, 10, 'These silver earrings have a hexagonal shape with a zircon placed', '925 Silver \r\nPerfect for sensitive skin\r\nEarring Size: Height  0.5 cm Width  0.5 cm\r\nComes with the  Jewellery kit and authenticity certificate\r\nContent: Earrings', '2', 'Metal', 'Silver', 'Active', '2025-02-01 09:32:20', '2025-02-01 09:32:53'),
(52, 6, 11, 9, 'Golden Star Anklet', 'e4_vAsiohv.webp', 2399, 10, 'This golden anklet has a very elegant design with a gorgeous star design studded with zircons.', '925 Silver with Gold Plating\r\nPerfect for sensitive skin\r\nLength of Chain: 25 cm 5 cm Adjustable\r\nMotif Height: 0.5 cm Width: 0.6 cm\r\nComes with the Jewellery kit and authenticity certificate\r\nContent: Anklet', '3', 'Yellow ', 'Gold', 'Active', '2025-02-01 09:38:19', '2025-02-01 09:38:19'),
(53, 6, 13, 9, 'Platinum Zircon Anklet', 'e3_KpqMgeC.webp', 6499, 10, 'This platinum anklet has square motifs studded with zircons.', '925 Silver \r\nPerfect for sensitive skin\r\nLength of Chain: 23 cm  3 cm Adjustable\r\nComes with the Jewellery kit and authenticity certificate\r\nContent: Anklet', '3', 'Silver', 'Platinum', 'Active', '2025-02-01 09:40:00', '2025-02-01 09:40:00'),
(54, 6, 14, 9, 'Rose Gold Anklet', 'e2_0nIrk0a.webp', 3099, 10, 'This rose gold anklet features a dual layer design with zircons dangling.', '925 Silver with Rose Gold Plating\r\nPerfect for sensitive skin\r\nLength of Chain: 25 cm  5 cm Adjustable\r\nComes with the  Jewellery kit and authenticity certificate\r\nContent: Anklet', '3', 'Baby Pink', 'Rose Gold', 'Active', '2025-02-01 09:41:16', '2025-02-01 09:41:16'),
(55, 6, 12, 9, 'Silver Pearls Anklet', 'a1_HLeUydr.webp', 1899, 10, 'This silver anklet features a floral motif in the centre of the chain along with two pearls on its side.', '925 Silver \r\nPerfect for sensitive skin\r\nLength of Chain: 25 cm  4 cm Adjustable\r\nComes with the Jewellery kit and authenticity certificate\r\nContent: Anklet', '3', 'Metal', 'Silver', 'Active', '2025-02-01 09:42:43', '2025-02-01 09:43:45'),
(56, 1, 12, 8, 'Silver Flamme Ring', 'rs1_SHiJrPu.webp', 799, 10, 'This ring embodies brightness boldness and beauty offering you the perfect combination of all three.', 'This silver ring features a rhombus motif at the center with two oval designs on both sides studded with zircons.\r\n925 Silver \r\nDiameter: 1.62 cm \r\nFixed Size\r\nRing size: Indian 11\r\nComes with the Jewellery kit and authenticity certificate\r\nContent: Ring', '4', 'Metal', 'Silver', 'Active', '2025-02-12 16:00:46', '2025-02-12 16:00:46'),
(57, 1, 12, 8, 'Zircon Queen of Venus Ring', 'rs2_BCAHafx.webp', 799, 10, 'If women are really from Venus then you are its Queen. Wear this minimalistic ring to remind yourself of the simple joys in live.\r\n', 'This silver ring has a circle motif at the centre with zircon placed in it.\r\n\r\n925 Silver \r\nPerfect for sensitive skin\r\nRing Diameter: 1.7 cm \r\nRing size: Indian - 12 US - 6\r\nComes with the Jewellery kit and authenticity certificate\r\nContent: Ring', '5', 'Metal', 'Silver', 'Active', '2025-02-12 16:03:08', '2025-02-12 16:07:57'),
(58, 1, 12, 8, 'Zircon Channel of Love Ring', 'rs3_uSZOEiP.webp', 1599, 10, 'So unique so sleek and so stylish. Channelise these three factors of beauty with this Channel of Love ring. This could be a perfect gift for your bestie', 'This gorgeous silver ring has zircon studded in the band.\r\n925 Silver \r\nPerfect for sensitive skin\r\nAdjustable size to ensure no fitting issues\r\nRing Diameter: 1.7 cm + Adjustable\r\nComes with the Jewellery kit and authenticity certificate\r\nContent: Ring', '6', 'Metal', 'Silver', 'Active', '2025-02-12 16:06:26', '2025-02-12 16:07:32'),
(59, 1, 14, 8, 'Rose Gold Floral Chic Ring', 'rr1_WPOF7a6.webp', 1699, 10, 'The Rose Gold Floral Glory Ring is inspired by the demure style of a girl that only gets accentuated with exquisite finery.\r\n', 'The Rose Gold Floral Glory Ring has a lovely floral design with studded zircons.\r\n925 Sterling Silver with Rose Gold plating\r\nAdjustable size to ensure no fitting issues\r\nAAA+ Quality Zircons\r\nDiameter: 18mm + top Adjustable \r\nMotif: 12 x 7.5 mm ', '4', 'Baby Pink', 'Rose Gold', 'Active', '2025-02-12 16:11:45', '2025-02-12 16:11:45'),
(60, 1, 14, 8, ' Timeless Elegant Ring', 'rr2_ORbR3in.webp', 2099, 10, 'A design that marries tradition with a modern twist perfect for the one who loves the best of both worlds.', 'This rose gold ring for women features a circle design zircon at the centre.\r\n\r\n925 Silver with Rose Gold Plating\r\nPerfect for sensitive skin\r\nAdjustable size to ensure no fitting issues\r\nRing Diameter: 1.66 cm + Adjustable\r\nRing size: Indian - 12', '5', 'Baby Pink', 'Rose Gold', 'Active', '2025-02-12 16:15:51', '2025-02-12 16:15:51'),
(61, 1, 14, 8, ' Classic Solitaire Ring', 'rr3_GkAeXl4.jpg', 2999, 10, 'The Rose Gold Classic Solitaire Ring is inspired by a graceful symphony of sophistication and refinement adorning you with timeless allure and captivating charm.', 'This ring has a gorgeous rectangular motif with a big zircon at the centre and small zircons on both sides.\r\n\r\n925 Silver With Rose Gold Plating\r\nPerfect for sensitive skin\r\nAdjustable size to ensure no fitting issues\r\nRing Diameter: 1.8 cm + Adjustable\r\nContent: Ring', '6', 'Baby Pink', 'Rose Gold', 'Active', '2025-02-12 16:18:01', '2025-02-12 16:18:01'),
(62, 1, 13, 8, 'Refined Solitaire Ring', 'rp1_gvOXz1N.webp', 1899, 10, 'Born out of a refined art this solitaire style ring exhibits magnificence in an unparalleled combination of style and splendour. Pretty yourself up with this gorgeous piece.', 'This silver ring highlights a single stone zircon upon prong setting stemming from a band of alternate zircons.\r\n925 Silver \r\nPerfect for sensitive skin\r\nRing Diameter: 1.7 cm \r\nRing size: Indian - 12 US - 6', '4', 'Metal', 'Silver', 'Active', '2025-02-12 16:22:15', '2025-02-12 16:22:15'),
(63, 1, 13, 8, 'Platinum Lab-Grown ', 'rp2_2UGrsdo.webp', 71148, 10, 'Even if you are not a jewellery person this ring will surprise you. Try it once you will love it.', 'This pure rose gold ring features a flower motif with lab-grown diamonds.\r\n\r\nLab grown diamonds\r\n It does not discolour so go ahead wear it every day.\r\nRing Diameter: 1.66 cm\r\nRing size: Indian - 12\r\nFixed Size', '5', 'Metal', 'Silver', 'Active', '2025-02-12 16:25:07', '2025-02-12 16:30:23'),
(64, 1, 13, 8, ' Lab Grown Diamonds', 'rp3_bWWG5ni.webp', 28045, 10, 'For the moments you need to feel like the queen of your own story this ring crowns your hand with grace.', 'This pure rose gold ring features a classic two-row design studded with lab grown diamonds.\r\n\r\nLab-grown diamonds\r\n It does not discolour so go ahead, wear it every day.\r\nRing Diameter: 1.66 cm\r\nRing size: Indian - 12\r\nFixed Size', '6', 'Metal', 'Silver', 'Active', '2025-02-12 16:29:43', '2025-02-12 16:29:43'),
(65, 1, 11, 8, 'Gold And Lab ring', 'rg1_l0WBMYq.webp', 15126, 10, 'Style this gold  diamond ring with a floral printed yellow dress.', 'This gold ring has a leaf motif studded with lab grown diamonds.\r\n\r\nLab-grown diamonds\r\nOur 14K solid gold pieces are made to last forever. 14K gold will not oxidise or discolour so you can wear your jewellery daily.\r\nRing Diameter: 1.7 cm\r\nRing size: Indian 12 US  6\r\nFixed Size', '4', 'Yellow ', 'Gold', 'Active', '2025-02-12 16:34:10', '2025-02-12 16:34:10'),
(66, 1, 11, 8, 'Made With 14K Gold', 'rg2_23wGr4F.webp', 13819, 10, 'A bit of magic is all you need to brighten up the day. This simple yet stylish ring can easily help you elevate your everyday look.', 'This gold ring features an open-ring design with one side adorned by a trio of lab grown diamonds leaf motifs while the other end is embellished with another single stone lab grown diamond.', '5', 'Yellow ', 'Gold', 'Active', '2025-02-12 16:36:29', '2025-02-12 16:36:29'),
(67, 1, 11, 8, 'Golden Flower Girl Ring', 'rg3_vpyAxSR.webp', 1799, 10, 'The Golden Flower Girl Ring is inspired by the demure style of a girl that only gets accentuated with exquisite finery.\r\n', 'The Gold Plated Flower Girl Ring has a lovely floral design with studded zircons.\r\n925 Sterling Silver with Gold plating \r\nAdjustable size to ensure no fitting issues\r\nAAA+ Quality Zircons\r\nDiameter: 18mm + top Adjustable\r\nMotif: 12 x 7.5 mm ', '6', 'Yellow ', 'Gold', 'Active', '2025-02-12 16:38:42', '2025-02-12 16:38:42'),
(68, 2, 12, 8, 'Anushka Sharma Silver Leaf ', 'ns1_tT8irqn.webp', 1999, 10, 'Feel the beautiful breeze with the rustle of the leaves filling the air. This necklace will make a memorable present for your dear ones.', '925 Silver\r\nPerfect for sensitive skin\r\nLength of chain: 43 cm + 6 cm Adjustable\r\nMotif Height: 1 cm Width: 3.1 cm ', 'Free Size', 'Metal', 'Silver', 'Active', '2025-02-12 16:43:17', '2025-02-12 16:43:17'),
(69, 2, 12, 8, '', 'ns2_YNbGLVE.webp', 2699, 10, 'The Silver Whimsical Charms Necklace is inspired by natures spring dance and the joy of small things.\r\n', 'This silver necklace features an intricately arranged butterfly on a chain.\r\n925 Silver\r\nPerfect for sensitive skin\r\nThe necklace size is 41 cm and the adjustable chain is 6 cm\r\nMotif Height: 0.5 cm, Width: 0.7 cm', 'Free Size', 'Metal', 'Silver', 'Active', '2025-02-12 16:45:07', '2025-02-12 16:45:07'),
(70, 2, 12, 8, 'Silver Plated Necklace Set', 'ns3_s4OKUmZ.jpg', 2640, 10, 'Experience the captivating beauty of this exquisite oxidized silver necklace and earring set, a timeless piece that exudes elegance and grace. The necklace, a masterpiece of intricate design, features a delicate cascade of sparkling stones, resembling a blossoming rose garden. The warm glow of the oxidized silver creates a luxurious and timeless appeal, making it a true statement piece. The matching earrings, adorned with shimmering stones and intricate details, perfectly complement the necklace, creating a harmonious and captivating ensemble. This set is more than just jewelry it is a wearable work of art that will elevate any outfit and make you feel truly special.', 'Base Metal:\r\nBrass\r\n\r\nWeight:\r\n40 g\r\n\r\nSales Package:\r\n1 Necklace and 1 Pair of Earrings\r\n\r\nEarring Length:\r\nMed(Ear lobe size)\r\n\r\nNecklace Type:\r\nChoker\r\n\r\nColor:\r\nSilver, Sea Green\r\n\r\nIdeal For:\r\nGirls, Women\r\n\r\nNecklace Clasp Type:\r\nS-hook\r\n\r\nCollection:\r\nEthnic\r\n\r\nTrend:\r\nAmerican Diamond Jewellery, Handcrafted, Ethnic Choker\r\n\r\nOccasion:\r\nWedding, Party Wear, Religions, Love, Function, Engagement, Ethnic Party\r\n\r\nEarring Type:\r\nStud Earring\r\n\r\nPolish:\r\nSilver Polish', 'Free Size', 'Metal', 'Silver', 'Active', '2025-02-12 17:13:56', '2025-02-12 17:13:56'),
(71, 2, 14, 8, 'Baby Pink Beaded Necklace', 'nr1_V6ZKORc.webp', 2550, 10, 'It is a jewellery set fit for the queens Exude the royal vibe with this stone studded jewellery set. Consisting of a necklace, matching earrings, this necklace set is crafted from rose gold plated brass, stones and beads Occasion Bring your style to a whole new level with this handcrafted piece of jewellery. When you are celebrating a special Occasion a birthday, wedding, or personal milestone  this piece adds that extra something that makes us feel special and looking our best.', 'Weight:\r\n40 g\r\n\r\nWarranty:\r\n6 Month\r\n\r\nSales Package:\r\n1 Necklace and 1 Pair of Earrings\r\n\r\nEarring Length:\r\nSmall(smaller than ear lobe)\r\n\r\nNecklace Type:\r\nChoker\r\n\r\nColor:\r\nRose Gold, Baby Pink\r\n\r\nIdeal For:\r\nGirls, Women\r\n\r\nNecklace Clasp Type:\r\nS hook\r\n\r\nCollection:\r\nContemporary\r\n\r\nTrend:\r\nAmerican Diamond Jewellery, Contemporary Choker\r\n\r\nOccasion:\r\nWedding, Party Wear, Religions, Love, Function, Engagement, Ethnic Party\r\n\r\nPolish:\r\nRose Gold Polish\r\n\r\nBase Metal:\r\nBrass\r\n\r\nEarring Type:\r\nStud Earring', 'Free Size', 'Baby Pink', 'Rose Gold', 'Active', '2025-02-12 17:19:48', '2025-02-12 17:26:31'),
(72, 2, 14, 8, 'Rose Gold Stoned Necklace', 'nr2_eA4oTLA.webp', 1799, 10, 'Elevate your elegance with our Rose Gold Stoned Necklace. With its interplay of stones, there is grace and harmony in this piece.', 'The rose gold necklace features a circular motif design of various zircon stone sizes arranged in a harmonious manner.\r\n\r\n925 Silver with Rose Gold Plating\r\nPerfect for sensitive skin\r\nThe necklace size is 43 cm and the adjustable chain is 5 cm\r\n', 'Free Size', 'Baby Pink', 'Rose Gold', 'Active', '2025-02-12 17:28:28', '2025-02-12 17:28:28'),
(73, 2, 14, 8, 'Rose Gold Artsy Floral Necklace', 'nr3_Yxg08of.webp', 1799, 10, 'The Rose Gold Artsy Floral Necklace is inspired by the artistic curves of blooming flower petals', 'The Rose Gold Artsy Floral Necklace has a dangling like silhouette design with a rose gold finish and zircons.\r\nIncludes 16 + 2 adjustable Sterling Silver Chain with Rose Gold Plating\r\n925 Silver with Rose Gold Plating\r\nAAA+ Quality Zircons\r\nLength: 40 mm+ 5 mm Adjustable\r\nCharm: 13.3 x 13.3 mm\r\nMotif+Chain Length: 64 mm', 'Free Size', 'Baby Pink', 'Rose Gold', 'Active', '2025-02-12 17:31:08', '2025-02-12 17:31:08'),
(74, 2, 14, 8, 'Anushka Sharma Rose Gold Heart ', 'nr4_JyroMjM.webp', 2199, 10, 'Express your precious self love with this necklace. This can be your favourite choice for gifting your special friend.', 'The rose gold necklace has a heart motif nestling a heart design dangling from it.\r\n\r\n925 Silver with Rose Gold Plating\r\nPerfect for sensitive skin\r\nLength of chain: 44.5 cm + 5 cm Adjustable\r\nMotif Height: 2.1 cm, Width: 2.1 cm ', 'Free Size', 'Baby Pink', 'Rose Gold', 'Active', '2025-02-12 17:33:27', '2025-02-12 17:33:27');

-- --------------------------------------------------------

--
-- Table structure for table `staff_tb`
--

DROP TABLE IF EXISTS `staff_tb`;
CREATE TABLE IF NOT EXISTS `staff_tb` (
  `s_id` int(11) NOT NULL AUTO_INCREMENT,
  `s_name` varchar(50) NOT NULL,
  `s_address` text NOT NULL,
  `s_contact` bigint(20) NOT NULL,
  `s_image` varchar(100) NOT NULL,
  `s_password` varchar(20) NOT NULL,
  `s_status` enum('Active','Deactive') NOT NULL,
  `s_cdate` datetime NOT NULL,
  `s_udate` datetime NOT NULL,
  PRIMARY KEY (`s_id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `staff_tb`
--

INSERT INTO `staff_tb` (`s_id`, `s_name`, `s_address`, `s_contact`, `s_image`, `s_password`, `s_status`, `s_cdate`, `s_udate`) VALUES
(8, 'Patel Dhruvi', 'Plot no.212/F6 Harinam Flat sector 20 Gandhinagar', 7572890125, 'testimonial-4.jpg', '123', 'Active', '2025-01-31 14:09:04', '2025-02-12 15:31:28'),
(9, 'Raval Riddhi ', '12 Tulsinagar society Vijapur', 9537074551, 'user4-128x128_PNGXt7t.jpg', '263', 'Active', '2025-01-31 14:10:15', '2025-02-19 12:14:22');

-- --------------------------------------------------------

--
-- Table structure for table `subcategory_tb`
--

DROP TABLE IF EXISTS `subcategory_tb`;
CREATE TABLE IF NOT EXISTS `subcategory_tb` (
  `sub_id` int(11) NOT NULL AUTO_INCREMENT,
  `cat_id` int(11) NOT NULL,
  `sub_name` varchar(50) NOT NULL,
  `sub_image` varchar(100) NOT NULL,
  `sub_status` enum('Active','Deactive') NOT NULL,
  `sub_cdate` datetime NOT NULL,
  `sub_udate` datetime NOT NULL,
  PRIMARY KEY (`sub_id`)
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `subcategory_tb`
--

INSERT INTO `subcategory_tb` (`sub_id`, `cat_id`, `sub_name`, `sub_image`, `sub_status`, `sub_cdate`, `sub_udate`) VALUES
(12, 7, 'Silver', 'silver_LlM3iOV.webp', 'Active', '2025-01-18 15:09:47', '2025-01-31 12:44:40'),
(14, 5, 'Rose Gold', 'rose_gold_GQzbxJY.jpg', 'Active', '2025-01-18 15:10:39', '2025-01-31 12:48:26'),
(13, 6, 'Platinum', 'platinum_Cy3mp36.webp', 'Active', '2025-01-18 15:10:13', '2025-01-31 18:21:24'),
(11, 8, 'Gold', 'gold_u5X0S5O.webp', 'Active', '2025-01-18 15:08:52', '2025-01-31 12:48:56');

-- --------------------------------------------------------

--
-- Table structure for table `user_tb`
--

DROP TABLE IF EXISTS `user_tb`;
CREATE TABLE IF NOT EXISTS `user_tb` (
  `u_id` int(11) NOT NULL AUTO_INCREMENT,
  `u_name` varchar(50) NOT NULL,
  `u_contact` bigint(20) NOT NULL,
  `u_address` text NOT NULL,
  `u_image` varchar(100) NOT NULL,
  `u_password` varchar(20) NOT NULL,
  `u_status` enum('Active','Deactive') NOT NULL,
  `u_cdate` datetime NOT NULL,
  `u_udate` datetime NOT NULL,
  PRIMARY KEY (`u_id`)
) ENGINE=MyISAM AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_tb`
--

INSERT INTO `user_tb` (`u_id`, `u_name`, `u_contact`, `u_address`, `u_image`, `u_password`, `u_status`, `u_cdate`, `u_udate`) VALUES
(15, 'Raval Archana', 9909869820, 'Ambika society,Vijapur', 'u3.avif', '147', 'Active', '2025-01-31 12:13:48', '2025-02-20 08:39:24'),
(14, 'Raval Riddhi', 9537074551, '12 tulsinagar society near shardul society,Vijapur', 'u2.avif', '263', 'Active', '2025-01-31 12:09:12', '2025-02-20 08:31:58'),
(13, 'Patel Dhruvi', 7572890125, 'Plot no212/f6 harinam flat sector-20,Gandhinagar', 'u1.jpg', '123', 'Active', '2025-01-31 12:02:05', '2025-02-19 13:08:17'),
(16, 'Mahi', 8160574924, 'Rakhayal', 'testimonial-4_AvZsOoG.jpg', '147', 'Active', '2025-02-19 13:09:32', '2025-02-19 14:23:38');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
