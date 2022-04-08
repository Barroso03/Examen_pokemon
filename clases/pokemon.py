#clase pokemon con get y set
class Pokemon: 
    def __init__(self, nombre, tipo, ataque, defensa, vida): 
        self.nombre = nombre 
        self.tipo = tipo 
        self.ataque = ataque 
        self.defensa = defensa 
        self.vida = vida
#funcion get y set ID del Pokémon. Número entero y único que identifica a la criatura Pokémon.
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
#funcion get y set nombre del Pokémon. Cadena de caracteres que representa el nombre del Pokémon.
    def get_nombre(self):
        return self.nombre
    def set_nombre(self, nombre):
        self.nombre = nombre
#funcion get y set tipo del Pokémon. Cadena de caracteres que representa el tipo del Pokémon.
    def get_tipo(self):
        return self.tipo
    def set_tipo(self, tipo):
        self.tipo = tipo
#funcion get y set ataque del Pokémon. Número entero que representa el ataque del Pokémon.
    def get_ataque(self):
        return self.ataque
    def set_ataque(self, ataque):
        self.ataque = ataque
#funcion get y set defensa del Pokémon. Número entero que representa la defensa del Pokémon.
    def get_defensa(self):
        return self.defensa
    def set_defensa(self, defensa):
        self.defensa = defensa
#funcion get y set vida del Pokémon. Número entero que representa la vida del Pokémon.
    def get_vida(self):
        return self.vida
    def set_vida(self, vida):
        self.vida = vida
#funcion get y set nivel del Pokémon. Número entero que representa el nivel del Pokémon.
    def get_nivel(self):
        return self.nivel
    def set_nivel(self, nivel):
        self.nivel = nivel
#funcion get y set experiencia del Pokémon. Número entero que representa la experiencia del Pokémon.
    def get_experiencia(self):
        return self.experiencia
    def set_experiencia(self, experiencia):
        self.experiencia = experiencia
