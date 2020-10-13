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
-- Table structure for table `contact`
--

CREATE TABLE `contact` (
  `id` int(255) not null primary key auto_increment,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `subject` varchar(255) NOT NULL,
  `message` varchar(255) NOT NULL,
  `date` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contact`
--

INSERT INTO `contact` (`id`, `name`, `email`, `subject`, `message`, `date`) VALUES
(12, 'Mohd Kamleen', 'kamleenmohd@gmail.com', 'want to say hi!!', 'hiiiiiiiiii', ''),
(15, 'Mohd Kamleen', 'kamleenmohd@gmail.com', 'looking a partnership', 'hiiiiiiiiiiiiii', ''),
(16, 'Mohd Kamleen', 'kamleenmohd@gmail.com', 'want to hire me ', 'bhai mera project bnane h\r\n', ''),
(17, 'Mohd Kamleen', 'kamleenmohd@gmail.com', 'want to say hi!!', 'gfhgfdhgfh', ''),
(18, 'Mohd Kamleen', 'kamleenmohd@gmail.com', 'hiiiiii', 'yhthty', ''),
(19, 'daniyal ', 'daniyal@gmail.com', 'bas waise hi', 'hii bro\r\n', ''),
(21, 'Mohd Kamleen', 'kamleenmohd@gmail.com', 'Need help with a one-off project', 'fdsfdsfds', '03Oct,2020 AT Saturday 8:39AM'),
(22, 'Mohd Kamleenf', 'kamleenmohd@gmail.com', 'dfdg', 'dfgdfgdg', '03Oct,2020 AT Saturday 8:41AM'),
(23, 'Mohd Kamleenf', 'kamleenmohd@gmail.com', 'dfdg', 'dfgdfgdg', '03Oct,2020 AT Saturday 8:41AM');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contact`
--
ALTER TABLE `contact`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contact`
--
ALTER TABLE `contact`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
