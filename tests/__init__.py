from abc import ABC, abstractmethod


class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada: int):
        self._longitud_esperada: int
        self.longitud_esperada: int = longitud_esperada


    def _validar_longitud(self, clave: str) -> bool:
        pass

    def _contiene_mayusculas(self, clave: str) -> bool:
        contiene_mayus = any(caracter.isupper() for caracter in clave)
        return contiene_mayus


    def _contiene_minisculas(self, clave: str) -> bool:
        contiene_min = any(caracter.islower() for caracter in clave)
        return contiene_min

    def _contiene_numero(self, clave: str) -> bool:
        contiene_num = any(caracter.isdigit() for caracter in clave)
        return contiene_num

    @abstractmethod
    def es_valida(self, clave: str) -> bool:
        pass

class Validador:
    def __init__(self, regla: ReglaValidacion):
        self.regla: ReglaValidacion = regla

    def es_valida(self, clave: str) -> bool:
        return self.regla.es_valida(clave)

class ReglaValidacionGanimedes(ReglaValidacion):
    def __init__(self):
        pass

    def contiene_caracter_especial(self, clave: str) -> bool:
        cont = 0
        c_especial = "@_#$%"
        for caracter in clave:
            if caracter in c_especial:
                cont += 1

        if cont >= 1:
            return True
        else:
            return False






