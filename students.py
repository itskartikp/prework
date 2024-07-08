import sqlite3

#Function to connect to the SQLite database.
def connect_to_sql_database(db_name):
    connection = sqlite3.connect(db_name)
    return connection

#Function to search for students with names starting with the search string (case insensitive).
def search_students_by_name(connection, search_name):
    cursor = connection.cursor()
    query = "SELECT name, marks FROM Students WHERE name LIKE ? COLLATE NOCASE"
    cursor.execute(query, (search_name + '%',))  
    return cursor.fetchall()


#Function to print the search results in a table format.
def print_result(results):

    if results:
        headers = ["Name", "Marks"]
        col_widths = [max(len(str(row[i])) for row in results) for i in range(len(headers))]
        col_widths = [max(len(header), width) for header, width in zip(headers, col_widths)]

        format_string = ' | '.join([f"{{:<{width}}}" for width in col_widths])

        print(format_string.format(*headers))
        print('-' * (sum(col_widths) + len(col_widths) * 3 - 1))

        for row in results:
            print(format_string.format(*row))

        total_marks = sum(row[1] for row in results)
        average_marks = total_marks / len(results) if results else 0

        print('-' * (sum(col_widths) + len(col_widths) * 3 - 1))
        print(f"{'Total Marks':<{col_widths[0]}} | {total_marks:<{col_widths[1]}}")
        print(f"{'Average Marks':<{col_widths[0]}} | {average_marks:.2f}")
        print()

    else:
        print("No results found.")
        print()



def main():
    db_name = 'assignment.db'

    while True:
        search_name = input("Enter a search string: ").strip()      
        print()  

        if not search_name:
            print("Please enter a search string.")
            continue

        connection = connect_to_sql_database(db_name)
        results = search_students_by_name(connection, search_name)
        connection.close()

        print_result(results)


if __name__ == "__main__":
    main()
