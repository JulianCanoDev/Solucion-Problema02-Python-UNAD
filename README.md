# Solución Problema 02 - Gestión de Precios de Menú (Restaurante)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)

Programa en Python para la gestión de precios y promociones en un menú de restaurante. Corresponde a la **Fase 5** del curso **Fundamentos de Programación (213022)** de la **UNAD**.

## Descripción

El sistema administra una matriz de productos del menú (nombre, categoría y precio base) y aplica un **15 % de descuento** sobre aquellos que pertenezcan a una categoría objetivo y superen un umbral de precio definido. Los resultados se presentan en un reporte tabular formateado en consola.

### Funcionalidades

- Definición de al menos 6 productos con precios base en pesos colombianos.
- Configuración parametrizada de categoría promocional y umbral de precio.
- Cálculo automático de precio final con descuento del 15 % cuando se cumplen las condiciones.
- Reporte de salida alineado con formato monetario.

## Requisitos

- Python 3.10 o superior.
- No requiere librerías externas (solo *Standard Library*).

## Uso

```bash
python problema_2.py
```

Ejemplo de salida:

```
==================================================================
         SISTEMA DE GESTIÓN DE PRECIOS Y PROMOCIONES - RESTAURANTE
==================================================================
 -> Categoría sujeta a promoción: Comida Rápida
 -> Umbral de precio base calificado: $12,000.00
==================================================================
Producto                  Categoría          Precio Base Precio Final
------------------------------------------------------------------
Hamburguesa Clásica       Comida Rápida       $18,000.00   $15,300.00
Papas Fritas Medianas     Acompañamientos      $7,000.00    $7,000.00
Pizza Especial            Comida Rápida       $26,000.00   $22,100.00
Lasaña Boloñesa           Pastas              $22,000.00   $22,000.00
Jugo Natural de Lulo      Bebidas              $6,500.00    $6,500.00
Perro Caliente Especial   Comida Rápida       $11,500.00   $11,500.00
==================================================================
```

## Estructura del proyecto

```
├── problema_2.py      # Código fuente principal
├── requirements.txt   # Dependencias (ninguna externa)
└── README.md          # Este archivo
```

## Autor

**Julian Andres Cano Orozco**  
Ingeniería Multimedia - UNAD  
Curso: Fundamentos de Programación (213022) - Grupo 213022B_2201