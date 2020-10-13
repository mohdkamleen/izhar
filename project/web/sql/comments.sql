-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 03, 2020 at 09:29 AM
-- Server version: 10.4.13-MariaDB
-- PHP Version: 7.4.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `kamleen`
--

-- --------------------------------------------------------

--
-- Table structure for table `comments`
--

CREATE TABLE `comments` (
  `date` varchar(255) DEFAULT NULL,
  `id` int(255) not null primary key auto_increment,
  `comment` varchar(200) DEFAULT NULL,
  `user` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `comments`
--

INSERT INTO `comments` (`date`, `id`, `comment`, `user`) VALUES
('02-09-2020  time 7:20:34', 43, 'nice', 'abid'),
('02-09-2020  time 7:40:59', 44, 'cool', 'ankur'),
('02-09-2020 time 7:41:10', 45, 'kya baat h bhai', 'gopal'),
('02-09-2020  time 7:42:04', 46, 'nice bro', 'rehan'),
('02-09-2020  time 7:44:15', 47, 'khoob', 'sayyed bhai'),
('02-09-2020  time 7:44:30', 48, 'wow bro kese bnaye', 'ratnesh'),
('02-09-2020&nbsp; time 8:10:30', 49, 'hiiiiiiiiiiiiiiiiiiiii', ''),
('02-09-2020  time 8:10:44', 50, 'nice blog', 'adil'),
('02-09-2020&nbsp; time 8:11:01', 51, 'awesome', ''),
('02-09-2020&nbsp; time 8:11:10', 52, 'nice kamleen ', ''),
('02-09-2020  time 6:56:09', 53, 'wow', 'Mohd kamleen'),
('02Oct,2020 AT Friday7:23:24PM', 54, 'nice', 'kamleenmohd@gmail.com '),
('02Oct,2020 AT Friday 7:24:44PM', 55, 'ewwwwwwwwwwwww', ''),
('02Oct,2020 AT Friday 7:26:PM', 56, 'nice bro', ''),
('02Oct,2020 AT Friday 7:26PM', 57, 'wah kamleen bhai gjab', ''),
('02Oct,2020 AT Friday 7:29PM', 58, 'wah kamleeen nice project koi h nhee pure csjm me aisa project bnane wala', ''),
('02Oct,2020 AT Friday 7:31PM', 59, 'wow', ''),
('02Oct,2020 AT Friday 7:46PM', 60, 'dsfdsfdsf', 'UNKNOWN'),
('02Oct,2020 AT Friday 7:48PM', 61, 'dfdsgfdgdfg', 'UNKNOWN'),
('02Oct,2020 AT Friday 8:20PM', 62, 'gfdgdfgdfgdfgdf', 'UNKNOWN'),
('02Oct,2020 AT Friday 8:51PM', 63, 'dsfsfdsfds', 'tab'),
('02Oct,2020 AT Friday 8:53PM', 64, 'dsfdsfdsfds', 'UNKNOWN'),
('02Oct,2020 AT Friday 8:54PM', 65, 'hgfdhfhgfhgfhf', 'UNKNOWN'),
('02Oct,2020 AT Friday 8:58PM', 66, 'dfgfdgfd', 'UNKNOWN'),
('03Oct,2020 AT Saturday 7:10AM', 67, 'wow', 'UNKNOWN'),
('03Oct,2020 AT Saturday 9:28AM', 68, 'very very vey nice kamleen bhai isse best koi nheeee', 'adil');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `comments`
--
ALTER TABLE `comments`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `comments`
--
ALTER TABLE `comments`
  MODIFY `id` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=69;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
