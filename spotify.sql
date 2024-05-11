-- phpMyAdmin SQL Dump
-- version 3.4.5
-- http://www.phpmyadmin.net
--
-- Servidor: localhost
-- Tiempo de generación: 11-05-2024 a las 16:16:07
-- Versión del servidor: 5.5.16
-- Versión de PHP: 5.3.8

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de datos: `spotify`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `artistas`
--

CREATE TABLE IF NOT EXISTS `artistas` (
  `id_artista` int(100) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  `correo` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id_artista`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=31 ;

--
-- Volcado de datos para la tabla `artistas`
--

INSERT INTO `artistas` (`id_artista`, `nombre`, `correo`) VALUES
(1, 'Michael Jackson', 'michael.jackson@gmail.com'),
(2, 'The Beatles', 'thebeatles@gmail.com'),
(3, 'Queen', 'queen@gmail.com'),
(4, 'Elton John', 'eltonjohn@gmail.com'),
(5, 'Madonna', 'madonna@gmail.com'),
(6, 'Bob Marley', 'bobmarley@gmail.com'),
(7, 'Led Zeppelin', 'ledzeppelin@gmail.com'),
(8, 'Pink Floyd', 'pinkfloyd@gmail.com'),
(9, 'Bad Bunny', 'badbunny@gmail.com'),
(10, 'Prince Royce', 'princeroyce@gmail.com'),
(11, 'The Rolling Stones', 'rollingstones@gmail.com'),
(12, 'Harry Styles', 'harrystyles@gmail.com'),
(13, 'Adele', 'adele@gmail.com'),
(14, 'Beyoncé', 'beyonce@gmail.com'),
(15, 'The Weeknd', 'theweeknd@gmail.com'),
(16, 'Ed Sheeran', 'edsheeran@gmail.com'),
(17, 'Taylor Swift', 'taylorswift@gmail.com'),
(18, 'Eminem', 'eminem@gmail.com'),
(19, 'Kanye West', 'kanyewest@gmail.com'),
(20, 'Drake', 'drake@gmail.com'),
(21, 'Rihanna', 'rihanna@gmail.com'),
(22, 'Coldplay', 'coldplay@gmail.com'),
(23, 'U2', 'u2@gmail.com'),
(24, 'Metallica', 'metallica@gmail.com'),
(25, 'Nirvana', 'nirvana@gmail.com'),
(26, 'Red Hot Chili Peppers', 'redhotchilipeppers@gmail.com'),
(27, 'AC/DC', 'acdc@gmail.com'),
(28, 'Bruno Mars', 'brunomars@gmail.com'),
(29, 'Radiohead', 'radiohead@gmail.com'),
(30, 'Queen', 'queen@gmail.com');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `genero_musical`
--

CREATE TABLE IF NOT EXISTS `genero_musical` (
  `id_genero` int(100) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id_genero`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=51 ;

--
-- Volcado de datos para la tabla `genero_musical`
--

INSERT INTO `genero_musical` (`id_genero`, `nombre`) VALUES
(1, 'Pop'),
(2, 'Rock'),
(3, 'Metal'),
(4, 'Salsa'),
(5, 'Corridos'),
(6, 'Reggaeton'),
(7, 'Rap'),
(8, 'Trap'),
(9, 'Bachata'),
(10, 'Clasica'),
(11, 'Jazz'),
(12, 'Blues'),
(13, 'Funk'),
(14, 'Soul'),
(15, 'R&B'),
(16, 'Reggae'),
(17, 'Folk'),
(18, 'Country'),
(19, 'Bluegrass'),
(20, 'Jazz fusion'),
(21, 'Swing'),
(22, 'Ska'),
(23, 'Punk'),
(24, 'Indie'),
(25, 'Alternative'),
(26, 'Ambient'),
(27, 'Electronic'),
(28, 'Techno'),
(29, 'House'),
(30, 'Drum and Bass'),
(31, 'Dubstep'),
(32, 'Trance'),
(33, 'Breakbeat'),
(34, 'Trip-hop'),
(35, 'Disco'),
(36, 'Hip-hop'),
(37, 'Dancehall'),
(38, 'Calypso'),
(39, 'Soca'),
(40, 'Flamenco'),
(41, 'Mariachi'),
(42, 'Tango'),
(43, 'Samba'),
(44, 'Bossa nova'),
(45, 'Merengue'),
(46, 'Cumbia'),
(47, 'Mambo'),
(48, 'Cha-cha-chá'),
(49, 'Bolero'),
(50, 'Vallenato');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `gustos`
--

CREATE TABLE IF NOT EXISTS `gustos` (
  `id_gustos` int(100) NOT NULL AUTO_INCREMENT,
  `id_genero` int(100) NOT NULL,
  `id_usuario` int(100) NOT NULL,
  PRIMARY KEY (`id_gustos`),
  KEY `id_genero` (`id_genero`),
  KEY `id_usuario` (`id_usuario`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=391 ;

--
-- Volcado de datos para la tabla `gustos`
--

INSERT INTO `gustos` (`id_gustos`, `id_genero`, `id_usuario`) VALUES
(1, 4, 5),
(2, 9, 1),
(3, 6, 1),
(4, 4, 2),
(5, 1, 4),
(6, 2, 4),
(7, 6, 2),
(8, 5, 2),
(9, 1, 2),
(10, 8, 3),
(11, 3, 3),
(12, 6, 3),
(13, 10, 1),
(14, 8, 1),
(15, 2, 3),
(16, 8, 7),
(17, 10, 9),
(18, 1, 10),
(19, 5, 5),
(20, 6, 8),
(21, 4, 9),
(22, 3, 10),
(23, 2, 11),
(24, 3, 7),
(25, 4, 6),
(26, 3, 12),
(27, 9, 5),
(28, 6, 7),
(29, 1, 6),
(30, 6, 6),
(301, 13, 1),
(302, 18, 1),
(303, 20, 1),
(304, 21, 1),
(305, 22, 1),
(306, 12, 2),
(307, 15, 2),
(308, 16, 2),
(309, 17, 2),
(310, 19, 2),
(311, 11, 3),
(312, 14, 3),
(313, 16, 3),
(314, 17, 3),
(315, 18, 3),
(316, 11, 4),
(317, 12, 4),
(318, 15, 4),
(319, 18, 4),
(320, 19, 4),
(321, 12, 5),
(322, 13, 5),
(323, 14, 5),
(324, 15, 5),
(325, 16, 5),
(326, 12, 6),
(327, 13, 6),
(328, 14, 6),
(329, 17, 6),
(330, 20, 6),
(331, 12, 7),
(332, 14, 7),
(333, 15, 7),
(334, 17, 7),
(335, 18, 7),
(336, 11, 8),
(337, 14, 8),
(338, 15, 8),
(339, 17, 8),
(340, 19, 8),
(341, 11, 9),
(342, 12, 9),
(343, 14, 9),
(344, 16, 9),
(345, 17, 9),
(346, 13, 10),
(347, 14, 10),
(348, 15, 10),
(349, 5, 10),
(350, 1, 10),
(351, 13, 11),
(352, 18, 11),
(353, 5, 11),
(354, 21, 11),
(355, 22, 11),
(356, 12, 12),
(357, 15, 12),
(358, 16, 12),
(359, 17, 12),
(360, 19, 12),
(361, 1, 13),
(362, 2, 13),
(363, 5, 13),
(364, 17, 13),
(365, 18, 13),
(366, 11, 14),
(367, 5, 14),
(368, 15, 14),
(369, 9, 14),
(370, 19, 14),
(371, 4, 15),
(372, 13, 15),
(373, 14, 15),
(374, 8, 15),
(375, 9, 15),
(376, 3, 16),
(377, 13, 16),
(378, 14, 16),
(379, 8, 16),
(380, 20, 16),
(381, 8, 17),
(382, 14, 17),
(383, 7, 17),
(384, 17, 17),
(385, 10, 17),
(386, 11, 18),
(387, 3, 18),
(388, 15, 18),
(389, 1, 18),
(390, 5, 18);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE IF NOT EXISTS `usuarios` (
  `id_usuario` int(100) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  `apellido` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  `edad` int(100) NOT NULL,
  `genero` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  `telefono` int(100) NOT NULL,
  `correo` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id_usuario`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=19 ;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id_usuario`, `nombre`, `apellido`, `edad`, `genero`, `telefono`, `correo`) VALUES
(1, 'Daniel', 'Lopez', 19, 'Masculino', 69807939, 'danilepez@gmail.com'),
(2, 'Dorian', 'Ticona', 22, 'Masculino', 76451324, 'dorian@gmail.com'),
(3, 'Camila', 'Bocangel', 20, 'Femenino', 76590897, 'camila@gmail.com'),
(4, 'Pablo', 'Acha', 19, 'Masculino', 67549821, 'pablo@gmail.com'),
(5, 'Jorge', 'Saenz', 21, 'Masculino', 76509876, 'jorgesaenz@gmail.com'),
(6, 'Paul', 'Landaeta', 31, 'Masculino', 75645289, 'paul@gmail.com'),
(7, 'Mazen', 'Abuhamdan', 20, 'Masculino', 67584132, 'mazen@gmail.com'),
(8, 'Camilo', 'Zuleta', 19, 'Masculino', 79584866, 'toto@gmail.com'),
(9, 'Ana', 'Vargas', 25, 'Femenino', 74615212, 'ana@gmail.com'),
(10, 'Isabella', 'Alvarez', 17, 'Femenino', 67586251, 'isabella@gmail.com'),
(11, 'Ernesto', 'Castro', 31, 'Masculino', 69087364, 'castro@gmail.com\r\n'),
(12, 'Ximena', 'Bocangel', 24, 'Femenino', 76541311, 'ximena@gmail.com'),
(13, 'Laura', 'Martinez', 23, 'Femenino', 73214567, 'laura@gmail.com'),
(14, 'Carlos', 'Garcia', 28, 'Masculino', 68745231, 'carlos@gmail.com'),
(15, 'Andrea', 'Lopez', 26, 'Femenino', 71589632, 'andrea@gmail.com'),
(16, 'Alejandro', 'Perez', 30, 'Masculino', 79856412, 'alejandro@gmail.com'),
(17, 'María', 'Gonzalez', 20, 'Femenino', 74589621, 'maria@gmail.com'),
(18, 'Juan', 'Diaz', 25, 'Masculino', 76549871, 'juan@gmail.com');

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `gustos`
--
ALTER TABLE `gustos`
  ADD CONSTRAINT `gustos_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`),
  ADD CONSTRAINT `gustos_ibfk_2` FOREIGN KEY (`id_genero`) REFERENCES `genero_musical` (`id_genero`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
