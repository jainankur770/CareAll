-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 07, 2020 at 05:44 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `careall`
--

-- --------------------------------------------------------

--
-- Table structure for table `elder_details`
--

CREATE TABLE `elder_details` (
  `Id` int(11) NOT NULL,
  `Name` varchar(20) NOT NULL,
  `Age` int(3) NOT NULL,
  `Fund_raised` int(8) NOT NULL,
  `Contact` bigint(10) NOT NULL,
  `Taken_care_by` int(5) NOT NULL DEFAULT 0,
  `Request_id` int(3) NOT NULL,
  `Review` text DEFAULT NULL,
  `Rating` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `elder_details`
--

INSERT INTO `elder_details` (`Id`, `Name`, `Age`, `Fund_raised`, `Contact`, `Taken_care_by`, `Request_id`, `Review`, `Rating`) VALUES
(1, 'Ankur', 55, 10000, 8824547824, 0, 0, NULL, NULL),
(2, 'Adarsh', 55, 15000, 7845124579, 0, 0, NULL, NULL),
(5, 'aman', 60, 7500, 6123548746, 1, 0, NULL, NULL),
(6, 'akash', 51, 12000, 7846951591, 0, 0, NULL, NULL),
(7, 'aditya', 64, 8500, 7513649875, 0, 0, NULL, NULL),
(8, 'amit', 74, 20000, 8624513975, 0, 0, NULL, NULL),
(9, 'shreeyash', 53, 14000, 6324512876, 0, 0, NULL, NULL),
(10, 'mayank', 72, 20000, 9658741354, 2, 0, NULL, NULL),
(11, 'mohit', 64, 15000, 1245789654, 0, 0, NULL, NULL),
(12, 'akansha', 68, 15000, 8745123654, 0, 0, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `taking_care`
--

CREATE TABLE `taking_care` (
  `youth_id` int(11) NOT NULL,
  `old_id_1` int(11) DEFAULT NULL,
  `old_id_2` int(11) DEFAULT NULL,
  `old_id_3` int(11) NOT NULL,
  `old_id_4` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `taking_care`
--

INSERT INTO `taking_care` (`youth_id`, `old_id_1`, `old_id_2`, `old_id_3`, `old_id_4`) VALUES
(2, 10, 0, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `youth_details`
--

CREATE TABLE `youth_details` (
  `Id` int(11) NOT NULL,
  `Name` varchar(20) NOT NULL,
  `Age` int(3) NOT NULL,
  `Address` varchar(100) NOT NULL,
  `Contact` bigint(10) NOT NULL,
  `Number_undertaken_elders` int(1) NOT NULL DEFAULT 0,
  `Review` text DEFAULT NULL,
  `Rating` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `youth_details`
--

INSERT INTO `youth_details` (`Id`, `Name`, `Age`, `Address`, `Contact`, `Number_undertaken_elders`, `Review`, `Rating`) VALUES
(1, 'Ankur', 27, 'mahesh colony gulabpura', 4512365478, 0, NULL, NULL),
(2, 'Ashok', 30, 'udaipur', 5741236519, 1, NULL, NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `elder_details`
--
ALTER TABLE `elder_details`
  ADD PRIMARY KEY (`Id`);

--
-- Indexes for table `taking_care`
--
ALTER TABLE `taking_care`
  ADD PRIMARY KEY (`youth_id`,`old_id_3`),
  ADD UNIQUE KEY `old_id_4` (`old_id_4`);

--
-- Indexes for table `youth_details`
--
ALTER TABLE `youth_details`
  ADD PRIMARY KEY (`Id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `elder_details`
--
ALTER TABLE `elder_details`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `youth_details`
--
ALTER TABLE `youth_details`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
