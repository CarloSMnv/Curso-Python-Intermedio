# ========================================
# BLOQUE 2 - EJERCICIOS PARA ESTUDIANTES
# Completa los ejercicios marcados con ✍️ TÚ HACES
# ========================================

import json
import requests

# ========================================
# TEMA 2.1: CICLOS FOR
# ========================================

print("="*50)
print("TEMA 2.1: CICLOS FOR")
print("="*50)

# ✍️ TÚ HACES - EJERCICIO 1
print("\n✍️ EJERCICIO 1 - Análisis de ventas")

ventas = [1500, 2300, 1800, 3200, 1900, 2800, 2100]

# TODO: 1. Imprime cada venta con su número de día
print("Ventas de la semana:")
# Usa: for i, venta in enumerate(ventas, 1):
# Tu código aquí:




# TODO: 2. Calcula el total de ventas
# Pista: usa sum(ventas)
total = 0  # Reemplaza esto

print(f"\n💰 Total de ventas: ${total:,}")

# TODO: 3. Calcula el promedio
# promedio = total / len(ventas)
promedio = 0  # Reemplaza esto

print(f"📊 Promedio diario: ${promedio:,.2f}")

# TODO: 4. Encuentra la venta más alta
# Pista: usa max(ventas)
venta_maxima = 0  # Reemplaza esto

print(f"🏆 Venta más alta: ${venta_maxima:,}")

# TODO: 5. Cuenta cuántas ventas fueron > $2000
# Usa un contador y un if dentro del for
contador = 0
# Tu código aquí:




print(f"📈 Días con ventas > $2000: {contador}")

# TODO: BONUS - Imprime qué días específicos fueron > $2000
print("\nDías con ventas mayores a $2000:")
# Tu código aquí:




# ========================================
# TEMA 2.2: FUNCIONES BÁSICAS
# ========================================

print("\n\n" + "="*50)
print("TEMA 2.2: FUNCIONES")
print("="*50)

# ✍️ TÚ HACES - EJERCICIO 2
print("\n✍️ EJERCICIO 2 - Sistema de calificaciones")

# TODO: Crea la función calcular_promedio
# Debe recibir 3 calificaciones y retornar el promedio
def calcular_promedio(calif1, calif2, calif3):
    # Tu código aquí:
    pass  # Reemplaza el pass con tu código


# TODO: Crea la función obtener_letra
# Debe recibir un promedio y retornar la letra correspondiente:
# >= 90: "A"
# >= 80: "B"
# >= 70: "C"
# < 70: "F"
def obtener_letra(promedio):
    # Tu código aquí:
    pass  # Reemplaza el pass con tu código


# TODO: Prueba tus funciones con estas calificaciones
calif1, calif2, calif3 = 85, 92, 78

# Calcula el promedio


# Obtiene la letra


# Imprime el resultado
# print(f"Tu promedio es ??? - Calificación: ???")

# TODO: BONUS - Prueba con más casos
# casos = [(95, 98, 92), (80, 85, 78), (70, 72, 69)]
# Recorre los casos y muestra el promedio y letra de cada uno




# ========================================
# TEMA 2.3: LIST COMPREHENSIONS
# ========================================

print("\n\n" + "="*50)
print("TEMA 2.3: LIST COMPREHENSIONS")
print("="*50)

# ✍️ TÚ HACES - EJERCICIO 3
print("\n✍️ EJERCICIO 3 - Filtros de productos")

productos = [
    {"nombre": "Laptop", "precio": 15000},
    {"nombre": "Mouse", "precio": 350},
    {"nombre": "Teclado", "precio": 800},
    {"nombre": "Monitor", "precio": 4500},
    {"nombre": "USB", "precio": 150}
]

# TODO: 1. Crea una lista solo con los nombres de productos
# nombres = [p["nombre"] for p in productos]
nombres_productos = []  # Reemplaza con list comprehension

print(f"1. Nombres: {nombres_productos}")

# TODO: 2. Crea una lista con nombres de productos caros (precio > $1000)
# productos_caros = [p["nombre"] for p in productos if ...]
productos_caros = []  # Reemplaza con list comprehension

print(f"2. Productos caros: {productos_caros}")

# TODO: 3. Crea una lista con todos los precios con 20% de descuento
# precios_descuento = [p["precio"] * 0.8 for p in productos]
precios_descuento = []  # Reemplaza con list comprehension

print(f"3. Precios con descuento: {precios_descuento}")

# TODO: 4. Lista de nombres de productos baratos (precio < $500)
productos_baratos = []  # Reemplaza con list comprehension

print(f"4. Productos baratos: {productos_baratos}")

# TODO: BONUS - Dict comprehension
# Crea un diccionario: {nombre: precio_con_descuento}
# productos_descuento = {p["nombre"]: p["precio"] * 0.8 for p in productos}
productos_descuento = {}  # Reemplaza con dict comprehension

print(f"\nBONUS - Diccionario con descuentos:")
# for nombre, precio in productos_descuento.items():
#     print(f"  {nombre}: ${precio:.2f}")

# ========================================
# TEMA 2.4: MANEJO DE ARCHIVOS JSON
# ========================================