#funcion get y set evolucion del Pokémon. Cadena de caracteres que representa la evolucion del Pokémon.
    def get_evolucion(self):
        return self.evolucion
    def set_evolucion(self, evolucion):
        self.evolucion = evolucion




    def fight_attack(self, pokemon_to_attack):
        if self.tipo == "Agua":
            if pokemon_to_attack.tipo == "Agua":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 2)
            elif pokemon_to_attack.tipo == "Fuego":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Electrico":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Planta":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Fantasma":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Roca":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Volador":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Psiquico":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Lucha":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Bicho":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Acero":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Hielo":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Dragon":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Insecto":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
        elif self.tipo == "Fuego":
            if pokemon_to_attack.tipo == "Agua":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Fuego":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 2)
            elif pokemon_to_attack.tipo == "Electrico":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Planta":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Fantasma":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Roca":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Volador":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Psiquico":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Lucha":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Bicho":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Acero":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Hielo":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Dragon":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Insecto":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
        elif self.tipo == "Electrico":
            if pokemon_to_attack.tipo == "Agua":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Fuego":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Electrico":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 2)
            elif pokemon_to_attack.tipo == "Planta":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Fantasma":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Roca":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Volador":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Psiquico":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Lucha":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Bicho":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Acero":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Hielo":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Dragon":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Insecto":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
        elif self.tipo == "Planta":
            if pokemon_to_attack.tipo == "Agua":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Fuego":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Electrico":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Planta":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 2)
            elif pokemon_to_attack.tipo == "Fantasma":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Roca":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Volador":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Psiquico":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Lucha":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Bicho":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Acero":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Hielo":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Dragon":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Insecto":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
        elif self.tipo == "Fantasma":
            if pokemon_to_attack.tipo == "Agua":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Fuego":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Electrico":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Planta":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Fantasma":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 2)
            elif pokemon_to_attack.tipo == "Roca":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Volador":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Psiquico":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Lucha":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Bicho":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Acero":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Hielo":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Dragon":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Insecto":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
        elif self.tipo == "Roca":
            if pokemon_to_attack.tipo == "Agua":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Fuego":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Electrico":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Planta":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Fantasma":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Roca":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 2)
            elif pokemon_to_attack.tipo == "Volador":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Psiquico":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Lucha":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Bicho":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Acero":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Hielo":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Dragon":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Insecto":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
        elif self.tipo == "Volador":
            if pokemon_to_attack.tipo == "Agua":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Fuego":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Electrico":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Planta":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Fantasma":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Roca":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Volador":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 2)
            elif pokemon_to_attack.tipo == "Psiquico":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Lucha":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Bicho":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Acero":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Hielo":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Dragon":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Insecto":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
        elif self.tipo == "Psiquico":
            if pokemon_to_attack.tipo == "Agua":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Fuego":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Electrico":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Planta":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Fantasma":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Roca":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Volador":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Psiquico":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 2)
            elif pokemon_to_attack.tipo == "Lucha":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Bicho":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Acero":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Hielo":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Dragon":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Insecto":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
        elif self.tipo == "Lucha":
            if pokemon_to_attack.tipo == "Agua":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Fuego":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Electrico":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Planta":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Fantasma":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Roca":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Volador":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Psiquico":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Lucha":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 2)
            elif pokemon_to_attack.tipo == "Bicho":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Acero":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Hielo":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Dragon":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Insecto":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
        elif self.tipo == "Bicho":
            if pokemon_to_attack.tipo == "Agua":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Fuego":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Electrico":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Planta":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Fantasma":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Roca":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Volador":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Psiquico":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Lucha":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Bicho":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 2)
            elif pokemon_to_attack.tipo == "Acero":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Hielo":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Dragon":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Insecto":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
        elif self.tipo == "Acero":
            if pokemon_to_attack.tipo == "Agua":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Fuego":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Electrico":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Planta":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Fantasma":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Roca":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Volador":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Psiquico":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Lucha":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Bicho":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Acero":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 2)
            elif pokemon_to_attack.tipo == "Hielo":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)   
            elif pokemon_to_attack.tipo == "Dragon":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Insecto":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
        elif self.tipo == "Hielo":
            if pokemon_to_attack.tipo == "Agua":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Fuego":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Electrico":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Planta":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Fantasma":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Roca":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Volador":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Psiquico":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Lucha":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Bicho":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Acero":
                pokemon_to_attack.v
                pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Hielo":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 2)
            elif pokemon_to_attack.tipo == "Dragon":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Insecto":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
        elif self.tipo == "Dragon":
            if pokemon_to_attack.tipo == "Agua":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Fuego":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Electrico":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Planta":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Fantasma":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Roca":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Volador":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Psiquico":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Lucha":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Bicho":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Acero":
                pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Hielo":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Dragon":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 2)
            elif pokemon_to_attack.tipo == "Insecto":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
        elif self.tipo == "Insecto":
            if pokemon_to_attack.tipo == "Agua":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Fuego":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Electrico":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Planta":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Fantasma":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Roca":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Volador":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Psiquico":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Lucha":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Bicho":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Acero":
                pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Hielo":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Dragon":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 0.5)
            elif pokemon_to_attack.tipo == "Insecto":
                pokemon_to_attack.vida = pokemon_to_attack.vida - (self.ataque * 2)
        #  Programe el método fight_defense(self, int points_of_damage)

    def fight_defense(self, points_of_damage):
        self.vida = self.vida - points_of_damage
        if self.vida <= 0:
            self.vida = 0
            self.esta_vivo = False
        else:
            self.esta_vivo = True
    #  Programe el método is_alive(self) que devuelve True si el Pokémon está vivo y False en caso contrario.

    def is_alive(self):
        if self.esta_vivo == True:
            return True
        else:
            return False
    #  Programe el método revive(self) que reviva al Pokémon.

    def revive(self):
        self.esta_vivo = True
        self.vida = self.vida_maxima
    #  Programe el método get_name(self) que devuelve el nombre del Pokémon.

    


    def __str__(self):
        return "Pokemon: " + self.nombre + " Tipo: " + self.tipo + " Vida: " + str(self.vida) + " Ataque: " + str(
            self.ataque) + " Defensa: " + str(self.defensa) + " Velocidad: " + str(self.velocidad) + " Esta vivo: " + str(
            self.esta_vivo)

        



               



       
 

    

 
    

#funcion get y set ID del Pokémon. Número entero y único que identifica a la criatura Pokémon.
#funcion get y set Nombre del Pokémon. Nombre de la critarua Pokémon.
#funcion get y set Tipo de arma que lleva a cabo el Pokémon. En esta primera versión del juego, solamente 4 tipos de arma van a existir: Puñetazo, Patada, Codazo, Cabezazo.
#funcion get y set Puntos de salud que tiene el Pokémon. Deben de estar entre 1 y 100.

# funcion get y set Índice de ataque del Pokémon. Deben de estar entre 1 y 10.
#funcion get y set Índice de defensa del Pokémon. Deben de estar entre 1 y 10.






