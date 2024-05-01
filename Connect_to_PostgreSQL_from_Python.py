import psycopg2

conn = None
cur = None

try:
    conn = psycopg2.connect(
        database='project',
        user='postgres',
        password='1',
        host='localhost',
        port='5432'
    )
    conn.autocommit = True
    cur = conn.cursor()


# create table
    def create_table():
        create_tables = """ CREATE TABLE IF NOT EXISTS product (
                            id SERIAL PRIMARY KEY,
                            name VARCHAR(255) NOT NULL,
                            price NUMERIC(10,2) NOT NULL,
                            color VARCHAR(255) NOT NULL ) """
        cur.execute(create_tables)
        print("Table created successfully")


# select_all_product
    def select_all_product():
        select_all = """ SELECT * FROM product """
        cur.execute(select_all)
        for row in cur.fetchall():
            print(row)

    # select_all_product()


# insert_into_product
    def insert_into_product():
        name = str(input("Enter product name: "))
        price = float(input("Enter product price: "))
        color = str(input("Enter product color: "))

        insert_into = """
                        INSERT INTO product (name, price, color)
                        VALUES (%s, %s, %s); """
        insert_into_params = (name, price, color)
        cur.execute(insert_into, insert_into_params)

    # insert_into_product()

# delete_product
    def delete_product():
        select_all_product()
        _id = str(input("Enter product id: "))

        delete_products = """ DELETE FROM product WHERE id = %s; """
        cur.execute(delete_products, _id)
        print("Product deleted successfully")

    # delete_product()


# update_product
    def update_product():
        select_all_product()
        _id = str(input("Enter product id: "))
        name = str(input("Enter product name: "))
        price = str(input("Enter product price: "))
        color = str(input("Enter product color: "))

        update_products = """ UPDATE product SET name = %s, price = %s, color = %s WHERE id = %s; """
        update_products_params = (name, price, color, _id)
        cur.execute(update_products, update_products_params)
        print("Product updated successfully")

    # update_product()


# select_one_product
    def select_one_product():
        _id = str(input('Enter product id: '))

        select_one_products = """ SELECT * FROM product WHERE id = %s; """
        cur.execute(select_one_products, _id)
        product = cur.fetchone()
        if product:
            print(product)
        else:
            print('No such product')

    # select_one_product()


except psycopg2.OperationalError as e:
    print(e)


finally:
    if conn is not None:
        conn.close()
    if cur is not None:
        cur.close()
