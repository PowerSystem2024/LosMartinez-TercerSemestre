import psycopg2

connection = psycopg2.connect(
    user="postgres",
    password="admin",
    host="127.0.0.1",
    port="5432",
    database="db_test"
)

print("Conexión exitosa a la base de datos")
print(connection)

with connection:
    with connection.cursor() as cursor:
        sql = "SELECT * FROM persona"
        cursor.execute(sql)
        results = cursor.fetchall()

        if results:
            print(f"Personas encontradas: {results}")
        else:
            print("No se encontró la persona con el id proporcionado.")

print("Conexión cerrada")
print("Fin del programa")