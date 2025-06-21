class NumerosIgualesException(Exception):
    """Excepción personalizada para cuando ambos números son iguales."""
    pass

try:
    numero1 = int(input('Digite el primer número: '))
    numero2 = int(input('Digite el segundo número: '))

    if numero1 == numero2:
        raise NumerosIgualesException('Los números son iguales.')

    resultado = numero1 / numero2

except TypeError as e:
    print(f'TypeError - Ocurrió un error: {type(e)}')

except ZeroDivisionError as e:
    print(f'ZeroDivisionError - Ocurrió un error: {type(e)}')

except NumerosIgualesException as e:
    print(f'NumerosIgualesException - {e}')

except Exception as e:
    print(f'Excepción - Ocurrió un error: {type(e)}')

else:
    print('No se arrojó ninguna excepción.')

finally:
    print('Este bloque siempre se va a ejecutar.')

print(f'El resultado es: {resultado}')
print('Seguimos...')