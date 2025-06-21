import psycopg2  # Esto es para poder conectarnos a Postgre

connection = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd')

try:
    with connection:
        with connection.cursor() as cursor:
            query = 'INSERT INTO persona (nombre, apellido, email) VALUES (%s, %s, %s)'
            values = (
                ('Carlos', 'Lara', 'clara@mail.com'),
                ('Marcos', 'Canto', 'mcanto@mail.com'),
                ('Marcelo', 'Cuenca', 'cuencaM@mail.com'),
            )  # Es una tupla de tuplas

            cursor.executemany(query, values)  # De esta manera ejecutamos la sentencia
            # connection.commit() esto se utiliza para guardar los cambios en la base de datos
            inserted_records = cursor.rowcount
            print(f'Los registros insertados son: {inserted_records}')

except Exception as e:
    print(f'Ocurrió un error: {e}')

finally:
    connection.close()