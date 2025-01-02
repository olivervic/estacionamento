-- phpMyAdmin SQL Dump
-- version 5.2.1deb3
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Tempo de geração: 02/01/2025 às 12:12
-- Versão do servidor: 8.0.40-0ubuntu0.24.04.1
-- Versão do PHP: 8.3.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `estacionamento`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `carros`
--

CREATE TABLE `carros` (
  `id` int NOT NULL,
  `carro` varchar(20) NOT NULL,
  `placa` varchar(10) NOT NULL,
  `responsavel` varchar(100) NOT NULL,
  `vaga` int NOT NULL,
  `horario_entrada` time NOT NULL,
  `horario_saida` time NOT NULL,
  `dia_semana` varchar(50) NOT NULL,
  `alterado_por` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `carros`
--

INSERT INTO `carros` (`id`, `carro`, `placa`, `responsavel`, `vaga`, `horario_entrada`, `horario_saida`, `dia_semana`, `alterado_por`) VALUES
(1, 'Ford Fiesta', 'OPA-8979', 'Bruno ', 1, '00:00:00', '00:00:00', 'qui', 1),
(152, 'Ford Fiesta', 'HNA-4811', 'Vinícius Campos', 1, '00:00:00', '00:00:00', 'seg-sex', NULL),
(153, 'Honda Fit', 'HHT-6285', 'Luciano Correia', 5, '00:00:00', '00:00:00', 'seg-dom', NULL),
(154, 'Hyundai Creta', 'QSJ-2A49', 'Elaine do Carmo', 6, '00:00:00', '00:00:00', 'seg-dom', NULL),
(155, 'Tracker', 'TCH-2B28', 'Caroline dos Santos', 7, '00:00:00', '00:00:00', 'seg-dom', NULL),
(156, 'HRV', 'QMX-0868', 'Sérgio de Paula', 9, '00:00:00', '00:00:00', 'seg-dom', NULL),
(157, 'Uno Sporting', 'OWH-2C06', 'Fernando Tibúrcio', 10, '00:00:00', '00:00:00', 'seg-dom', NULL),
(158, 'Bravo Sporting', 'GOG-0002', 'Felipe Wang', 11, '00:00:00', '00:00:00', 'seg-dom', NULL),
(159, 'Ford Fiesta', 'OPA-8979', 'Bruno Neves', 1, '00:00:00', '00:00:00', 'seg-sex', NULL),
(177, 'Toyota Etios', 'QNQ-2056', 'Mariana', 28, '08:00:00', '19:00:00', 'SEG-SEX', NULL),
(178, 'HB20', 'SIB-9I53', 'André | Aline', 29, '08:00:00', '19:00:00', 'SEG-SEX', NULL),
(179, 'Fiat Cronos', 'SIM-9E14', 'Terence', 31, '08:00:00', '19:00:00', 'SEG-SEX', NULL),
(268, 'Sandero', 'OQV-8650', 'Patrícia Pinho', 33, '08:00:00', '19:00:00', 'SEG-SEX', NULL),
(269, 'Polo', 'SIF-5A06', 'Léo Avelino', 35, '08:00:00', '19:00:00', 'SEG-SEX', NULL),
(270, 'Onix', 'OWM-3075', 'Téssia Gonçalves', 36, '08:00:00', '19:00:00', 'SEG-SEX', NULL),
(271, 'Ford Ecosport', 'HIC-6E02', 'Júnior de Castro', 37, '08:00:00', '19:00:00', 'SEG-SEX', NULL),
(272, 'Virtus', 'RNP-5D55', 'Lorena', 38, '08:00:00', '19:00:00', 'qui', NULL),
(273, 'Fox Vermelho', 'HNU-2682', 'Carla', 39, '08:00:00', '19:00:00', 'SEG-SEX', NULL),
(274, 'Pajero TR4', 'HCJ-6518', 'Magela', 40, '08:00:00', '19:00:00', 'SEG-SEX', NULL),
(275, 'Nivus', 'SHI-7A94', 'Cadu Doné', 41, '08:00:00', '19:00:00', 'SEG-SEX', NULL),
(276, 'HB20', 'RNB-8E00', 'Pedro Rocha', 44, '08:00:00', '19:00:00', 'SEG-SEX', NULL),
(277, 'Toyota Etios', 'PXA-1439', 'Débora Rajão', 46, '08:00:00', '19:00:00', 'SEG-SEX', NULL),
(278, 'Palio Prata', 'HIX-3705', 'Márcio Rônei', 47, '08:00:00', '19:00:00', 'SEG-SEX', NULL),
(279, 'Fiat Mobi', 'PYK-2645', 'Regina Palla', 48, '08:00:00', '19:00:00', 'SEG-SEX', NULL),
(280, 'HB20', 'PYA-3502', 'PYA-3502', 49, '08:00:00', '19:00:00', 'SEG-SEX', NULL);

-- --------------------------------------------------------

--
-- Estrutura para tabela `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int NOT NULL,
  `nome` varchar(100) NOT NULL,
  `email` varchar(150) NOT NULL,
  `senha` varchar(255) NOT NULL,
  `permissao` enum('visualizar','editar') DEFAULT 'visualizar',
  `criado_em` timestamp NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `usuarios`
--

INSERT INTO `usuarios` (`id`, `nome`, `email`, `senha`, `permissao`, `criado_em`) VALUES
(1, 'netadmin', 'estacionamento@emc.mg.gov.br', 'teste', 'editar', '2024-11-25 14:01:07'),
(2, 'convidado', 'convidado@emc.mg.gov.br', 'teste', 'visualizar', '2024-11-25 14:01:07'),
(3, 'victor.oliveira', 'victor.oliveira@redeminas.mg.gov.br', 'teste', 'editar', '2024-11-25 14:01:07'),
(4, 'portaria', 'portaria@emc.mg.gov.br', 'teste', 'visualizar', '2024-11-25 14:01:07'),
(5, 'bruno.neves', 'bruno.neves@emc.mg.gov.br', 'teste', 'editar', '2024-11-25 14:01:07');

-- --------------------------------------------------------

--
-- Estrutura para tabela `usuarios_vagas`
--

CREATE TABLE `usuarios_vagas` (
  `id` int NOT NULL,
  `usuario_id` int NOT NULL,
  `vaga` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `usuarios_vagas`
--

INSERT INTO `usuarios_vagas` (`id`, `usuario_id`, `vaga`) VALUES
(17, 5, 1);

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `carros`
--
ALTER TABLE `carros`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_alterado_por` (`alterado_por`),
  ADD KEY `vaga` (`vaga`);

--
-- Índices de tabela `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Índices de tabela `usuarios_vagas`
--
ALTER TABLE `usuarios_vagas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `usuario_id` (`usuario_id`),
  ADD KEY `vaga` (`vaga`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `carros`
--
ALTER TABLE `carros`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=281;

--
-- AUTO_INCREMENT de tabela `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de tabela `usuarios_vagas`
--
ALTER TABLE `usuarios_vagas`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `carros`
--
ALTER TABLE `carros`
  ADD CONSTRAINT `fk_alterado_por` FOREIGN KEY (`alterado_por`) REFERENCES `usuarios` (`id`),
  ADD CONSTRAINT `fk_usuario_alteracao` FOREIGN KEY (`alterado_por`) REFERENCES `usuarios` (`id`);

--
-- Restrições para tabelas `usuarios_vagas`
--
ALTER TABLE `usuarios_vagas`
  ADD CONSTRAINT `usuarios_vagas_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`),
  ADD CONSTRAINT `usuarios_vagas_ibfk_2` FOREIGN KEY (`vaga`) REFERENCES `carros` (`vaga`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
