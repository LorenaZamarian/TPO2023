-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 06-05-2023 a las 02:22:47
-- Versión del servidor: 5.7.40-log
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `e-commerce`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `bodega`
--

CREATE TABLE `bodega` (
  `ID_Bodega` int(15) NOT NULL,
  `Ubicación` varchar(50) NOT NULL,
  `Descripcion` varchar(100) NOT NULL,
  `Imagen` varchar(100) NOT NULL,
  `Nombre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `bodega`
--

INSERT INTO `bodega` (`ID_Bodega`, `Ubicación`, `Descripcion`, `Imagen`, `Nombre`) VALUES
(1, 'Luján de Cuyo, Mendoza', '\r\n', '', 'Catena Zapata'),
(2, 'Tunuyán, Luján y Maipú, Mendoza', '', '', 'Luigi Bosca'),
(3, 'San Carlos, Mendoza', '', '', 'Zuccardi'),
(4, 'Tupungato, Mendoza', '', '', 'Salentein');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalle_venta`
--

CREATE TABLE `detalle_venta` (
  `ID_DetVenta` int(11) NOT NULL,
  `Cantidad` int(10) NOT NULL,
  `Precio_Venta` decimal(10,0) NOT NULL,
  `Id_de_ventas` int(11) NOT NULL,
  `Id_de_vinos` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `personas`
--

CREATE TABLE `personas` (
  `ID_Persona` int(10) NOT NULL,
  `Nombre` text NOT NULL,
  `Apellido` text NOT NULL,
  `DNI` int(20) NOT NULL,
  `E-mail` varchar(30) NOT NULL,
  `Teléfono` int(25) NOT NULL,
  `Dirección` varchar(50) NOT NULL,
  `Id_de_vinos` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `ID_Usuario` int(11) NOT NULL,
  `Nombre` int(11) NOT NULL,
  `E-mail` varchar(20) NOT NULL,
  `Password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `varietal`
--

CREATE TABLE `varietal` (
  `ID_Varietal` int(10) NOT NULL,
  `Nombre` varchar(50) NOT NULL,
  `Descripcion` varchar(500) NOT NULL,
  `imagen` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `varietal`
--

INSERT INTO `varietal` (`ID_Varietal`, `Nombre`, `Descripcion`, `imagen`) VALUES
(1, 'Blend', 'Son vinos en los que para su creación se utilizan diferentes variedades de uva, sin límite alguno.\r\nLa combinación vendrá dada por la cantidad y variedades que el enólogo crea prudente para concretar el vino. Son vinos que no buscan el liderazgo de una cepa sobre las demás sino que todas aporten su identidad para lograr un resultado determinado. ', ''),
(2, 'Chardonnay', ' Cuando se producen vinos de crianza a partir de la Chardonnay, estos se benefician del paso por barrica, lo que favorece la concentración de los sabores y les aporta un punto extra de cuerpo. En general, son vinos dulzones, de acidez moderada y cierto punto de untuosidad, con un grado alcohólico moderado.', ''),
(3, 'Malbec', 'La uva Malbec es una variedad considerada mejorante por lo que es muy buena para la elaboración de vinos, produce mostos de elevada intensidad de color, muy tánicos, de potencial aromático medio, pero con aromas muy peculiares y agradables. \r\nEn boca los vinos de Malbec son cálidos, suaves y de taninos dulce poco agresivos. Cuando se realiza crianza en madera, adquiere tonos a café, vainilla y chocolate.', ''),
(4, 'Rosé', ' Un rosado es, básicamente, un vino tinto con poca maceración. Proviene de uvas negras (o mezcla de uvas negras y blancas) y la tonalidad del rosado dependerá del tiempo de maceración: a menor tiempo, color más tenue y  blanquecino.\r\nLa calidad de un rosado es independiente de su color más o menos tenue.\r\nSon  vinos suaves en su mayoría, de consumo fresco y sin excesivo cuerpo. Por eso son ideales para la época primaveral.', ''),
(5, 'Sauvignon Blanc', 'La uva Sauvignon Blanc es una variedad de vinos blancos, de cuerpo ligero, elegante y de frescura particular. Es muy común presentar notas de cítricos y hortalizas, como espárragos y pepinos. Pero es posible encontrar ejemplares con aromas de frutas tropicales, como maracuyá, piña y kiwi. Ya en el paladar, la uva muestra buena acidez, repite las notas herbáceas y final refrescante.', ''),
(6, 'Torrontés', 'El Torrontés es un vino amarillo claro que ocasionalmente desarrolla matices dorados y verdes. Se caracteriza por su aroma a flores como la rosa, el jazmín y el geranio, siendo ocasional la aparición de efluvios especiados. Si bien sus aromas anticipan un vino dulce, su sabor revela una fresca acidez.', ''),
(7, 'Espumante', 'Un buen espumante, una vez servido, presenta una espuma persistente, burbujas pequeñas y continuas desde el fondo hacia la superficie, formando una hilera muy derecha y veloz. La temperatura de servicio recomendada es 6° a 9°C.', '');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ventas`
--

CREATE TABLE `ventas` (
  `ID_Ventas` int(200) NOT NULL,
  `Tipo_comprobante` varchar(10) NOT NULL,
  `Num_comprobante` int(20) NOT NULL,
  `Fecha` date NOT NULL,
  `Total_Venta` decimal(10,0) NOT NULL,
  `Id_de_usuario` int(11) NOT NULL,
  `Id_de_Persona` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vinos`
--

CREATE TABLE `vinos` (
  `ID_Vino` int(10) NOT NULL,
  `Nombre` varchar(50) NOT NULL,
  `Variedad` varchar(50) NOT NULL,
  `Cantidad` int(4) NOT NULL,
  `Imagen` varchar(100) NOT NULL,
  `Id_de_Bodega` int(11) NOT NULL,
  `Id_de_varietal` int(10) NOT NULL,
  `Bodega` varchar(50) NOT NULL,
  `Precio` decimal(10,0) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `vinos`
--

INSERT INTO `vinos` (`ID_Vino`, `Nombre`, `Variedad`, `Cantidad`, `Imagen`, `Id_de_Bodega`, `Id_de_varietal`, `Bodega`, `Precio`) VALUES
(1, 'D.V. Catena - Vino Tinto Histórico 2019', 'Blend', 100, '', 1, 0, '', 0),
(2, 'White Bones', 'Chardonnay', 100, '', 1, 0, '', 0),
(3, 'River', 'Malbec', 100, '', 1, 0, '', 0),
(4, 'Saint Felicien', 'Rosé', 100, '', 1, 0, '', 0),
(5, 'Saint Felicien', 'Sauvignon Blanc', 100, '', 1, 0, '', 0),
(6, '------', 'Torrontés', 0, '', 1, 0, '', 0),
(7, 'Blanc de Blancs', 'Espumante', 100, '', 1, 0, '', 0);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `bodega`
--
ALTER TABLE `bodega`
  ADD PRIMARY KEY (`ID_Bodega`);

--
-- Indices de la tabla `detalle_venta`
--
ALTER TABLE `detalle_venta`
  ADD PRIMARY KEY (`ID_DetVenta`),
  ADD KEY `FK_Ventas` (`Id_de_ventas`),
  ADD KEY `FK_Vinos` (`Id_de_vinos`);

--
-- Indices de la tabla `personas`
--
ALTER TABLE `personas`
  ADD PRIMARY KEY (`ID_Persona`),
  ADD KEY `FK_Vinos` (`Id_de_vinos`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`ID_Usuario`);

--
-- Indices de la tabla `varietal`
--
ALTER TABLE `varietal`
  ADD PRIMARY KEY (`ID_Varietal`);

--
-- Indices de la tabla `ventas`
--
ALTER TABLE `ventas`
  ADD PRIMARY KEY (`ID_Ventas`),
  ADD KEY `FK_Usuario` (`Id_de_usuario`),
  ADD KEY `FK_Persona` (`Id_de_Persona`);

--
-- Indices de la tabla `vinos`
--
ALTER TABLE `vinos`
  ADD PRIMARY KEY (`ID_Vino`),
  ADD KEY `FK_Bodega` (`Id_de_Bodega`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `ID_Usuario` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `detalle_venta`
--
ALTER TABLE `detalle_venta`
  ADD CONSTRAINT `detalle_venta_ibfk_1` FOREIGN KEY (`Id_de_vinos`) REFERENCES `vinos` (`ID_Vino`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `detalle_venta_ibfk_2` FOREIGN KEY (`Id_de_ventas`) REFERENCES `ventas` (`ID_Ventas`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `personas`
--
ALTER TABLE `personas`
  ADD CONSTRAINT `personas_ibfk_1` FOREIGN KEY (`Id_de_vinos`) REFERENCES `vinos` (`ID_Vino`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `ventas`
--
ALTER TABLE `ventas`
  ADD CONSTRAINT `ventas_ibfk_1` FOREIGN KEY (`Id_de_usuario`) REFERENCES `usuario` (`ID_Usuario`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `ventas_ibfk_2` FOREIGN KEY (`Id_de_Persona`) REFERENCES `personas` (`ID_Persona`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `vinos`
--
ALTER TABLE `vinos`
  ADD CONSTRAINT `vinos_ibfk_1` FOREIGN KEY (`Id_de_Bodega`) REFERENCES `bodega` (`ID_Bodega`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
