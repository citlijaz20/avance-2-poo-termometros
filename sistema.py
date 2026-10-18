# avance-2-poo-termometros
 "Sistema biomédico con herencia y encapsulamiento - Citlalli Flores".
# ==========================================
# SISTEMA DE GESTIÓN DE EQUIPOS BIOMÉDICOS
# Avance 2: Herencia, Encapsulamiento y Polimorfismo
# Alumna: Citlalli Jazmín Flores Sánchez
# ==========================================

# --- CLASE BASE (Superclase) ---
class TermometroDigital:
    def __init__(self, marca, ubicacion, temperatura, encendido, bateria):
        self.marca = marca
        self.ubicacion = ubicacion
        self.temperatura = temperatura
        self.encendido = encendido
        self.__bateria = bateria  # Atributo privado (Encapsulamiento)

    # Getter para consultar el atributo privado de forma segura
    def get_bateria(self):
        return self.__bateria

    # Setter para modificar el atributo privado con validación de rango (0% a 100%)
    def set_bateria(self, nueva_bateria):
        if 0 <= nueva_bateria <= 100:
            self.__bateria = nueva_bateria
            print(f"Batería actualizada exitosamente a {self.__bateria}%.")
        else:
            print(f"Error: La batería debe estar entre 0 y 100%. No se pudo asignar {nueva_bateria}%.")

    # Método 1: Encender el termómetro
    def encender(self):
        self.encendido = True
        return f"El termómetro {self.marca} ubicado en {self.ubicacion} está encendido y listo."

    # Método 2: Cambiar de ubicación (Demuestra independencia de instancias)
    def cambiar_ubicacion(self, nueva_ubicacion):
        self.ubicacion = nueva_ubicacion
        return f"El termómetro fue trasladado a: {self.ubicacion}."

    # Método 3 (Polimorfismo / Método base): Mostrar información general
    def mostrar_info(self):
        estado = "Encendido" if self.encendido else "Apagado"
        return f"Termómetro Estándar | Marca: {self.marca} | Lugar: {self.ubicacion} | Temperatura: {self.temperatura}°C | Batería: {self.get_bateria()}% | Estado: {estado}"


# --- CLASE DERIVADA (Subclase) ---
class TermometroInfrarrojo(TermometroDigital):
    def __init__(self, marca, ubicacion, temperatura, encendido, bateria, distancia_maxima, modo_superficie=False):
        # Usamos super() para heredar y reutilizar los atributos de la superclase
        super().__init__(marca, ubicacion, temperatura, encendido, bateria)
        self.distancia_maxima = distancia_maxima      # Atributo nuevo 1 de la subclase
        self._modo_superficie = modo_superficie       # Atributo nuevo 2 (Protegido con un guion bajo)

    # Método propio de la subclase
    def escanear_distancia(self):
        return f"Escaneando a distancia segura de hasta {self.distancia_maxima} cm con el dispositivo infrarrojo {self.marca}."

    # Método 4 (Sobrescritura / Override - Polimorfismo)
    def mostrar_info(self):
        # Reutilizamos parte de la lógica extendiendo el comportamiento con f-strings detallados
        estado = "Encendido" if self.encendido else "Apagado"
        modo = "Superficie" if self._modo_superficie else "Clínico/Corporal"
        return f"Termómetro Infrarrojo [AVANZADO] | Marca: {self.marca} | Lugar: {self.ubicacion} | Temp: {self.temperatura}°C | Batería: {self.get_bateria()}% | Distancia Máx: {self.distancia_maxima}cm | Modo: {modo} | Estado: {estado}"


# ==========================================
# PRUEBAS E INSTANCIACIÓN DE OBJETOS
# ==========================================

print("=== 1. PRUEBA DE LA CLASE BASE ===")
termom_base = TermometroDigital("Omron", "Piso 1 - Sala A", 36.5, False, 80)
print(termom_base.encender())
print(termom_base.mostrar_info())

print("\n" + "-" * 50 + "\n")

print("=== 2. PRUEBAS DE LA SUBCLASE (HERENCIA Y POLIMORFISMO) ===")
# Instanciamos 2 objetos de la subclase
infra1 = TermometroInfrarrojo("Braun", "Urgencias", 38.2, True, 95, 15, False)
infra2 = TermometroInfrarrojo("Beurer", "Consultorio 3", 37.0, True, 45, 10, True)

# Demostración del método sobrescrito (Polimorfismo)
print(infra1.mostrar_info())
print(infra1.escanear_distancia())

print("\n" + infra2.mostrar_info())
print(infra2.escanear_distancia())

print("\n" + "-" * 50 + "\n")

print("=== 3. DEMOSTRACIÓN DE ENCAPSULAMIENTO Y VALIDACIÓN ===")
print(f"Nivel de batería actual (consultado por Getter): {infra1.get_bateria()}%")
# Intentamos asignar un valor inválido (rompiendo la regla de negocio)
infra1.set_bateria(120) 
# Asignamos un valor válido
infra1.set_bateria(65)
print(f"Nuevo nivel de batería verificado: {infra1.get_bateria()}%")

print("\n" + "-" * 50 + "\n")

print("=== 4. INDEPENDENCIA DE DATOS ENTRE INSTANCIAS (SELF) ===")
print("Antes del traslado:")
print(f" - {infra2.marca}: {infra2.ubicacion}")
# Modificamos la ubicación solo en infra2
print(infra2.cambiar_ubicacion("Piso 2 - Sala B"))
print("Después del traslado (verificando que infra1 no se altera):")
print(f" - infra1 mantiene su ubicación: {infra1.ubicacion}")
print(f" - infra2 actualizó su ubicación: {infra2.ubicacion}")
