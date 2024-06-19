-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 19/06/2024 às 21:25
-- Versão do servidor: 10.4.32-MariaDB
-- Versão do PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `pizzasnachtech`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `clientes`
--

CREATE TABLE `clientes` (
  `cliente_id` int(11) NOT NULL,
  `nome` varchar(255) NOT NULL,
  `endereco` varchar(255) NOT NULL,
  `telefone` varchar(20) NOT NULL,
  `email` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `clientes`
--

INSERT INTO `clientes` (`cliente_id`, `nome`, `endereco`, `telefone`, `email`) VALUES
(1, 'João Silva', '', '123456789', 'joao@brocolis.com'),
(3, 'Maria Oliveira', '', '987654321', 'maria@brocolis.com'),
(4, 'Pedro Almeida', '', '456789123', 'pedro@brocolis.com'),
(5, 'João Silva', '', '123456789', 'joao@brocolis.com'),
(6, 'Maria Oliveira', '', '987654321', 'maria@brocolis.com'),
(7, 'Pedro Almeida', '', '456789123', 'pedro@brocolis.com'),
(8, 'João Silva', '', '123456789', 'joao@brocolis.com'),
(9, 'Maria Oliveira', '', '987654321', 'maria@brocolis.com'),
(10, 'Pedro Almeida', '', '456789123', 'pedro@brocolis.com'),
(11, 'João Silva', '', '123456789', 'joao@brocolis.com'),
(12, 'Maria Oliveira', '', '987654321', 'maria@brocolis.com'),
(13, 'Pedro Almeida', '', '456789123', 'pedro@brocolis.com'),
(14, 'João Silva', '', '123456789', 'joao@brocolis.com'),
(15, 'Maria Oliveira', '', '987654321', 'maria@brocolis.com'),
(16, 'Pedro Almeida', '', '456789123', 'pedro@brocolis.com'),
(17, 'João Silva', '', '123456789', 'joao@brocolis.com'),
(18, 'Maria Oliveira', '', '987654321', 'maria@brocolis.com'),
(19, 'Pedro Almeida', '', '456789123', 'pedro@brocolis.com'),
(20, 'João Silva', '', '123456789', 'joao@brocolis.com'),
(21, 'Maria Oliveira', '', '987654321', 'maria@brocolis.com'),
(22, 'Pedro Almeida', '', '456789123', 'pedro@brocolis.com'),
(23, 'Ana Costa', '', '123456789', 'ana@brocolis.com'),
(24, 'João Silva Jr.', '', '123456789', 'joaojr@brocolis.com'),
(25, 'Maria Silva', '', '123456789', 'maria@brocolis.com'),
(26, 'Pedro Silva', '', '123456789', 'pedro@brocolis.com'),
(27, 'Ana Silva', '', '123456789', 'ana@brocolis.com'),
(28, 'João Silva III', '', '123456789', 'joaoiii@brocolis.com'),
(29, 'Maria Silva Jr.', '', '123456789', 'mariajr@brocolis.com'),
(30, 'Pedro Silva Jr.', '', '123456789', 'pedrojr@brocolis.com'),
(31, 'Ana Silva Jr.', '', '123456789', 'anajr@brocolis.com'),
(32, 'João Silva IV', '', '123456789', 'joaoiv@brocolis.com'),
(33, 'Maria Silva III', '', '123456789', 'mariaiii@brocolis.com'),
(34, 'Pedro Silva III', '', '123456789', 'pedroiii@brocolis.com'),
(35, 'João Silva', '', '123456789', 'joao@brocolis.com'),
(36, 'Maria Oliveira', '', '987654321', 'maria@brocolis.com'),
(37, 'Pedro Almeida', '', '456789123', 'pedro@brocolis.com'),
(50, 'João Silva', '', '123456789', 'joao@brocolis.com'),
(51, 'Maria Oliveira', '', '987654321', 'maria@brocolis.com'),
(52, 'Pedro Almeida', '', '456789123', 'pedro@brocolis.com'),
(53, 'Ana Costa', '', '123456789', 'ana@brocolis.com'),
(54, 'João Silva Jr.', '', '123456789', 'joaojr@brocolis.com'),
(55, 'Maria Silva', '', '123456789', 'maria@brocolis.com'),
(56, 'Pedro Silva', '', '123456789', 'pedro@brocolis.com'),
(57, 'Ana Silva', '', '123456789', 'ana@brocolis.com'),
(58, 'João Silva III', '', '123456789', 'joaoiii@brocolis.com'),
(59, 'Maria Silva Jr.', '', '123456789', 'mariajr@brocolis.com'),
(60, 'Pedro Silva Jr.', '', '123456789', 'pedrojr@brocolis.com'),
(61, 'Ana Silva Jr.', '', '123456789', 'anajr@brocolis.com'),
(62, 'João Silva IV', '', '123456789', 'joaoiv@brocolis.com'),
(63, 'Maria Silva III', '', '123456789', 'mariaiii@brocolis.com'),
(64, 'Pedro Silva III', '', '123456789', 'pedroiii@brocolis.com'),
(65, 'Ana Costa', '', '123456789', 'ana@brocolis.com'),
(66, 'João Silva Jr.', '', '123456789', 'joaojr@brocolis.com'),
(67, 'Maria Silva', '', '123456789', 'maria@brocolis.com'),
(68, 'Pedro Silva', '', '123456789', 'pedro@brocolis.com'),
(69, 'Ana Silva', '', '123456789', 'ana@brocolis.com'),
(70, 'Tiago III', '', '123456789', 'tiagoiii@brocolis.com'),
(71, 'Maria Silva Jr.', '', '123456789', 'mariajr@brocolis.com'),
(72, 'Pedro Silva Jr.', '', '123456789', 'pedrojr@brocolis.com'),
(73, 'Ana Silva Jr.', '', '123456789', 'anajr@brocolis.com'),
(74, 'Bartolomeu IV', '', '123456789', 'bartolomeuiv@brocolis.com'),
(75, 'Maria Silva III', '', '123456789', 'mariaiii@brocolis.com'),
(76, 'Filipe III', '', '123456789', 'filipeiii@brocolis.com'),
(77, 'João Silva', '', '123456789', 'joao@brocolis.com'),
(78, 'Maria Oliveira', '', '987654321', 'maria@brocolis.com'),
(79, 'Pedro Almeida', '', '456789123', 'pedro@brocolis.com'),
(80, 'Ana Costa', '', '123456789', 'ana@brocolis.com'),
(81, 'João Silva Jr.', '', '123456789', 'joaojr@brocolis.com'),
(82, 'Maria Silva', '', '123456789', 'maria@brocolis.com'),
(83, 'Pedro Silva', '', '123456789', 'pedro@brocolis.com'),
(84, 'Ana Silva', '', '123456789', 'ana@brocolis.com'),
(85, 'João Silva III', '', '123456789', 'joaoiii@brocolis.com'),
(86, 'Maria Silva Jr.', '', '123456789', 'mariajr@brocolis.com'),
(87, 'Pedro Silva Jr.', '', '123456789', 'pedrojr@brocolis.com'),
(88, 'Ana Silva Jr.', '', '123456789', 'anajr@brocolis.com'),
(89, 'João Silva IV', '', '123456789', 'joaoiv@brocolis.com'),
(90, 'Maria Silva III', '', '123456789', 'mariaiii@brocolis.com'),
(91, 'Pedro Silva III', '', '123456789', 'pedroiii@brocolis.com'),
(92, 'Ana Costa', '', '123456789', 'ana@brocolis.com'),
(93, 'João Silva Jr.', '', '123456789', 'joaojr@brocolis.com'),
(94, 'Maria Silva', '', '123456789', 'maria@brocolis.com'),
(95, 'Pedro Silva', '', '123456789', 'pedro@brocolis.com'),
(96, 'Ana Silva', '', '123456789', 'ana@brocolis.com'),
(97, 'Tiago III', '', '123456789', 'tiagoiii@brocolis.com'),
(98, 'Maria Silva Jr.', '', '123456789', 'mariajr@brocolis.com'),
(99, 'Pedro Silva Jr.', '', '123456789', 'pedrojr@brocolis.com'),
(100, 'Ana Silva Jr.', '', '123456789', 'anajr@brocolis.com'),
(101, 'Bartolomeu IV', '', '123456789', 'bartolomeuiv@brocolis.com'),
(102, 'Maria Silva III', '', '123456789', 'mariaiii@brocolis.com'),
(103, 'Filipe III', '', '123456789', 'filipeiii@brocolis.com'),
(104, 'João Silva', '', '123456789', 'joao@brocolis.com'),
(105, 'Maria Oliveira', '', '987654321', 'maria@brocolis.com'),
(106, 'Pedro Almeida', '', '456789123', 'pedro@brocolis.com'),
(107, 'Ana Costa', '', '123456789', 'ana@brocolis.com'),
(108, 'João Silva Jr.', '', '123456789', 'joaojr@brocolis.com'),
(109, 'Maria Silva', '', '123456789', 'maria@brocolis.com'),
(110, 'Pedro Silva', '', '123456789', 'pedro@brocolis.com'),
(111, 'Ana Silva', '', '123456789', 'ana@brocolis.com'),
(112, 'João Silva III', '', '123456789', 'joaoiii@brocolis.com'),
(113, 'Maria Silva Jr.', '', '123456789', 'mariajr@brocolis.com'),
(114, 'Pedro Silva Jr.', '', '123456789', 'pedrojr@brocolis.com'),
(115, 'Ana Silva Jr.', '', '123456789', 'anajr@brocolis.com'),
(116, 'João Silva IV', '', '123456789', 'joaoiv@brocolis.com'),
(117, 'Maria Silva III', '', '123456789', 'mariaiii@brocolis.com'),
(118, 'Pedro Silva III', '', '123456789', 'pedroiii@brocolis.com'),
(119, 'Ana Costa', '', '123456789', 'ana@brocolis.com'),
(120, 'João Silva Jr.', '', '123456789', 'joaojr@brocolis.com'),
(121, 'Maria Silva', '', '123456789', 'maria@brocolis.com'),
(122, 'Pedro Silva', '', '123456789', 'pedro@brocolis.com'),
(123, 'Ana Silva', '', '123456789', 'ana@brocolis.com'),
(124, 'Tiago III', '', '123456789', 'tiagoiii@brocolis.com'),
(125, 'Maria Silva Jr.', '', '123456789', 'mariajr@brocolis.com'),
(126, 'Pedro Silva Jr.', '', '123456789', 'pedrojr@brocolis.com'),
(127, 'Ana Silva Jr.', '', '123456789', 'anajr@brocolis.com'),
(128, 'Bartolomeu IV', '', '123456789', 'bartolomeuiv@brocolis.com'),
(129, 'Maria Silva III', '', '123456789', 'mariaiii@brocolis.com'),
(130, 'Filipe III', '', '123456789', 'filipeiii@brocolis.com'),
(131, 'João Silva', '', '123456789', 'joao@brocolis.com'),
(132, 'Maria Oliveira', '', '987654321', 'maria@brocolis.com'),
(133, 'Pedro Almeida', '', '456789123', 'pedro@brocolis.com'),
(134, 'Ana Costa', '', '123456789', 'ana@brocolis.com'),
(135, 'João Silva Jr.', '', '123456789', 'joaojr@brocolis.com'),
(136, 'Maria Silva', '', '123456789', 'maria@brocolis.com'),
(137, 'Pedro Silva', '', '123456789', 'pedro@brocolis.com'),
(138, 'Ana Silva', '', '123456789', 'ana@brocolis.com'),
(139, 'João Silva III', '', '123456789', 'joaoiii@brocolis.com'),
(140, 'Maria Silva Jr.', '', '123456789', 'mariajr@brocolis.com'),
(141, 'Pedro Silva Jr.', '', '123456789', 'pedrojr@brocolis.com'),
(142, 'Ana Silva Jr.', '', '123456789', 'anajr@brocolis.com'),
(143, 'João Silva IV', '', '123456789', 'joaoiv@brocolis.com'),
(144, 'Maria Silva III', '', '123456789', 'mariaiii@brocolis.com'),
(145, 'Pedro Silva III', '', '123456789', 'pedroiii@brocolis.com'),
(146, 'Ana Costa', '', '123456789', 'ana@brocolis.com'),
(147, 'João Silva Jr.', '', '123456789', 'joaojr@brocolis.com'),
(148, 'Maria Silva', '', '123456789', 'maria@brocolis.com'),
(149, 'Pedro Silva', '', '123456789', 'pedro@brocolis.com'),
(150, 'Ana Silva', '', '123456789', 'ana@brocolis.com'),
(151, 'Tiago III', '', '123456789', 'tiagoiii@brocolis.com'),
(152, 'Maria Silva Jr.', '', '123456789', 'mariajr@brocolis.com'),
(153, 'Pedro Silva Jr.', '', '123456789', 'pedrojr@brocolis.com'),
(154, 'Ana Silva Jr.', '', '123456789', 'anajr@brocolis.com'),
(155, 'Bartolomeu IV', '', '123456789', 'bartolomeuiv@brocolis.com'),
(156, 'Maria Silva III', '', '123456789', 'mariaiii@brocolis.com'),
(157, 'Filipe III', '', '123456789', 'filipeiii@brocolis.com'),
(158, 'João Silva', '', '123456789', 'joao@brocolis.com'),
(159, 'Maria Oliveira', '', '987654321', 'maria@brocolis.com'),
(160, 'Pedro Almeida', '', '456789123', 'pedro@brocolis.com'),
(161, 'Ana Costa', '', '123456789', 'ana@brocolis.com'),
(162, 'João Silva Jr.', '', '123456789', 'joaojr@brocolis.com'),
(163, 'Maria Silva', '', '123456789', 'maria@brocolis.com'),
(164, 'Pedro Silva', '', '123456789', 'pedro@brocolis.com'),
(165, 'Ana Silva', '', '123456789', 'ana@brocolis.com'),
(166, 'João Silva III', '', '123456789', 'joaoiii@brocolis.com'),
(167, 'Maria Silva Jr.', '', '123456789', 'mariajr@brocolis.com'),
(168, 'Pedro Silva Jr.', '', '123456789', 'pedrojr@brocolis.com'),
(169, 'Ana Silva Jr.', '', '123456789', 'anajr@brocolis.com'),
(170, 'João Silva IV', '', '123456789', 'joaoiv@brocolis.com'),
(171, 'Maria Silva III', '', '123456789', 'mariaiii@brocolis.com'),
(172, 'Pedro Silva III', '', '123456789', 'pedroiii@brocolis.com'),
(173, 'Ana Costa', '', '123456789', 'ana@brocolis.com'),
(174, 'João Silva Jr.', '', '123456789', 'joaojr@brocolis.com'),
(175, 'Maria Silva', '', '123456789', 'maria@brocolis.com'),
(176, 'Pedro Silva', '', '123456789', 'pedro@brocolis.com'),
(177, 'Ana Silva', '', '123456789', 'ana@brocolis.com'),
(178, 'Tiago III', '', '123456789', 'tiagoiii@brocolis.com'),
(179, 'Maria Silva Jr.', '', '123456789', 'mariajr@brocolis.com'),
(180, 'Pedro Silva Jr.', '', '123456789', 'pedrojr@brocolis.com'),
(181, 'Ana Silva Jr.', '', '123456789', 'anajr@brocolis.com'),
(182, 'Bartolomeu IV', '', '123456789', 'bartolomeuiv@brocolis.com'),
(183, 'Maria Silva III', '', '123456789', 'mariaiii@brocolis.com'),
(184, 'Filipe III', '', '123456789', 'filipeiii@brocolis.com'),
(185, 'João Silva', '', '123456789', 'joao@brocolis.com'),
(186, 'Maria Oliveira', '', '987654321', 'maria@brocolis.com'),
(187, 'Pedro Almeida', '', '456789123', 'pedro@brocolis.com'),
(188, 'Ana Costa', '', '123456789', 'ana@brocolis.com'),
(189, 'João Silva Jr.', '', '123456789', 'joaojr@brocolis.com'),
(190, 'Maria Silva', '', '123456789', 'maria@brocolis.com'),
(191, 'Pedro Silva', '', '123456789', 'pedro@brocolis.com'),
(192, 'Ana Silva', '', '123456789', 'ana@brocolis.com'),
(193, 'João Silva III', '', '123456789', 'joaoiii@brocolis.com'),
(194, 'Maria Silva Jr.', '', '123456789', 'mariajr@brocolis.com'),
(195, 'Pedro Silva Jr.', '', '123456789', 'pedrojr@brocolis.com'),
(196, 'Ana Silva Jr.', '', '123456789', 'anajr@brocolis.com'),
(197, 'João Silva IV', '', '123456789', 'joaoiv@brocolis.com'),
(198, 'Maria Silva III', '', '123456789', 'mariaiii@brocolis.com'),
(199, 'Pedro Silva III', '', '123456789', 'pedroiii@brocolis.com'),
(200, 'Ana Costa', '', '123456789', 'ana@brocolis.com'),
(201, 'João Silva Jr.', '', '123456789', 'joaojr@brocolis.com'),
(202, 'Maria Silva', '', '123456789', 'maria@brocolis.com'),
(203, 'Pedro Silva', '', '123456789', 'pedro@brocolis.com'),
(204, 'Ana Silva', '', '123456789', 'ana@brocolis.com'),
(205, 'Tiago III', '', '123456789', 'tiagoiii@brocolis.com'),
(206, 'Maria Silva Jr.', '', '123456789', 'mariajr@brocolis.com'),
(207, 'Pedro Silva Jr.', '', '123456789', 'pedrojr@brocolis.com'),
(208, 'Ana Silva Jr.', '', '123456789', 'anajr@brocolis.com'),
(209, 'Bartolomeu IV', '', '123456789', 'bartolomeuiv@brocolis.com'),
(210, 'Maria Silva III', '', '123456789', 'mariaiii@brocolis.com'),
(211, 'Filipe III', '', '123456789', 'filipeiii@brocolis.com'),
(212, 'João Silva', '', '123456789', 'joao@brocolis.com'),
(213, 'Maria Oliveira', '', '987654321', 'maria@brocolis.com'),
(214, 'Pedro Almeida', '', '456789123', 'pedro@brocolis.com'),
(215, 'Ana Costa', '', '123456789', 'ana@brocolis.com'),
(216, 'João Silva Jr.', '', '123456789', 'joaojr@brocolis.com'),
(217, 'Maria Silva', '', '123456789', 'maria@brocolis.com'),
(218, 'Pedro Silva', '', '123456789', 'pedro@brocolis.com'),
(219, 'Ana Silva', '', '123456789', 'ana@brocolis.com'),
(220, 'João Silva III', '', '123456789', 'joaoiii@brocolis.com'),
(221, 'Maria Silva Jr.', '', '123456789', 'mariajr@brocolis.com'),
(222, 'Pedro Silva Jr.', '', '123456789', 'pedrojr@brocolis.com'),
(223, 'Ana Silva Jr.', '', '123456789', 'anajr@brocolis.com'),
(224, 'João Silva IV', '', '123456789', 'joaoiv@brocolis.com'),
(225, 'Maria Silva III', '', '123456789', 'mariaiii@brocolis.com'),
(226, 'Pedro Silva III', '', '123456789', 'pedroiii@brocolis.com'),
(227, 'Ana Costa', '', '123456789', 'ana@brocolis.com'),
(228, 'João Silva Jr.', '', '123456789', 'joaojr@brocolis.com'),
(229, 'Maria Silva', '', '123456789', 'maria@brocolis.com'),
(230, 'Pedro Silva', '', '123456789', 'pedro@brocolis.com'),
(231, 'Ana Silva', '', '123456789', 'ana@brocolis.com'),
(232, 'Tiago III', '', '123456789', 'tiagoiii@brocolis.com'),
(233, 'Maria Silva Jr.', '', '123456789', 'mariajr@brocolis.com'),
(234, 'Pedro Silva Jr.', '', '123456789', 'pedrojr@brocolis.com'),
(235, 'Ana Silva Jr.', '', '123456789', 'anajr@brocolis.com'),
(236, 'Bartolomeu IV', '', '123456789', 'bartolomeuiv@brocolis.com'),
(237, 'Maria Silva III', '', '123456789', 'mariaiii@brocolis.com'),
(238, 'Filipe III', '', '123456789', 'filipeiii@brocolis.com'),
(239, 'João Silva', '', '123456789', 'joao@brocolis.com'),
(240, 'Maria Oliveira', '', '987654321', 'maria@brocolis.com'),
(241, 'Pedro Almeida', '', '456789123', 'pedro@brocolis.com'),
(242, 'Ana Costa', '', '123456789', 'ana@brocolis.com'),
(243, 'João Silva Jr.', '', '123456789', 'joaojr@brocolis.com'),
(244, 'Maria Silva', '', '123456789', 'maria@brocolis.com'),
(245, 'Pedro Silva', '', '123456789', 'pedro@brocolis.com'),
(246, 'Ana Silva', '', '123456789', 'ana@brocolis.com'),
(247, 'João Silva III', '', '123456789', 'joaoiii@brocolis.com'),
(248, 'Maria Silva Jr.', '', '123456789', 'mariajr@brocolis.com'),
(249, 'Pedro Silva Jr.', '', '123456789', 'pedrojr@brocolis.com'),
(250, 'Ana Silva Jr.', '', '123456789', 'anajr@brocolis.com'),
(251, 'João Silva IV', '', '123456789', 'joaoiv@brocolis.com'),
(252, 'Maria Silva III', '', '123456789', 'mariaiii@brocolis.com'),
(253, 'Pedro Silva III', '', '123456789', 'pedroiii@brocolis.com'),
(254, 'Ana Costa', '', '123456789', 'ana@brocolis.com'),
(255, 'João Silva Jr.', '', '123456789', 'joaojr@brocolis.com'),
(256, 'Maria Silva', '', '123456789', 'maria@brocolis.com'),
(257, 'Pedro Silva', '', '123456789', 'pedro@brocolis.com'),
(258, 'Ana Silva', '', '123456789', 'ana@brocolis.com'),
(259, 'Tiago III', '', '123456789', 'tiagoiii@brocolis.com'),
(260, 'Maria Silva Jr.', '', '123456789', 'mariajr@brocolis.com'),
(261, 'Pedro Silva Jr.', '', '123456789', 'pedrojr@brocolis.com'),
(262, 'Ana Silva Jr.', '', '123456789', 'anajr@brocolis.com'),
(263, 'Bartolomeu IV', '', '123456789', 'bartolomeuiv@brocolis.com'),
(264, 'Maria Silva III', '', '123456789', 'mariaiii@brocolis.com'),
(265, 'Filipe III', '', '123456789', 'filipeiii@brocolis.com'),
(266, 'João Silva', '', '123456789', 'joao@brocolis.com'),
(267, 'Maria Oliveira', '', '987654321', 'maria@brocolis.com'),
(268, 'Pedro Almeida', '', '456789123', 'pedro@brocolis.com'),
(269, 'Ana Costa', '', '123456789', 'ana@brocolis.com'),
(270, 'João Silva Jr.', '', '123456789', 'joaojr@brocolis.com'),
(271, 'Maria Silva', '', '123456789', 'maria@brocolis.com'),
(272, 'Pedro Silva', '', '123456789', 'pedro@brocolis.com'),
(273, 'Ana Silva', '', '123456789', 'ana@brocolis.com'),
(274, 'João Silva III', '', '123456789', 'joaoiii@brocolis.com'),
(275, 'Maria Silva Jr.', '', '123456789', 'mariajr@brocolis.com'),
(276, 'Pedro Silva Jr.', '', '123456789', 'pedrojr@brocolis.com'),
(277, 'Ana Silva Jr.', '', '123456789', 'anajr@brocolis.com'),
(278, 'João Silva IV', '', '123456789', 'joaoiv@brocolis.com'),
(279, 'Maria Silva III', '', '123456789', 'mariaiii@brocolis.com'),
(280, 'Pedro Silva III', '', '123456789', 'pedroiii@brocolis.com'),
(281, 'Ana Costa', '', '123456789', 'ana@brocolis.com'),
(282, 'João Silva Jr.', '', '123456789', 'joaojr@brocolis.com'),
(283, 'Maria Silva', '', '123456789', 'maria@brocolis.com'),
(284, 'Pedro Silva', '', '123456789', 'pedro@brocolis.com'),
(285, 'Ana Silva', '', '123456789', 'ana@brocolis.com'),
(286, 'Tiago III', '', '123456789', 'tiagoiii@brocolis.com'),
(287, 'Maria Silva Jr.', '', '123456789', 'mariajr@brocolis.com'),
(288, 'Pedro Silva Jr.', '', '123456789', 'pedrojr@brocolis.com'),
(289, 'Ana Silva Jr.', '', '123456789', 'anajr@brocolis.com'),
(290, 'Bartolomeu IV', '', '123456789', 'bartolomeuiv@brocolis.com'),
(291, 'Maria Silva III', '', '123456789', 'mariaiii@brocolis.com'),
(292, 'Filipe III', '', '123456789', 'filipeiii@brocolis.com'),
(293, 'João Silva', '', '123456789', 'joao@brocolis.com'),
(294, 'Maria Oliveira', '', '987654321', 'maria@brocolis.com'),
(295, 'Pedro Almeida', '', '456789123', 'pedro@brocolis.com'),
(296, 'Ana Costa', '', '123456789', 'ana@brocolis.com'),
(297, 'João Silva Jr.', '', '123456789', 'joaojr@brocolis.com'),
(298, 'Maria Silva', '', '123456789', 'maria@brocolis.com'),
(299, 'Pedro Silva', '', '123456789', 'pedro@brocolis.com'),
(300, 'Ana Silva', '', '123456789', 'ana@brocolis.com'),
(301, 'João Silva III', '', '123456789', 'joaoiii@brocolis.com'),
(302, 'Maria Silva Jr.', '', '123456789', 'mariajr@brocolis.com'),
(303, 'Pedro Silva Jr.', '', '123456789', 'pedrojr@brocolis.com'),
(304, 'Ana Silva Jr.', '', '123456789', 'anajr@brocolis.com'),
(305, 'João Silva IV', '', '123456789', 'joaoiv@brocolis.com'),
(306, 'Maria Silva III', '', '123456789', 'mariaiii@brocolis.com'),
(307, 'Pedro Silva III', '', '123456789', 'pedroiii@brocolis.com'),
(308, 'Ana Costa', '', '123456789', 'ana@brocolis.com'),
(309, 'João Silva Jr.', '', '123456789', 'joaojr@brocolis.com'),
(310, 'Maria Silva', '', '123456789', 'maria@brocolis.com'),
(311, 'Pedro Silva', '', '123456789', 'pedro@brocolis.com'),
(312, 'Ana Silva', '', '123456789', 'ana@brocolis.com'),
(313, 'Tiago III', '', '123456789', 'tiagoiii@brocolis.com'),
(314, 'Maria Silva Jr.', '', '123456789', 'mariajr@brocolis.com'),
(315, 'Pedro Silva Jr.', '', '123456789', 'pedrojr@brocolis.com'),
(316, 'Ana Silva Jr.', '', '123456789', 'anajr@brocolis.com'),
(317, 'Bartolomeu IV', '', '123456789', 'bartolomeuiv@brocolis.com'),
(318, 'Maria Silva III', '', '123456789', 'mariaiii@brocolis.com'),
(319, 'Filipe III', '', '123456789', 'filipeiii@brocolis.com'),
(320, 'João Silva', '', '123456789', 'joao@brocolis.com'),
(321, 'Maria Oliveira', '', '987654321', 'maria@brocolis.com'),
(322, 'Pedro Almeida', '', '456789123', 'pedro@brocolis.com'),
(323, 'Ana Costa', '', '123456789', 'ana@brocolis.com'),
(324, 'João Silva Jr.', '', '123456789', 'joaojr@brocolis.com'),
(325, 'Maria Silva', '', '123456789', 'maria@brocolis.com'),
(326, 'Pedro Silva', '', '123456789', 'pedro@brocolis.com'),
(327, 'Ana Silva', '', '123456789', 'ana@brocolis.com'),
(328, 'João Silva III', '', '123456789', 'joaoiii@brocolis.com'),
(329, 'Maria Silva Jr.', '', '123456789', 'mariajr@brocolis.com'),
(330, 'Pedro Silva Jr.', '', '123456789', 'pedrojr@brocolis.com'),
(331, 'Ana Silva Jr.', '', '123456789', 'anajr@brocolis.com'),
(332, 'João Silva IV', '', '123456789', 'joaoiv@brocolis.com'),
(333, 'Maria Silva III', '', '123456789', 'mariaiii@brocolis.com'),
(334, 'Pedro Silva III', '', '123456789', 'pedroiii@brocolis.com'),
(335, 'Ana Costa', '', '123456789', 'ana@brocolis.com'),
(336, 'João Silva Jr.', '', '123456789', 'joaojr@brocolis.com'),
(337, 'Maria Silva', '', '123456789', 'maria@brocolis.com'),
(338, 'Pedro Silva', '', '123456789', 'pedro@brocolis.com'),
(339, 'Ana Silva', '', '123456789', 'ana@brocolis.com'),
(340, 'Tiago III', '', '123456789', 'tiagoiii@brocolis.com'),
(341, 'Maria Silva Jr.', '', '123456789', 'mariajr@brocolis.com'),
(342, 'Pedro Silva Jr.', '', '123456789', 'pedrojr@brocolis.com'),
(343, 'Ana Silva Jr.', '', '123456789', 'anajr@brocolis.com'),
(344, 'Bartolomeu IV', '', '123456789', 'bartolomeuiv@brocolis.com'),
(345, 'Maria Silva III', '', '123456789', 'mariaiii@brocolis.com'),
(346, 'Filipe III', '', '123456789', 'filipeiii@brocolis.com'),
(347, 'João Silva', '', '123456789', 'joao@brocolis.com'),
(348, 'Maria Oliveira', '', '987654321', 'maria@brocolis.com'),
(349, 'Pedro Almeida', '', '456789123', 'pedro@brocolis.com'),
(350, 'Ana Costa', '', '123456789', 'ana@brocolis.com'),
(351, 'João Silva Jr.', '', '123456789', 'joaojr@brocolis.com'),
(352, 'Maria Silva', '', '123456789', 'maria@brocolis.com'),
(353, 'Pedro Silva', '', '123456789', 'pedro@brocolis.com'),
(354, 'Ana Silva', '', '123456789', 'ana@brocolis.com'),
(355, 'João Silva III', '', '123456789', 'joaoiii@brocolis.com'),
(356, 'Maria Silva Jr.', '', '123456789', 'mariajr@brocolis.com'),
(357, 'Pedro Silva Jr.', '', '123456789', 'pedrojr@brocolis.com'),
(358, 'Ana Silva Jr.', '', '123456789', 'anajr@brocolis.com'),
(359, 'João Silva IV', '', '123456789', 'joaoiv@brocolis.com'),
(360, 'Maria Silva III', '', '123456789', 'mariaiii@brocolis.com'),
(361, 'Pedro Silva III', '', '123456789', 'pedroiii@brocolis.com'),
(362, 'Ana Costa', '', '123456789', 'ana@brocolis.com'),
(363, 'João Silva Jr.', '', '123456789', 'joaojr@brocolis.com'),
(364, 'Maria Silva', '', '123456789', 'maria@brocolis.com'),
(365, 'Pedro Silva', '', '123456789', 'pedro@brocolis.com'),
(366, 'Ana Silva', '', '123456789', 'ana@brocolis.com'),
(367, 'Tiago III', '', '123456789', 'tiagoiii@brocolis.com'),
(368, 'Maria Silva Jr.', '', '123456789', 'mariajr@brocolis.com'),
(369, 'Pedro Silva Jr.', '', '123456789', 'pedrojr@brocolis.com'),
(370, 'Ana Silva Jr.', '', '123456789', 'anajr@brocolis.com'),
(371, 'Bartolomeu IV', '', '123456789', 'bartolomeuiv@brocolis.com'),
(372, 'Maria Silva III', '', '123456789', 'mariaiii@brocolis.com'),
(373, 'Filipe III', '', '123456789', 'filipeiii@brocolis.com'),
(1236, 'João Silva', '', '123456789', NULL),
(1237, 'João Silva', '', '123456789', 'joao@brocolis.com'),
(1238, 'Maria Oliveira', '', '987654321', 'maria@brocolis.com'),
(1239, 'Pedro Almeida', '', '456789123', 'pedro@brocolis.com'),
(1240, 'Ana Costa', '', '123456789', 'ana@brocolis.com'),
(1241, 'João Silva Jr.', '', '123456789', 'joaojr@brocolis.com'),
(1242, 'Maria Silva', '', '123456789', 'maria@brocolis.com'),
(1243, 'Pedro Silva', '', '123456789', 'pedro@brocolis.com'),
(1244, 'Ana Silva', '', '123456789', 'ana@brocolis.com'),
(1245, 'João Silva III', '', '123456789', 'joaoiii@brocolis.com'),
(1246, 'Maria Silva Jr.', '', '123456789', 'mariajr@brocolis.com'),
(1247, 'Pedro Silva Jr.', '', '123456789', 'pedrojr@brocolis.com'),
(1248, 'Ana Silva Jr.', '', '123456789', 'anajr@brocolis.com'),
(1249, 'João Silva IV', '', '123456789', 'joaoiv@brocolis.com'),
(1250, 'Maria Silva III', '', '123456789', 'mariaiii@brocolis.com'),
(1251, 'Pedro Silva III', '', '123456789', 'pedroiii@brocolis.com'),
(1252, 'Ana Costa', '', '123456789', 'ana@brocolis.com'),
(1253, 'João Silva Jr.', '', '123456789', 'joaojr@brocolis.com'),
(1254, 'Maria Silva', '', '123456789', 'maria@brocolis.com'),
(1255, 'Pedro Silva', '', '123456789', 'pedro@brocolis.com'),
(1256, 'Ana Silva', '', '123456789', 'ana@brocolis.com'),
(1257, 'Tiago III', '', '123456789', 'tiagoiii@brocolis.com'),
(1258, 'Maria Silva Jr.', '', '123456789', 'mariajr@brocolis.com'),
(1259, 'Pedro Silva Jr.', '', '123456789', 'pedrojr@brocolis.com'),
(1260, 'Ana Silva Jr.', '', '123456789', 'anajr@brocolis.com'),
(1261, 'Bartolomeu IV', '', '123456789', 'bartolomeuiv@brocolis.com'),
(1262, 'Maria Silva III', '', '123456789', 'mariaiii@brocolis.com'),
(1263, 'Filipe III', '', '123456789', 'filipeiii@brocolis.com'),
(1264, 'João Silva', '', '123456789', 'joao@brocolis.com'),
(1265, 'Maria Oliveira', '', '987654321', 'maria@brocolis.com'),
(1266, 'Pedro Almeida', '', '456789123', 'pedro@brocolis.com'),
(1267, 'Ana Costa', '', '123456789', 'ana@brocolis.com'),
(1268, 'João Silva Jr.', '', '123456789', 'joaojr@brocolis.com'),
(1269, 'Maria Silva', '', '123456789', 'maria@brocolis.com'),
(1270, 'Pedro Silva', '', '123456789', 'pedro@brocolis.com'),
(1271, 'Ana Silva', '', '123456789', 'ana@brocolis.com'),
(1272, 'João Silva III', '', '123456789', 'joaoiii@brocolis.com'),
(1273, 'Maria Silva Jr.', '', '123456789', 'mariajr@brocolis.com'),
(1274, 'Pedro Silva Jr.', '', '123456789', 'pedrojr@brocolis.com'),
(1275, 'Ana Silva Jr.', '', '123456789', 'anajr@brocolis.com'),
(1276, 'João Silva IV', '', '123456789', 'joaoiv@brocolis.com'),
(1277, 'Maria Silva III', '', '123456789', 'mariaiii@brocolis.com'),
(1278, 'Pedro Silva III', '', '123456789', 'pedroiii@brocolis.com'),
(1279, 'Ana Costa', '', '123456789', 'ana@brocolis.com'),
(1280, 'João Silva Jr.', '', '123456789', 'joaojr@brocolis.com'),
(1281, 'Maria Silva', '', '123456789', 'maria@brocolis.com'),
(1282, 'Pedro Silva', '', '123456789', 'pedro@brocolis.com'),
(1283, 'Ana Silva', '', '123456789', 'ana@brocolis.com'),
(1284, 'Tiago III', '', '123456789', 'tiagoiii@brocolis.com'),
(1285, 'Maria Silva Jr.', '', '123456789', 'mariajr@brocolis.com'),
(1286, 'Pedro Silva Jr.', '', '123456789', 'pedrojr@brocolis.com'),
(1287, 'Ana Silva Jr.', '', '123456789', 'anajr@brocolis.com'),
(1288, 'Bartolomeu IV', '', '123456789', 'bartolomeuiv@brocolis.com'),
(1289, 'Maria Silva III', '', '123456789', 'mariaiii@brocolis.com'),
(1290, 'Filipe III', '', '123456789', 'filipeiii@brocolis.com'),
(1291, 'João Silva', '', '123456789', 'joao@brocolis.com'),
(1292, 'Maria Oliveira', '', '987654321', 'maria@brocolis.com'),
(1293, 'Pedro Almeida', '', '456789123', 'pedro@brocolis.com'),
(1294, 'Ana Costa', '', '123456789', 'ana@brocolis.com'),
(1295, 'João Silva Jr.', '', '123456789', 'joaojr@brocolis.com'),
(1296, 'Maria Silva', '', '123456789', 'maria@brocolis.com'),
(1297, 'Pedro Silva', '', '123456789', 'pedro@brocolis.com'),
(1298, 'Ana Silva', '', '123456789', 'ana@brocolis.com'),
(1299, 'João Silva III', '', '123456789', 'joaoiii@brocolis.com'),
(1300, 'Maria Silva Jr.', '', '123456789', 'mariajr@brocolis.com'),
(1301, 'Pedro Silva Jr.', '', '123456789', 'pedrojr@brocolis.com'),
(1302, 'Ana Silva Jr.', '', '123456789', 'anajr@brocolis.com'),
(1303, 'João Silva IV', '', '123456789', 'joaoiv@brocolis.com'),
(1304, 'Maria Silva III', '', '123456789', 'mariaiii@brocolis.com'),
(1305, 'Pedro Silva III', '', '123456789', 'pedroiii@brocolis.com'),
(1306, 'Ana Costa', '', '123456789', 'ana@brocolis.com'),
(1307, 'João Silva Jr.', '', '123456789', 'joaojr@brocolis.com'),
(1308, 'Maria Silva', '', '123456789', 'maria@brocolis.com'),
(1309, 'Pedro Silva', '', '123456789', 'pedro@brocolis.com'),
(1310, 'Ana Silva', '', '123456789', 'ana@brocolis.com'),
(1311, 'Tiago III', '', '123456789', 'tiagoiii@brocolis.com'),
(1312, 'Maria Silva Jr.', '', '123456789', 'mariajr@brocolis.com'),
(1313, 'Pedro Silva Jr.', '', '123456789', 'pedrojr@brocolis.com'),
(1314, 'Ana Silva Jr.', '', '123456789', 'anajr@brocolis.com'),
(1315, 'Bartolomeu IV', '', '123456789', 'bartolomeuiv@brocolis.com'),
(1316, 'Maria Silva III', '', '123456789', 'mariaiii@brocolis.com'),
(1317, 'Filipe III', '', '123456789', 'filipeiii@brocolis.com'),
(1318, 'João Silva', '', '123456789', 'joao@brocolis.com'),
(1319, 'Maria Oliveira', '', '987654321', 'maria@brocolis.com'),
(1320, 'Pedro Almeida', '', '456789123', 'pedro@brocolis.com'),
(1321, 'Ana Costa', '', '123456789', 'ana@brocolis.com'),
(1322, 'João Silva Jr.', '', '123456789', 'joaojr@brocolis.com'),
(1323, 'Maria Silva', '', '123456789', 'maria@brocolis.com'),
(1324, 'Pedro Silva', '', '123456789', 'pedro@brocolis.com'),
(1325, 'Ana Silva', '', '123456789', 'ana@brocolis.com'),
(1326, 'João Silva III', '', '123456789', 'joaoiii@brocolis.com'),
(1327, 'Maria Silva Jr.', '', '123456789', 'mariajr@brocolis.com'),
(1328, 'Pedro Silva Jr.', '', '123456789', 'pedrojr@brocolis.com'),
(1329, 'Ana Silva Jr.', '', '123456789', 'anajr@brocolis.com'),
(1330, 'João Silva IV', '', '123456789', 'joaoiv@brocolis.com'),
(1331, 'Maria Silva III', '', '123456789', 'mariaiii@brocolis.com'),
(1332, 'Pedro Silva III', '', '123456789', 'pedroiii@brocolis.com'),
(1333, 'Ana Costa', '', '123456789', 'ana@brocolis.com'),
(1334, 'João Silva Jr.', '', '123456789', 'joaojr@brocolis.com'),
(1335, 'Maria Silva', '', '123456789', 'maria@brocolis.com'),
(1336, 'Pedro Silva', '', '123456789', 'pedro@brocolis.com'),
(1337, 'Ana Silva', '', '123456789', 'ana@brocolis.com'),
(1338, 'Tiago III', '', '123456789', 'tiagoiii@brocolis.com'),
(1339, 'Maria Silva Jr.', '', '123456789', 'mariajr@brocolis.com'),
(1340, 'Pedro Silva Jr.', '', '123456789', 'pedrojr@brocolis.com'),
(1341, 'Ana Silva Jr.', '', '123456789', 'anajr@brocolis.com'),
(1342, 'Bartolomeu IV', '', '123456789', 'bartolomeuiv@brocolis.com'),
(1343, 'Maria Silva III', '', '123456789', 'mariaiii@brocolis.com'),
(1344, 'Filipe III', '', '123456789', 'filipeiii@brocolis.com'),
(1345, 'João Silva', '', '123456789', 'joao@brocolis.com'),
(1346, 'Maria Oliveira', '', '987654321', 'maria@brocolis.com'),
(1347, 'Pedro Almeida', '', '456789123', 'pedro@brocolis.com'),
(1348, 'Ana Costa', '', '123456789', 'ana@brocolis.com'),
(1349, 'João Silva Jr.', '', '123456789', 'joaojr@brocolis.com'),
(1350, 'Maria Silva', '', '123456789', 'maria@brocolis.com'),
(1351, 'Pedro Silva', '', '123456789', 'pedro@brocolis.com'),
(1352, 'Ana Silva', '', '123456789', 'ana@brocolis.com'),
(1353, 'João Silva III', '', '123456789', 'joaoiii@brocolis.com'),
(1354, 'Maria Silva Jr.', '', '123456789', 'mariajr@brocolis.com'),
(1355, 'Pedro Silva Jr.', '', '123456789', 'pedrojr@brocolis.com'),
(1356, 'Ana Silva Jr.', '', '123456789', 'anajr@brocolis.com'),
(1357, 'João Silva IV', '', '123456789', 'joaoiv@brocolis.com'),
(1358, 'Maria Silva III', '', '123456789', 'mariaiii@brocolis.com'),
(1359, 'Pedro Silva III', '', '123456789', 'pedroiii@brocolis.com'),
(1360, 'Ana Costa', '', '123456789', 'ana@brocolis.com'),
(1361, 'João Silva Jr.', '', '123456789', 'joaojr@brocolis.com'),
(1362, 'Maria Silva', '', '123456789', 'maria@brocolis.com'),
(1363, 'Pedro Silva', '', '123456789', 'pedro@brocolis.com'),
(1364, 'Ana Silva', '', '123456789', 'ana@brocolis.com'),
(1365, 'Tiago III', '', '123456789', 'tiagoiii@brocolis.com'),
(1366, 'Maria Silva Jr.', '', '123456789', 'mariajr@brocolis.com'),
(1367, 'Pedro Silva Jr.', '', '123456789', 'pedrojr@brocolis.com'),
(1368, 'Ana Silva Jr.', '', '123456789', 'anajr@brocolis.com'),
(1369, 'Bartolomeu IV', '', '123456789', 'bartolomeuiv@brocolis.com'),
(1370, 'Maria Silva III', '', '123456789', 'mariaiii@brocolis.com'),
(1371, 'Filipe III', '', '123456789', 'filipeiii@brocolis.com'),
(1372, 'João Silva', '', '123456789', 'joao@brocolis.com'),
(1373, 'Maria Oliveira', '', '987654321', 'maria@brocolis.com'),
(1374, 'Pedro Almeida', '', '456789123', 'pedro@brocolis.com'),
(1375, 'Ana Costa', '', '123456789', 'ana@brocolis.com'),
(1376, 'João Silva Jr.', '', '123456789', 'joaojr@brocolis.com'),
(1377, 'Maria Silva', '', '123456789', 'maria@brocolis.com'),
(1378, 'Pedro Silva', '', '123456789', 'pedro@brocolis.com'),
(1379, 'Ana Silva', '', '123456789', 'ana@brocolis.com'),
(1380, 'João Silva III', '', '123456789', 'joaoiii@brocolis.com'),
(1381, 'Maria Silva Jr.', '', '123456789', 'mariajr@brocolis.com'),
(1382, 'Pedro Silva Jr.', '', '123456789', 'pedrojr@brocolis.com'),
(1383, 'Ana Silva Jr.', '', '123456789', 'anajr@brocolis.com'),
(1384, 'João Silva IV', '', '123456789', 'joaoiv@brocolis.com'),
(1385, 'Maria Silva III', '', '123456789', 'mariaiii@brocolis.com'),
(1386, 'Pedro Silva III', '', '123456789', 'pedroiii@brocolis.com'),
(1387, 'Ana Costa', '', '123456789', 'ana@brocolis.com'),
(1388, 'João Silva Jr.', '', '123456789', 'joaojr@brocolis.com'),
(1389, 'Maria Silva', '', '123456789', 'maria@brocolis.com'),
(1390, 'Pedro Silva', '', '123456789', 'pedro@brocolis.com'),
(1391, 'Ana Silva', '', '123456789', 'ana@brocolis.com'),
(1392, 'Tiago III', '', '123456789', 'tiagoiii@brocolis.com'),
(1393, 'Maria Silva Jr.', '', '123456789', 'mariajr@brocolis.com'),
(1394, 'Pedro Silva Jr.', '', '123456789', 'pedrojr@brocolis.com'),
(1395, 'Ana Silva Jr.', '', '123456789', 'anajr@brocolis.com'),
(1396, 'Bartolomeu IV', '', '123456789', 'bartolomeuiv@brocolis.com'),
(1397, 'Maria Silva III', '', '123456789', 'mariaiii@brocolis.com'),
(1398, 'Filipe III', '', '123456789', 'filipeiii@brocolis.com'),
(1399, 'João Silva', '', '123456789', 'joao@brocolis.com'),
(1400, 'Maria Oliveira', '', '987654321', 'maria@brocolis.com'),
(1401, 'Pedro Almeida', '', '456789123', 'pedro@brocolis.com'),
(1402, 'Ana Costa', '', '123456789', 'ana@brocolis.com'),
(1403, 'João Silva Jr.', '', '123456789', 'joaojr@brocolis.com'),
(1404, 'Maria Silva', '', '123456789', 'maria@brocolis.com'),
(1405, 'Pedro Silva', '', '123456789', 'pedro@brocolis.com'),
(1406, 'Ana Silva', '', '123456789', 'ana@brocolis.com'),
(1407, 'João Silva III', '', '123456789', 'joaoiii@brocolis.com'),
(1408, 'Maria Silva Jr.', '', '123456789', 'mariajr@brocolis.com'),
(1409, 'Pedro Silva Jr.', '', '123456789', 'pedrojr@brocolis.com'),
(1410, 'Ana Silva Jr.', '', '123456789', 'anajr@brocolis.com'),
(1411, 'João Silva IV', '', '123456789', 'joaoiv@brocolis.com'),
(1412, 'Maria Silva III', '', '123456789', 'mariaiii@brocolis.com'),
(1413, 'Pedro Silva III', '', '123456789', 'pedroiii@brocolis.com'),
(1414, 'Ana Costa', '', '123456789', 'ana@brocolis.com'),
(1415, 'João Silva Jr.', '', '123456789', 'joaojr@brocolis.com'),
(1416, 'Maria Silva', '', '123456789', 'maria@brocolis.com'),
(1417, 'Pedro Silva', '', '123456789', 'pedro@brocolis.com'),
(1418, 'Ana Silva', '', '123456789', 'ana@brocolis.com'),
(1419, 'Tiago III', '', '123456789', 'tiagoiii@brocolis.com'),
(1420, 'Maria Silva Jr.', '', '123456789', 'mariajr@brocolis.com'),
(1421, 'Pedro Silva Jr.', '', '123456789', 'pedrojr@brocolis.com'),
(1422, 'Ana Silva Jr.', '', '123456789', 'anajr@brocolis.com'),
(1423, 'Bartolomeu IV', '', '123456789', 'bartolomeuiv@brocolis.com'),
(1424, 'Maria Silva III', '', '123456789', 'mariaiii@brocolis.com'),
(1425, 'Filipe III', '', '123456789', 'filipeiii@brocolis.com');

-- --------------------------------------------------------

--
-- Estrutura para tabela `ingredientes`
--

CREATE TABLE `ingredientes` (
  `ingrediente_id` int(11) NOT NULL,
  `nome` varchar(255) NOT NULL,
  `tipo` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `itens_pedido`
--

CREATE TABLE `itens_pedido` (
  `item_pedido_id` int(11) NOT NULL,
  `pedido_id` int(11) NOT NULL,
  `pizza_id` int(11) NOT NULL,
  `quantidade` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `pedidos`
--

CREATE TABLE `pedidos` (
  `pedido_id` int(11) NOT NULL,
  `cliente_id` int(11) NOT NULL,
  `data_hora_pedido` datetime NOT NULL,
  `forma_pagamento` varchar(255) NOT NULL,
  `status` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `pedidos`
--

INSERT INTO `pedidos` (`pedido_id`, `cliente_id`, `data_hora_pedido`, `forma_pagamento`, `status`) VALUES
(1, 1, '2024-06-19 15:59:00', 'Cartão de Crédito', 'Pendente'),
(3, 3, '2024-06-19 15:59:00', 'Cartão de Crédito', 'Pendente'),
(4, 4, '2024-06-19 15:59:00', 'Cartão de Crédito', 'Pendente'),
(5, 5, '2024-06-19 15:59:00', 'Cartão de Crédito', 'Pendente'),
(6, 6, '2024-06-19 15:59:00', 'Cartão de Crédito', 'Pendente'),
(7, 7, '2024-06-19 15:59:00', 'Cartão de Crédito', 'Pendente'),
(8, 8, '2024-06-19 15:59:00', 'Cartão de Crédito', 'Pendente'),
(9, 9, '2024-06-19 15:59:00', 'Cartão de Crédito', 'Pendente'),
(10, 10, '2024-06-19 15:59:00', 'Cartão de Crédito', 'Pendente'),
(11, 11, '2024-06-19 15:59:00', 'Cartão de Crédito', 'Pendente'),
(14, 14, '2024-06-19 15:59:00', 'Cartão de Crédito', 'Pendente'),
(15, 15, '2024-06-19 15:59:00', 'Cartão de Crédito', 'Pendente'),
(16, 16, '2024-06-19 15:59:00', 'Cartão de Crédito', 'Pendente'),
(17, 17, '2024-06-19 15:59:00', 'Cartão de Crédito', 'Pendente'),
(18, 18, '2024-06-19 15:59:00', 'Cartão de Crédito', 'Pendente'),
(19, 19, '2024-06-19 15:59:00', 'Cartão de Crédito', 'Pendente'),
(20, 20, '2024-06-19 15:59:00', 'Cartão de Crédito', 'Pendente'),
(21, 21, '2024-06-19 15:59:00', 'Cartão de Crédito', 'Pendente'),
(22, 22, '2024-06-19 15:59:00', 'Cartão de Crédito', 'Pendente'),
(23, 23, '2024-06-19 15:59:00', 'Cartão de Crédito', 'Pendente'),
(24, 24, '2024-06-19 15:59:00', 'Cartão de Crédito', 'Pendente');

-- --------------------------------------------------------

--
-- Estrutura para tabela `pizzas`
--

CREATE TABLE `pizzas` (
  `pizza_id` int(11) NOT NULL,
  `nome` varchar(255) NOT NULL,
  `tamanho` varchar(255) NOT NULL,
  `preco` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `pizza_ingredientes`
--

CREATE TABLE `pizza_ingredientes` (
  `pizza_ingrediente_id` int(11) NOT NULL,
  `pizza_id` int(11) NOT NULL,
  `ingrediente_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `t1`
--

CREATE TABLE `t1` (
  `id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `t1`
--

INSERT INTO `t1` (`id`) VALUES
(1);

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`cliente_id`);

--
-- Índices de tabela `ingredientes`
--
ALTER TABLE `ingredientes`
  ADD PRIMARY KEY (`ingrediente_id`);

--
-- Índices de tabela `itens_pedido`
--
ALTER TABLE `itens_pedido`
  ADD PRIMARY KEY (`item_pedido_id`),
  ADD KEY `pedido_id` (`pedido_id`),
  ADD KEY `pizza_id` (`pizza_id`);

--
-- Índices de tabela `pedidos`
--
ALTER TABLE `pedidos`
  ADD PRIMARY KEY (`pedido_id`),
  ADD KEY `cliente_id` (`cliente_id`);

--
-- Índices de tabela `pizzas`
--
ALTER TABLE `pizzas`
  ADD PRIMARY KEY (`pizza_id`);

--
-- Índices de tabela `pizza_ingredientes`
--
ALTER TABLE `pizza_ingredientes`
  ADD PRIMARY KEY (`pizza_ingrediente_id`),
  ADD KEY `pizza_id` (`pizza_id`),
  ADD KEY `ingrediente_id` (`ingrediente_id`);

--
-- Índices de tabela `t1`
--
ALTER TABLE `t1`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `clientes`
--
ALTER TABLE `clientes`
  MODIFY `cliente_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1426;

--
-- AUTO_INCREMENT de tabela `ingredientes`
--
ALTER TABLE `ingredientes`
  MODIFY `ingrediente_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `itens_pedido`
--
ALTER TABLE `itens_pedido`
  MODIFY `item_pedido_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `pedidos`
--
ALTER TABLE `pedidos`
  MODIFY `pedido_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;

--
-- AUTO_INCREMENT de tabela `pizzas`
--
ALTER TABLE `pizzas`
  MODIFY `pizza_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `pizza_ingredientes`
--
ALTER TABLE `pizza_ingredientes`
  MODIFY `pizza_ingrediente_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `itens_pedido`
--
ALTER TABLE `itens_pedido`
  ADD CONSTRAINT `itens_pedido_ibfk_1` FOREIGN KEY (`pedido_id`) REFERENCES `pedidos` (`pedido_id`),
  ADD CONSTRAINT `itens_pedido_ibfk_2` FOREIGN KEY (`pizza_id`) REFERENCES `pizzas` (`pizza_id`);

--
-- Restrições para tabelas `pedidos`
--
ALTER TABLE `pedidos`
  ADD CONSTRAINT `pedidos_ibfk_1` FOREIGN KEY (`cliente_id`) REFERENCES `clientes` (`cliente_id`);

--
-- Restrições para tabelas `pizza_ingredientes`
--
ALTER TABLE `pizza_ingredientes`
  ADD CONSTRAINT `pizza_ingredientes_ibfk_1` FOREIGN KEY (`pizza_id`) REFERENCES `pizzas` (`pizza_id`),
  ADD CONSTRAINT `pizza_ingredientes_ibfk_2` FOREIGN KEY (`ingrediente_id`) REFERENCES `ingredientes` (`ingrediente_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
