class tamagochi:
    def __init__(self,nombre):
        self._nombre = nombre
        self.nivel_de_energia = 100
        self.nivel_de_hambre = 0
        self.nivel_de_felicidad = 50
        self.humor = self.actualizar_humor()
        self.esta_vivo = True
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre

    def __str__(self):
        return f"""
        Nombre: {self._nombre}
        Energía: {self.nivel_de_energia}
        Hambre: {self.nivel_de_hambre}
        Felicidad: {self.nivel_de_felicidad}
        Humor: {self.humor}
        Estado: {"Vivo" if self.esta_vivo else "Muerto"}
        """
    def actualizar_humor(self):
        if self.nivel_de_felicidad > 75:
            self.humor = "Euforico!!!"
        elif self.nivel_de_felicidad > 50:
            self.humor = "Estoy feliz"
        elif self.nivel_de_felicidad > 25:
            self.humor = "Estoy indiferente"
        elif self.nivel_de_felicidad > 0:
            self.humor = "estoy triste"
        else:
            self.humor = "Estoy enojado"
        return self.humor

    def alimentar(self):
        self.nivel_de_hambre -= 10
        if self.nivel_de_hambre < 0:
            self.nivel_de_hambre = 0
        self.nivel_de_felicidad += 20
        if self.nivel_de_energia < 0:
            self.nivel_de_energia = 0
        self.actualizar_humor()

    def jugar(self):
        self.nivel_de_felicidad += 20
        if   self.nivel_de_felicidad > 100:
            self.nivel_de_felicidad = 100
        self.nivel_de_energia -= 18
        if self.nivel_de_energia < 0:
            self.nivel_de_energia = 0
        self.nivel_de_hambre += 10
        if self.nivel_de_hambre > 100:
            self.nivel_de_hambre = 100
        self.verificar_estado()

    def dormir(self):
        self.nivel_de_energia += 40
        if self.nivel_de_energia > 100:
            self.nivel_de_energia = 100
            self.nivel_de_hambre +=5
        self.verificar_estado()


    def mostrar_estado(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nivel de energía: {self.nivel_de_energia}")
        print(f"Nivel de hambre: {self.nivel_de_energia}")
        print(f"Nivel de felicidad: {self.nivel_de_felicidad}")
        print(f"Humor: {self.humor}")
        print(f"¿Está vivo?: {self.esta_vivo}")

    def verificar_estado(self):
        if self.nivel_de_energia <= 0:
            self.esta_vivo = False
            print(f"oh {self._nombre} esta muerto!")
        elif self.nivel_de_hambre >= 20:
            
             if self.nivel_de_energia > 0:  # Solo reduce energía y felicidad si aún está vivo
                self.nivel_de_energia -= 20
                self.nivel_de_felicidad -= 30
                print(f'{self._nombre} tiene mucho hambre, dale una milanesa!')
                if self.nivel_de_energia <= 0:
                    self.esta_vivo = False
                print(f"Oh no! {self._nombre} se murió")
        self.actualizar_humor()


nombre_tamagochi = input("Elige un nombre para tu nueva mascota: ")
nuevo_tamagochi = tamagochi(nombre_tamagochi)
nuevo_tamagochi.alimentar()
nuevo_tamagochi.jugar()
nuevo_tamagochi.jugar()
nuevo_tamagochi.mostrar_estado()