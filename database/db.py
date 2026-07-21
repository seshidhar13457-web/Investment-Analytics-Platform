import psycopg2


def get_connection():

    return psycopg2.connect(
        host="localhost",
        database="investment_analytics",
        user="postgres",
        password="Seshidhar@12",
        port=5432
    )