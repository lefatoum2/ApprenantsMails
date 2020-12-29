-- phpMyAdmin SQL Dump
-- version 4.9.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Nov 20, 2020 at 01:08 PM
-- Server version: 5.7.24
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
-- Database: `binomotron2`
--

-- --------------------------------------------------------

--
-- Table structure for table `apprenant`
--

CREATE TABLE `apprenant` (
  `ID_APPRENANT` int(11) NOT NULL,
  `NOM` varchar(50) NOT NULL,
  `PRENOM` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `apprenant`
--

INSERT INTO `apprenant` (`ID_APPRENANT`, `NOM`, `PRENOM`) VALUES
(1, 'Mbarga Mvogo', 'Christian'),
(2, 'Sabia', 'Paul'),
(3, 'Hergoualch', 'Pereg'),
(4, 'Maintier', 'Ludivine'),
(5, 'Moulard', 'Eva'),
(6, 'Pertron', 'Aude'),
(7, 'Furiga', 'Julien'),
(8, 'Chaigneau', 'Thomas'),
(9, 'Rioual', 'Ronan'),
(10, 'Bokalli', 'Luigi'),
(11, 'Le Goff', 'Baptiste'),
(12, 'Le Berre', 'Baptiste'),
(13, 'Guillen', 'Celine'),
(14, 'Karfaoui', 'Christelle'),
(15, 'Le Moal', 'Patricia'),
(16, 'Cloatre', 'Erwan'),
(17, 'Bonneau', 'Amaury'),
(18, 'Verpoest', 'Guillaume'),
(19, 'Ibanni', 'Jamal'),
(20, 'Le Joncour', 'Jérémy');

-- --------------------------------------------------------

--
-- Table structure for table `apprenant_groupe`
--

CREATE TABLE `apprenant_groupe` (
  `ID_GROUPE` int(11) NOT NULL,
  `ID_PROJET` int(11) NOT NULL,
  `ID_APPRENANT` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `groupe`
--

CREATE TABLE `groupe` (
  `ID_GROUPE` int(11) NOT NULL,
  `LIBELLE` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `groupe`
--

INSERT INTO `groupe` (`ID_GROUPE`, `LIBELLE`) VALUES
(1, 'GROUPE 1'),
(2, 'GROUPE 2'),
(3, 'GROUPE 3'),
(4, 'GROUPE 4'),
(5, 'GROUPE 5'),
(6, 'GROUPE 6'),
(7, 'GROUPE 7'),
(8, 'GROUPE 8'),
(9, 'GROUPE 9'),
(10, 'GROUPE 10'),
(11, 'GROUPE 11'),
(12, 'GROUPE 12'),
(13, 'GROUPE 13'),
(14, 'GROUPE 14'),
(15, 'GROUPE 15'),
(16, 'GROUPE 16'),
(17, 'GROUPE 17'),
(18, 'GROUPE 18'),
(19, 'GROUPE 19'),
(20, 'GROUPE 20');

-- --------------------------------------------------------

--
-- Table structure for table `projet`
--

CREATE TABLE `projet` (
  `ID_PROJET` int(50) NOT NULL,
  `LIBELLE` varchar(50) NOT NULL,
  `DATE_DEBUT` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `apprenant`
--
ALTER TABLE `apprenant`
  ADD PRIMARY KEY (`ID_APPRENANT`);

--
-- Indexes for table `apprenant_groupe`
--
ALTER TABLE `apprenant_groupe`
  ADD KEY `ID_APPRENANT` (`ID_APPRENANT`),
  ADD KEY `ID_GROUPE` (`ID_GROUPE`),
  ADD KEY `ID_PROJET` (`ID_PROJET`);

--
-- Indexes for table `groupe`
--
ALTER TABLE `groupe`
  ADD PRIMARY KEY (`ID_GROUPE`);

--
-- Indexes for table `projet`
--
ALTER TABLE `projet`
  ADD PRIMARY KEY (`ID_PROJET`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `apprenant`
--
ALTER TABLE `apprenant`
  MODIFY `ID_APPRENANT` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `groupe`
--
ALTER TABLE `groupe`
  MODIFY `ID_GROUPE` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `projet`
--
ALTER TABLE `projet`
  MODIFY `ID_PROJET` int(50) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `apprenant_groupe`
--
ALTER TABLE `apprenant_groupe`
  ADD CONSTRAINT `apprenant_groupe_ibfk_1` FOREIGN KEY (`ID_APPRENANT`) REFERENCES `apprenant` (`ID_APPRENANT`),
  ADD CONSTRAINT `apprenant_groupe_ibfk_2` FOREIGN KEY (`ID_GROUPE`) REFERENCES `groupe` (`ID_GROUPE`),
  ADD CONSTRAINT `apprenant_groupe_ibfk_3` FOREIGN KEY (`ID_PROJET`) REFERENCES `projet` (`ID_PROJET`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;