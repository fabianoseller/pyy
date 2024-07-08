-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 06/07/2024 às 01:01
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
-- Banco de dados: `pythonbas`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `contatos`
--

CREATE TABLE `contatos` (
  `id` int(11) NOT NULL,
  `nome` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `mensagem` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `contatos`
--

INSERT INTO `contatos` (`id`, `nome`, `email`, `mensagem`) VALUES
(1, 'Fabiano', 'rudolfino@lasla.com', '12345678900000'),
(2, 'Rudolfino da silva', 'wolfganzebrasilas@silas.com.br', 'PORTASSSSSSSSSSSSSSSSSSSSSSSS'),
(3, 'Rudolfino da silva', 'rudolfin23@lasla.com', '3333333333333333333333333333333333333333333333333333333'),
(4, 'lalala4', 'lalala4@gmail.com', 'uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu555555555555555555555555'),
(5, 'lalala4', 'lalala4@gmail.com', 'Main Purpose:Founded in 1993, Trafigura is one of the largest physical commodities trading groups in the world. Trafigura sources, stores, transports and delivers a range of raw materials (including oil and refined products and metals and minerals) to clients around the world. The trading business is supported by industrial and financial assets, including 49.6 percent owned global oil products storage and distribution company Puma Energy; global terminals, warehousing and logistics operator Impala Terminals; Trafigura\'s Mining Group; 50 percent owned DT Group which specialises in logistics and trading; and Galena Asset Management. MAIN PURPOSE:As an operator, you are an enthusiastic self-starter with a strong interest in crafting and maintaining excellent business relationships.Given that the role will involve regular discussions with both traders and foreign clients regarding a wide range of commercial issues, a dynamic personality coupled with an ability to work under pressure are fundamental to your success.Knowledge Skills and Abilities, Key'),
(6, 'lalala5', 'lalala5@ugi.uy', 'Estamos buscando uma profissional para a posição de Assessora de Comunicação. A candidata ideal deve ser dinâmica, criativa e proativa, com habilidades para planejar e organizar, além de estar conectada com as mídias com foco em moda e que conectem com o segmento.');

-- --------------------------------------------------------

--
-- Estrutura para tabela `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `users`
--

INSERT INTO `users` (`id`, `username`, `password`, `email`) VALUES
(1, 'lalala', 'scrypt:32768:8:1$hLfHxTNgUgNjQ94Z$4a5fa474f2a027152db34fd239333f442a2f97c0bb1be5d49a6e9c519d34a718bb97f7a152ad80d30546172ce1001fd0f24e54bf9a2378e94419bcd365a7ed86', 'lala1@lala1.com'),
(2, 'Wolfgan Zebra Silas', 'scrypt:32768:8:1$ffTm3hoCqp4I5kUI$2a9814ee841d59a31c5fd05ea5b4c4edd4e8238acf6b1b2aad6a544cacaee4f7b69a7a60e459abea9a5590d3dfecccdc82c287732d269a7caa143d1e1d9cc826', 'wolfganzebrasilas@silas.com.br'),
(3, 'Wolfgan Zebra SAGU', 'scrypt:32768:8:1$0dlYMCYKfx97XoLQ$6ea612479ec616ce5dc8d2077f9f4fbac0472365ea250aa7c18b324f6bf7797c1aee862d6b6b17adcb5022d37cb28529de21937c0b2fbc5233aa1e19fa9aef8e', 'wolfganzebrasilas@silassagu.com.br'),
(4, 'Wolfgan Zebra SAGU1', 'scrypt:32768:8:1$wCV4emS2603PATbf$af3eba4617c35d5e6719da83f564fefa77b8020e0988bfad8b8aeb67b257c9965d6c83bab31eff60cfefb7b708c4109dac591fd99d2fd0522bd47489124c3258', 'wolfganzebrasilas@silassagu.com.br'),
(5, 'lalala2', 'scrypt:32768:8:1$HtMwvGYdzYUyFGGp$78b39bce225767db0ea835808f66136cc4f53ccf53615bd73a6669b43f18f95e2867f3a1fefd546cdc8383a0352103832a68c83cd1836c7bd051306da9de239b', 'lala1@lala2.com'),
(6, 'Wolfgan Zebra Silas3', 'scrypt:32768:8:1$b4H3krnIvVoEyFPL$1f6df1a68aedfc9b14157c10069fbce4c770232a3c180adc07b4cef73b4b709bd8f5d7dabd40be1411df791fa0199c0036aeeba5049e5af44cebd13052c0df1a', 'wolfganzebrasilas@silassagu.com.br'),
(7, 'Wolfgan Zebra Silas5', 'scrypt:32768:8:1$qPHHAVBuTKfkHYIC$c09ed13dc21293ce086e21f9980ad0e1a7e35ea0d211d7e62778d656fe5a33188703e71f9cb10f384ef2693f29a160d340a53eda48562c9f6b768962f0ecf180', 'wolfganzebrasilas5@silassagu.com.br'),
(8, 'Wolfgan Zebra Silas36', 'scrypt:32768:8:1$pI8mWuwUHnhgq7D0$834939950893d92dd87484a868f0ae6fe3f0395b338cf02b9ceec50338d912794f5f8fd8f077306596a4057dbc9072539ea1637515266feccdc6a9dea3c11dd4', 'wolfganzebrasilas@silas36.com.br'),
(9, 'lalala4', 'scrypt:32768:8:1$RhUPX98mIttowGxz$44eb0e8d4f86892e5078e8c99b598147042c49eafb0e799655313b68d098bb474913fbd6877f992e430bfc3b75c2e07cbae82581adaaffca6907eaccc6166cc3', 'lalala2@gmail.com'),
(10, 'lalala5', 'scrypt:32768:8:1$ZOClu5U05H4X83Wl$d5403b1402c353cef0bc0c54f00eb4cf6521ee003934afa023dcb099cb0003b00dc3bfc124725bae47d4063fa41fd550f41eedb31cfeab6a29719ad1428aebf5', 'lalala5@ugi.uy');

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `contatos`
--
ALTER TABLE `contatos`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `contatos`
--
ALTER TABLE `contatos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de tabela `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
