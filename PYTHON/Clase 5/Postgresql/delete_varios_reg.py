import psycopg2

DB_CONFIG = {
    'user': 'postgres',
    'password': 'admin',
    'host': '127.0.0.1',
    'port': '5432',
    'database': 'test_bd',
    'client_encoding': 'utf8'
}

connection = psycopg2.connect(**DB_CONFIG)

try:
    with connection:
        with connection.cursor() as cursor:
            query = 'DELETE FROM persona WHERE id_persona IN %s'
            user_input = input('Digite los números de registros que desee eliminar (separados por coma): ')

            try:
                ids = tuple(int(x.strip()) for x in user_input.split(',') if x.strip().isdigit())
            except ValueError:
                raise Exception("Entrada inválida: asegúrese de ingresar solo números separados por comas.")

            if not ids:
                print('No se ingresaron IDs válidos.')
            else:
                cursor.execute(query, (ids,))
                deleted_records = cursor.rowcount
                print(f'Los registros eliminados son: {deleted_records}')

except Exception as e:
    print(f'Ocurrió un error: {e}')

finally:
    connection.close()