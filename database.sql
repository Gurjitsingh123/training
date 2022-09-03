-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 03, 2022 at 07:51 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `training`
--

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `pk` bigint(20) NOT NULL,
  `Batch` varchar(15) COLLATE utf8mb4_unicode_ci NOT NULL,
  `IDJob` int(11) NOT NULL,
  `IDStyle` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `IDBom` int(11) NOT NULL,
  `IDMaterial` int(11) NOT NULL,
  `IDProduct` int(11) NOT NULL,
  `ifMissingBOM` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Category` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Material` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Description` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Product` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `XSreq` int(11) NOT NULL,
  `Sreq` int(11) NOT NULL,
  `Mreq` int(11) NOT NULL,
  `Lreq` int(11) NOT NULL,
  `XLreq` int(11) NOT NULL,
  `XXLreq` int(11) NOT NULL,
  `XXXLreq` int(11) NOT NULL,
  `XXXXLreq` int(11) NOT NULL,
  `Qtyreq` int(11) NOT NULL,
  `uXS` float DEFAULT NULL,
  `uS` float DEFAULT NULL,
  `uM` float DEFAULT NULL,
  `uL` float DEFAULT NULL,
  `uXL` float DEFAULT NULL,
  `uXXL` float DEFAULT NULL,
  `uXXXL` float DEFAULT NULL,
  `uXXXXL` float DEFAULT NULL,
  `uQty` float DEFAULT NULL,
  `XS` float DEFAULT NULL,
  `S` float DEFAULT NULL,
  `M` float DEFAULT NULL,
  `L` float DEFAULT NULL,
  `XL` float DEFAULT NULL,
  `XXL` float DEFAULT NULL,
  `XXXL` float DEFAULT NULL,
  `XXXXL` float DEFAULT NULL,
  `Qty` float DEFAULT NULL,
  `Usage` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`pk`, `Batch`, `IDJob`, `IDStyle`, `IDBom`, `IDMaterial`, `IDProduct`, `ifMissingBOM`, `Category`, `Material`, `Description`, `Product`, `XSreq`, `Sreq`, `Mreq`, `Lreq`, `XLreq`, `XXLreq`, `XXXLreq`, `XXXXLreq`, `Qtyreq`, `uXS`, `uS`, `uM`, `uL`, `uXL`, `uXXL`, `uXXXL`, `uXXXXL`, `uQty`, `XS`, `S`, `M`, `L`, `XL`, `XXL`, `XXXL`, `XXXXL`, `Qty`, `Usage`, `created_at`) VALUES
(233597, '63797382468', 23822, 'ZFC110', 1490, 10556, 4233, '', 'Zipper', 'YKK #3 Open End semi-auto lock', '', 'WMN\'S CYCLE AERO JERSEY', 0, 1, 1, 2, 0, 0, 0, 0, 4, 19, 19, 20, 21, 22, 23, 0, 0, 124, 0, 1, 1, 2, 0, 0, 0, 0, 4, '', '2022-08-29 22:10:23'),
(233631, '63797382468', 23822, 'ZFT350', 1574, 10556, 4675, '', 'Zipper', 'YKK #3 Open End semi-auto lock', '', 'WMN\'S TRI FULL ZIP RACESUIT (SET-IN)', 0, 1, 1, 1, 0, 0, 0, 0, 3, 15, 15, 16, 16, 17, 17, 0, 0, 96, 0, 1, 1, 1, 0, 0, 0, 0, 3, '', '2022-08-29 22:10:23'),
(233649, '63797382468', 23822, 'ZMC110', 1509, 10556, 4228, '', 'Zipper', 'YKK #3 Open End semi-auto lock', '', 'MEN\'S CYCLE AERO JERSEY', 0, 0, 2, 4, 1, 2, 0, 0, 9, 20, 20, 21, 22, 23, 24, 0, 0, 130, 0, 0, 2, 4, 1, 2, 0, 0, 9, '', '2022-08-29 22:10:23'),
(233684, '63797382468', 23822, 'ZMT350', 1587, 10556, 4676, '', 'Zipper', 'YKK #3 Open End semi-auto lock', '', 'MEN\'S TRI FULL ZIP RACESUIT  (SET-IN)', 0, 1, 4, 1, 0, 3, 0, 0, 9, 16, 16, 17, 17, 18, 18, 0, 0, 102, 0, 1, 4, 1, 0, 3, 0, 0, 9, '', '2022-08-29 22:10:23');

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `id` int(10) NOT NULL,
  `name` varchar(20) NOT NULL,
  `class` varchar(10) NOT NULL,
  `age` int(10) NOT NULL,
  `height` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`id`, `name`, `class`, `age`, `height`) VALUES
(2, 'simar', '10', 14, '5.9'),
(3, 'jass', 'ba', 19, '5.5'),
(4, 'gurvir', 'bca', 23, '5.8');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`pk`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`),
  ADD UNIQUE KEY `name_2` (`name`),
  ADD UNIQUE KEY `name_3` (`name`),
  ADD UNIQUE KEY `name_4` (`name`),
  ADD UNIQUE KEY `id_2` (`id`),
  ADD KEY `name_5` (`name`),
  ADD KEY `id` (`id`),
  ADD KEY `name_6` (`name`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `pk` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=233697;

--
-- AUTO_INCREMENT for table `student`
--
ALTER TABLE `student`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
