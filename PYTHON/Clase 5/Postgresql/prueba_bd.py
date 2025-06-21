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
            query = 'SELECT * FROM persona WHERE id_persona = %s'
            person_id = input('Id a buscar: ')
            cursor.execute(query, (person_id,))
            result = cursor.fetchone()

            print(result)

except Exception as e:
    print(f'Ocurrió un error: {e}.')

finally:
    connection.close()