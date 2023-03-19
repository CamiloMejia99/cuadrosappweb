-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 15-03-2023 a las 00:11:53
-- Versión del servidor: 10.4.24-MariaDB
-- Versión de PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `cuadros_c`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pqrs`
--

CREATE TABLE `pqrs` (
  `id` int(11) NOT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `apellido` varchar(45) DEFAULT NULL,
  `correo` varchar(45) DEFAULT NULL,
  `sexo` varchar(15) DEFAULT NULL,
  `likes` int(11) DEFAULT NULL,
  `descripcion` mediumtext DEFAULT NULL,
  `fecha` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `pqrs`
--

INSERT INTO `pqrs` (`id`, `nombre`, `apellido`, `correo`, `sexo`, `likes`, `descripcion`, `fecha`) VALUES
(1, 'urian', 'sanches', 'sanches@gmail.com', 'Masculino', 1, 'Me gusto la pagina', '2022-11-28 23:22:12'),
(2, 'Brenda', 'parra', 'parra@gmail.com', 'Femenino', 1, 'Me encanto, 10 de 10', '2022-11-28 23:22:25'),
(3, 'Alejandro', 'aux', 'aux@gmail.com', 'Masculino', 0, 'Carece de informacion', '2022-11-28 23:23:05'),
(7, 'fdsfs', 'fsdfsd', 'sdfsdf@hotmail.com', 'Masculino', 1, 'fddfbdf', '2023-03-14 00:45:54'),
(8, 'fdsfs', 'fsdfsd', 'sdfsdf@hotmail.com', 'Masculino', 1, 'fddfbdf', '2023-03-14 00:49:42'),
(9, 'fdsfs', 'fsdfsd', 'sdfsdf@hotmail.com', 'Masculino', 1, 'fddfbdf', '2023-03-14 00:50:02'),
(10, 'Diego', 'Maradona', 'Maradona@hmail.com', 'Masculino', 0, 'Me parece chafa esa pagina', '2023-03-14 10:20:33');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `product`
--

CREATE TABLE `product` (
  `pid` int(11) NOT NULL,
  `code` varchar(255) NOT NULL,
  `name` varchar(70) DEFAULT NULL,
  `image` varchar(255) NOT NULL,
  `category` varchar(70) DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `discount` int(11) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `product`
--

INSERT INTO `product` (`pid`, `code`, `name`, `image`, `category`, `price`, `discount`) VALUES
(1, 'EDNALAN01', 'Taberna de Moe', '1.jpg', '30x40cm', 13000, 100),
(2, 'EDNALAN02', 'Leo Messi', '2.jpg', '23x23 cm', 15000, 500),
(3, 'EDNALAN03', 'Insignia shingeki no kyojin', '3.jpg', '30x40 cm', 2000, 1250),
(4, 'EDNALAN04', 'Madara Uchiha', '4.jpg', '40x60 cm', 40000, 50),
(5, 'EDNALAN05', 'Mascota', '5.jpg', '35x25 cm', 21000, 1000),
(6, 'EDNALAN06', 'Atomo', '6.jpg', '50x50 cm', 47000, 7000),
(7, 'EDNALAN07', 'Flores', '7.jpg', '80x55 cm', 55000, 5000),
(8, 'EDNALAN08', 'Rap', '8.jpg', '90x40 cm', 70000, NULL),
(9, 'EDNALAN09', 'God Of War', '9.jpg', '90x60 cm', 73000, NULL),
(10, 'EDNALAN010', 'Naruto', '10.jpg', '100x70 cm', 98000, NULL),
(11, 'EDNALAN011', 'Ajedrez', '11.jpg', '110x75 cm', 117000, NULL),
(12, 'EDNALAN012', 'Abstracto', '12.jpg', '95x65 cm', 80000, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

CREATE TABLE `users` (
  `nombre` varchar(100) NOT NULL,
  `correo` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `users`
--

INSERT INTO `users` (`nombre`, `correo`, `password`) VALUES
('camilo', 'gerardobravo@udenar.edu.co', 'sha256$45PSeR5v2c4QpWBJ$86c8b6591a5d58f7536a4e932284dd98382c9afa64e5e453e1e341cd2f95f6af'),
('camilo', 'camilomp100@hotmail.com', 'sha256$ETkks9B9wGF6K1wi$597794eb8c67ee51183facc70353fdf8475e2302222aa210d49f16800d1e9722'),
('Eduardo lopez', 'Eduardolopez@gmail.com', 'sha256$CDJ25FZioE7dBjH7$31998135128e087ffe5571790bf0e5ac1d0e53fee532629aa0c1822d6fb10c53'),
('Vicente insuaty', 'Vicenteinsuaty@gmail.com', 'sha256$hZeBmx975dCDvg9j$dd4cf229e125d6db08843966398a22c4d617841ba252fd514d024f487350c780'),
('dsdsdss', 'dssdds@hotmail.com', 'sha256$VKk7EoGOmrFciPV5$cf5626f20387ecab0ca515389e1438852a8edf9d8e54dd928c272e75ea281e62');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `pqrs`
--
ALTER TABLE `pqrs`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`pid`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `pqrs`
--
ALTER TABLE `pqrs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `product`
--
ALTER TABLE `product`
  MODIFY `pid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=250;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
