# ========================================
# BLOQUE 1 - EJERCICIOS PARA ESTUDIANTES
# Completa los ejercicios marcados con ✍️ TÚ HACES
# ========================================

# ========================================
# TEMA 1.1: VARIABLES Y TIPOS DE DATOS
# ========================================

print("="*50)
print("TEMA 1.1: VARIABLES Y TIPOS DE DATOS")
print("="*50)

# ✍️ TÚ HACES - EJERCICIO 1
print("\n✍️ EJERCICIO 1 - Crear tu perfil gamer")
print("Crea variables para tu personaje de videojuego favorito")

# TODO: Crea las siguientes variables:
# - nombre_personaje (string)
# - nivel (int)
# - vida_actual (int)
# - vida_maxima (int)
# - ataque (int)
# - defensa (int)
# - nombre_juego (string)
# - es_main (boolean)

# Escribe tu código aquí:




# TODO: Imprime toda la información de forma bonita
# Usa f-strings y emojis si quieres
print("="*40)
print(f"🎮 PERFIL DE ???")
print("="*40)
# Continúa aquí...




# ========================================
# TEMA 1.2: LISTAS Y OPERACIONES BÁSICAS
# ========================================

print("\n\n" + "="*50)
print("TEMA 1.2: LISTAS")
print("="*50)

# ✍️ TÚ HACES - EJERCICIO 2
print("\n✍️ EJERCICIO 2 - Sistema de tareas")

# TODO: 1. Crea una lista vacía llamada 'tareas'
tareas = []

# TODO: 2. Agrega 5 tareas que tengas que hacer
# Usa tareas.append("nombre de la tarea")




# TODO: 3. Imprime cuántas tareas tienes
print(f"📝 Tienes ??? tareas pendientes")

# TODO: 4. Imprime cada tarea con un número
# Pista: usa enumerate(tareas, 1)
print("\nTareas:")
# Tu código aquí:




# TODO: 5. Elimina la primera tarea (ya la completaste)
# Pista: usa tareas.pop(0)



# TODO: 6. Imprime las tareas restantes
print(f"\nTareas restantes (???):")
# Tu código aquí:




# ========================================
# TEMA 1.3: DICCIONARIOS
# ========================================

print("\n\n" + "="*50)
print("TEMA 1.3: DICCIONARIOS")
print("="*50)

# ✍️ TÚ HACES - EJERCICIO 3
print("\n✍️ EJERCICIO 3 - Menú de restaurante")

# TODO: 1. Crea un diccionario 'menu' con 5 platillos y sus precios
# Ejemplo: menu = {"Pizza": 120, ...}
menu = {
    # Agrega aquí tus platillos
}

# TODO: 2. Imprime todos los platillos con sus precios
print("\n🍽️  MENÚ DEL RESTAURANTE:")
print("="*30)
# Tu código aquí (usa for platillo, precio in menu.items():)




# TODO: 3. Agrega 2 platillos nuevos
# Usa menu["Nombre"] = precio



# TODO: 4. Cambia el precio de uno de tus platillos originales



# TODO: 5. Calcula el precio total si pidieras todo
# Pista: usa sum(menu.values())
total = 0  # Reemplaza esto

print(f"\n💵 Precio total del menú: ${total:.2f}")

# TODO: 6. Imprime el platillo más caro
# Pista: usa max(menu.items(), key=lambda x: x[1])
# mas_caro = ?

print(f"👑 Platillo más caro: ??? ($???)")

# ========================================
# TEMA 1.4: CONDICIONALES
# ========================================

print("\n\n" + "="*50)
print("TEMA 1.4: CONDICIONALES")
print("="*50)

# ✍️ TÚ HACES - EJERCICIO 4
print("\n✍️ EJERCICIO 4 - Sistema de batalla")

# TODO: Crea estas variables con valores que tú quieras
personaje_hp = 0  # Cambia este valor
enemigo_hp = 0    # Cambia este valor

print(f"Tu HP: {personaje_hp}")
print(f"HP Enemigo: {enemigo_hp}")
print()

# TODO: Compara los HP y muestra mensajes
# Si tu HP > enemigo HP: "¡Vas ganando!"
# Si son iguales: "Están parejos"
# Si tu HP < enemigo HP: "¡Cuidado! El enemigo es más fuerte"

# Tu código aquí:




# TODO: BONUS - Agrega niveles de advertencia
# Si tu HP < 30: "¡HP CRÍTICO!"
# Si tu HP < 50: "HP bajo"
# Si tu HP >= 50: "HP saludable"

# Tu código aquí:




# ========================================
# 🎯 EJERCICIO INTEGRADOR (OPCIONAL)
# ========================================

print("\n\n" + "="*50)
print("🎯 EJERCICIO INTEGRADOR - Tabla de Clasificación")
print("="*50)

# Se te da esta lista de jugadores
jugadores = [
    {"nombre": "Player1", "puntos": 1500, "nivel": 5},
    {"nombre": "Player2", "puntos": 2300, "nivel": 7},
    {"nombre": "Player3", "puntos": 900, "nivel": 3}
]

# TODO: 1. Agrega tu propio jugador a la lista



# TODO: 2. Recorre la lista e imprime cada jugador
# Formato: "Nombre | Puntos: XXX | Nivel: X"
print("\n🏆 JUGADORES:")
# Tu código aquí:




# TODO: 3. Clasifica cada jugador por puntos:
# >= 2000: "🥇 Oro"
# >= 1000: "🥈 Plata"  
# < 1000: "🥉 Bronce"
# (Repite el loop pero ahora con la clasificación)




# TODO: 4. Calcula e imprime:
# - Total de puntos de todos los jugadores
# - Nivel promedio
# - Nombre del jugador con más puntos

print("\n📊 ESTADÍSTICAS:")
# Tu código aquí:




print("\n✅ ¡Ejercicios completados!")
print("📝 Recuerda guardar tu archivo")
print("🎉 ¡Buen trabajo!")