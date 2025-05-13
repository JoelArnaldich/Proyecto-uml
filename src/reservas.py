class Usuario:
    def __init__(self, nombre: str, correo: str):
        self.nombre = nombre
        self.correo = correo

    def get_nombre(self) -> str:
        return self.nombre

    def get_correo(self) -> str:
        return self.correo


class Sala:
    def __init__(self, nombre: str, capacidad: int):
        self.nombre = nombre
        self.capacidad = capacidad

    def get_nombre(self) -> str:
        return self.nombre

    def get_capacidad(self) -> int:
        return self.capacidad


class Reserva:
    def __init__(self, usuario: Usuario, sala: Sala, fecha: str, hora_inicio: str, hora_fin: str):
        self.usuario = usuario
        self.sala = sala
        self.fecha = fecha
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin

    def get_fecha(self) -> str:
        return self.fecha

    def get_hora_inicio(self) -> str:
        return self.hora_inicio

    def get_hora_fin(self) -> str:
        return self.hora_fin

    def get_usuario(self) -> Usuario:
        return self.usuario

    def get_sala(self) -> Sala:
        return self.sala