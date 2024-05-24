import os
class Paciente:

    pacientes = []

    def __init__(self, nombre, apellido, dni, h_clinica, obra_social):
        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni
        self._h_clinica = h_clinica
        self._obra_social = obra_social

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, dni):
        self._dni = dni  # Error de nombre de variable corregido

    @property
    def h_clinica(self):
        return self._h_clinica

    @h_clinica.setter
    def h_clinica(self, h_clinica):  # Nombre de método corregido
        self._h_clinica = h_clinica

    @property
    def obra_social(self):
        return self._obra_social

    @obra_social.setter
    def obra_social(self, obra_social):
        self._obra_social = obra_social

    @classmethod
    def agregar_pacientes(cls):
        nombre = input('Ingrese el nombre del paciente: ')
        apellido = input('Ingrese el apellido del paciente: ')
        dni = int(input('Ingrese el documento del paciente(sin puntos): '))
        h_clinica = input('Historia clinica: ')
        obra_social = input('Ingrese la obra social: ')
        paciente = cls(nombre, apellido, dni, h_clinica, obra_social)
        cls.pacientes.append(paciente)

    @classmethod
    def actualizar_pacientes(cls):
        h_clinica = input('Ingrese la historia clinica a actualizar: ')
        paciente_encontrado = False

        for paciente in cls.pacientes:
            if paciente.h_clinica == h_clinica:
                paciente.nombre = input('Ingrese el nombre del paciente: ')
                paciente.apellido = input('Ingrese el apellido del paciente: ')
                paciente.dni = int(input('Ingrese el documento del paciente(sin puntos): '))
                paciente.obra_social = input('Ingrese la obra social: ')
                paciente_encontrado = True
                break

        if not paciente_encontrado:
            print('No se encontró al paciente')

    @classmethod
    def eliminar_paciente(cls):
        h_clinica = input('Ingrese el nombre de la historia clinica a eliminar: ')
        paciente_encontrado = False

        for i, paciente in enumerate(cls.pacientes):
            if paciente.h_clinica == h_clinica:
                del cls.pacientes[i]
                paciente_encontrado = True
                break
        if not paciente_encontrado:
            print('Paciente no encontrado')

    @classmethod
    def mostrar_paciente(cls):
        if not cls.pacientes:
            print('No hay pacientes')
        else:
            for paciente in cls.pacientes:
                print(f"Nombre: {paciente.nombre}")
                print(f"Apellido: {paciente.apellido}")
                print(f"DNI: {paciente.dni}")
                print(f"Historia Clinica: {paciente.h_clinica}")
                print(f"Obra Social: {paciente.obra_social}")
                print()

    @classmethod
    def buscar_pacientes(cls):
        criterio_de_busqueda = input('Ingrese el criterio de busqueda: ')
        pacientes_encontrados = []

        for paciente in cls.pacientes:
            if criterio_de_busqueda.lower() in paciente.apellido.lower() or \
                    criterio_de_busqueda.lower() in paciente.h_clinica.lower():
                pacientes_encontrados.append(paciente)

        if pacientes_encontrados:
            for paciente in pacientes_encontrados:
                print(f'Nombre: {paciente.nombre}')
                print(f'Apellido: {paciente.apellido}')
                print(f'DNI: {paciente.dni}')
                print(f'Historia Clinica: {paciente.h_clinica}')
                print(f'Obra Social: {paciente.obra_social}')
                print()
        else:
            print('No se encontraron pacientes')


# Main
while True:
    print("\nMenú:")
    print("1. Agregar paciente")
    print("2. Actualizar paciente")
    print("3. Eliminar paciente")
    print("4. Mostrar historia clinica")
    print("5. Buscar paciente")
    print("6. Salir")

    opcion = input("Ingrese la opción deseada: ")

    if opcion == '1':
        Paciente.agregar_pacientes()
    elif opcion == '2':
        Paciente.actualizar_pacientes()
    elif opcion == '3':
        Paciente.eliminar_paciente()
    elif opcion == '4':
        Paciente.mostrar_paciente()
    elif opcion == '5':
        Paciente.buscar_pacientes()
    elif opcion == '6':
        break
    else:
        print('Opción no válida')
