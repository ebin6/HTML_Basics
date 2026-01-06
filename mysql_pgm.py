import pymysql

connection=pymysql.connect(user="root",password="admin",host="localhost",database="shopping_mart",cursorclass=pymysql.cursors.DictCursor)



# with connection.cursor() as cursor:
#     cursor.execute("SELECT * FROM users")
#     print(cursor.fetchall())

def addCategory():
    category=input("Enter category name : ")
    with connection.cursor() as cursor:
        cursor.execute(f"INSERT INTO categories(category_name)VALUES('{category}')")
        print("New category added")
        connection.commit()

def addProduct():
    product=input("Enter product name : ")
    category=int(input("Enter the category id : "))
    price=float(input("Enter the price : "))
    stock=int(input("Enter the stock detail : "))
    with connection.cursor() as cursor:
        cursor.execute(f"INSERT INTO products(prod_name,category_id,price,stock)VALUES('{product}','{category}',{price},{stock})")
        print("New Product added")
        connection.commit()

def viewCategories():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM categories ORDER BY category_id")
        for category in cursor.fetchall():
            print("-------------------------")
            print(category["category_id"],category["category_name"])

def viewProducts():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM products ORDER BY product_id")
      # print(cursor.fetchall())
        print("All products")
        for prod in cursor.fetchall():
            print("-------------------------")
            print(prod["product_id"], prod["prod_name"],prod["category_id"],prod["price"],prod["stock"])

        print("--------------------")

while True:
    print("1.Add category\n2.Add Product \n3.View Categories\n4.View All Products\n5.Exit")
    choice=int(input("Enter you choice : "))
    if choice==1:
        addCategory()
    elif choice==2:
        addProduct()
    elif choice==3:
        viewCategories()
    elif choice==4:
        viewProducts()
    elif choice==5:
        break
    else:
        print("Invalid choice")