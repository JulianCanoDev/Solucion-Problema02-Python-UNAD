# ========================================================================
# Nombre Completo: Julian Andres Cano Orozco [cite: 173]
# Programa Académico: Ingeniería Multimedia [cite: 181]
# Número de Grupo: 213022B_2201 [cite: 176]
# Código de Curso: 213022 [cite: 110]
# Fuente: Autoría propia [cite: 212]
# Problema Seleccionado: Problema 2 (Gestión de Precios de Menú) [cite: 112, 126]
# ========================================================================

def calcular_precio_final(producto, categoria_objetivo, umbral_precio):
    """
    Módulo (función) encargado de calcular el precio final de un producto.
    Aplica un 15% de descuento si pertenece a la categoría objetivo 
    y supera el umbral de precio establecido.
    """
    nombre = producto[0]
    categoria = producto[1]
    precio_base = producto[2]
    
    # Lógica de negocio: Validar condiciones de la promoción [cite: 132, 133]
    if categoria.lower() == categoria_objetivo.lower() and precio_base > umbral_precio:
        descuento = precio_base * 0.15
        precio_final = precio_base - descuento
    else:
        precio_final = precio_base [cite: 134]
        
    return precio_final


def main():
    """
    Función principal que orquesta el flujo de ejecución del programa[cite: 215].
    Definición de la matriz de datos y generación del reporte de salida[cite: 130, 135].
    """
    print("==================================================================")
    print("         SISTEMA DE GESTIÓN DE PRECIOS Y PROMOCIONES - RESTAURANTE")
    print("==================================================================")
    
    # Matriz inicialización: al menos 6 productos [cite: 116, 130]
    # Estructura: [Nombre del Producto, Categoría, Precio Base] 
    menu_productos = [
        ["Hamburguesa Clásica", "Comida Rápida", 18000],
        ["Papas Fritas Medianas", "Acompañamientos", 7000],
        ["Pizza Especial", "Comida Rápida", 26000],
        ["Lasaña Boloñesa", "Pastas", 22000],
        ["Jugo Natural de Lulo", "Bebidas", 6500],
        ["Perro Caliente Especial", "Comida Rápida", 11500]
    ]
    
    # Definición de variables de control para la promoción 
    categoria_objetivo = "Comida Rápida"
    umbral_precio_base = 12000
    
    # Mostrar parámetros de la auditoría de precios
    print(f" -> Categoría sujeta a promoción: {categoria_objetivo} ")
    print(f" -> Umbral de precio base calificado: ${umbral_precio_base:,.2f} ")
    print("==================================================================")
    
    # Encabezados del reporte de salida 
    print(f"{'Producto':<24} {'Categoría':<18} {'Precio Base':>10} {'Precio Final':>11}")
    print("-" * 66)
    
    # Iteración de la matriz para procesar y presentar la información 
    for producto in menu_productos:
        nombre_prod = producto[0]
        cat_prod = producto[1]
        base_prod = producto[2]
        
        # Llamado al módulo de cálculo parametrizado 
        precio_final_prod = calcular_precio_final(producto, categoria_objetivo, umbral_precio_base)
        
        # Impresión formateada con alineación limpia 
        print(f"{nombre_prod:<24} {cat_prod:<18} ${base_prod:>9,.2f} ${precio_final_prod:>10,.2f}")
        
    print("==================================================================")


if __name__ == "__main__":
    main() [cite: 243, 244]