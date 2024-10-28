from validadorclave.modelo.errores import NoCumpleLongitudMinimaError, ValidadorError
from validadorclave.modelo.validador import ReglaValidacion, Validador, ReglaValidacionGanimedes, ReglaValidacionCalisto


def validar_clave(clave: str, reglas: list[ReglaValidacion]):
    for regla in reglas:
        validador = Validador(regla)
        try:

            validador.es_valida(clave)

        except ValidadorError as err:
            print(f"Error: {type(regla).__name__}: {err}")

        else:
            print(f"Clave válida según regla {type(regla).__name__}")


if __name__ == "__main__":
    clave: str = input("Ingrese una clave: ")
    reglas: list[ReglaValidacion] = [ReglaValidacionGanimedes(), ReglaValidacionCalisto()]
    validar_clave(clave, reglas)