print("\n\n" + "="*50)
print("TEMA 2.4: ARCHIVOS JSON")
print("="*50)

# ✍️ TÚ HACES - EJERCICIO 4
print("\n✍️ EJERCICIO 4 - Registro de jugadores")

# TODO: 1. Crea esta lista de jugadores
jugadores = [
    {"nombre": "Player1", "puntos": 1500, "nivel": 5},
    {"nombre": "Player2", "puntos": 2300, "nivel": 7},
    {"nombre": "Player3", "puntos": 1200, "nivel": 4}
]

# TODO: 2. Guarda la lista en un archivo "jugadores.json"
# Pista:
# with open("jugadores.json", "w", encoding="utf-8") as f:
#     json.dump(jugadores, f, indent=2)

# Tu código aquí:




# TODO: 3. Lee el archivo y muestra todos los jugadores
# Pista:
# with open("jugadores.json", "r", encoding="utf-8") as f:
#     jugadores_leidos = json.load(f)

print("\n📊 Información de jugadores:")
# Tu código aquí:




# TODO: 4. Encuentra y muestra el jugador con más puntos
# Pista: usa max(jugadores_leidos, key=lambda x: x["puntos"])

# mejor = ?
# print(f"🏆 Mejor jugador: {mejor['nombre']}")

# TODO: 5. Calcula y muestra el promedio de nivel
# Pista: sum(j["nivel"] for j in jugadores_leidos) / len(jugadores_leidos)

# promedio_nivel = ?
# print(f"📈 Nivel promedio: {promedio_nivel:.1f}")

# TODO: 6. Agrega un nuevo jugador y guarda el archivo de nuevo
nuevo_jugador = {"nombre": "TuNombre", "puntos": 1800, "nivel": 6}

# Agregar a la lista


# Guardar de nuevo en el archivo


print(f"✅ Jugador {nuevo_jugador['nombre']} agregado")

# TODO: BONUS - Crea una función que actualice los puntos de un jugador
def actualizar_puntos(nombre, puntos_nuevos):
    """Actualiza los puntos de un jugador en el archivo"""
    # 1. Lee el archivo
    # 2. Busca el jugador por nombre
    # 3. Actualiza sus puntos
    # 4. Guarda el archivo
    pass  # Reemplaza con tu código

# Prueba tu función:
# actualizar_puntos("Player1", 2000)

# ========================================
# TEMA 2.5: TRABAJO CON APIs
# ========================================

print("\n\n" + "="*50)
print("TEMA 2.5: APIs")
print("="*50)

# ✍️ TÚ HACES - EJERCICIO 5
print("\n✍️ EJERCICIO 5 - Comparador de Pokémon")

# TODO: Crea una función que compare dos Pokémon
def comparar_pokemon(nombre1, nombre2):
    """
    Compara dos Pokémon usando la API de PokéAPI
    URL base: https://pokeapi.co/api/v2/pokemon/{nombre}
    """
    # TODO: 1. Construye las URLs para ambos Pokémon
    url1 = f"https://pokeapi.co/api/v2/pokemon/{nombre1.lower()}"
    url2 = # Completa aquí
    
    try:
        # TODO: 2. Haz las peticiones a la API
        resp1 = requests.get(url1, timeout=10)
        resp2 = # Completa aquí
        
        # TODO: 3. Verifica que ambas respuestas sean exitosas
        if resp1.status_code != 200 or resp2.status_code != 200:
            print("❌ Uno o ambos Pokémon no fueron encontrados")
            return
        
        # TODO: 4. Convierte las respuestas a JSON
        poke1 = resp1.json()
        poke2 = # Completa aquí
        
        # TODO: 5. Extrae la información necesaria
        # Pistas:
        # - Nombre: poke1['name']
        # - HP: poke1['stats'][0]['base_stat']
        # - Ataque: poke1['stats'][1]['base_stat']
        # - Peso: poke1['weight'] / 10 (para kg)
        
        nombre_1 = 
        nombre_2 = 
        
        hp1 = 
        hp2 = 
        
        ataque1 = 
        ataque2 = 
        
        peso1 = 
        peso2 = 
        
        # TODO: 6. Muestra la comparación
        print(f"\n⚔️  {nombre_1.upper()} VS {nombre_2.upper()}")
        print("="*50)
        
        # Compara HP
        if hp1 > hp2:
            print(f"❤️  HP: {nombre_1} gana ({hp1} vs {hp2})")
        # Completa las demás comparaciones...
        
        
        # Compara Ataque
        
        
        # Compara Peso
        
        
        # TODO: BONUS - Determina el ganador general
        # Cuenta cuántas categorías ganó cada uno
        
        
    except Exception as e:
        print(f"❌ Error: {e}")

# TODO: Prueba tu función con diferentes Pokémon
# Ejemplos:
# comparar_pokemon("pikachu", "charizard")
# comparar_pokemon("bulbasaur", "squirtle")
# comparar_pokemon("mewtwo", "mew")

# Llama a tu función aquí:




print("\n✅ ¡Ejercicios completados!")
print("📝 Recuerda guardar tu archivo")
print("🎉 ¡Excelente trabajo!")