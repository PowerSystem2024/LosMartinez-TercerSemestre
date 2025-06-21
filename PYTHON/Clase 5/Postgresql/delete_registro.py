import psycopg2  # Esto es para poder conectarnos a Postgre

connection = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd')

try:
    with connection:
        with connection.cursor() as cursor:
            query = 'DELETE FROM persona WHERE id_persona = %s'
            input_id = input('Digite el número de registro a eliminar: ')
            values = (input_id,)  # Es una tupla de valores

            cursor.execute(query, values)  # De esta manera ejecutamos la sentencia
            deleted_records = cursor.rowcount
            print(f'Los registros eliminados son: {deleted_records}')

except Exception as e:
    print(f'Ocurrió un error: {e}')

finally:
    connection.close()
