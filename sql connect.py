import pypyodbc

# Connection string to connect to your SQL Server using ODBC Driver 17 and Windows Authentication
conn = pypyodbc.connect(r'Driver={ODBC Driver 17 for SQL Server};'
                        r'Server=DESKTOP-O5D0NIF\SQLEXPRESS;'
                        'Database=amazon_seller;'
                        'Trusted_Connection=yes;')

# Creating a cursor object
cursor = conn.cursor()

# Example SQL query - replace 'orders' with the name of an existing table in your database
cursor.execute('SELECT * FROM amazon_staging_data')

# Fetching all results from the executed query
results = cursor.fetchall()

# Printing the results
for row in results:
    print(row)

# Close the connection
conn.close()
