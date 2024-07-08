# RG Pre-work Assignment 

<br>
<br>


### Running the SQL Script:

1. **Open a Terminal or Command Prompt:**
   - Navigate to the folder where you have stored the assignment files.

2. **Start SQLite3:**
   - Run the command `sqlite3 assignment.db`.
     - If you encounter an error, ensure that SQLite3 tools are installed on your system.

4. **Query the `student` Table:**
   - Use the following SQL command to query specific data from the `student` table. For example:
     ```
     SELECT name, marks FROM student WHERE name LIKE '%search_string%';
     ```
     Replace `search_string` with the term you want to search for in the `name` column. This query will return all rows where the `name` contains the specified search string (case insensitive).

5. **View Results:**
   - The SQL shell will display the names and marks of students matching the search criteria.

6. **Quit SQLite3:**
   - Type `.quit` to exit the SQLite shell.


<br>
<br>

### Running the Python Script:

1. **Ensure Python is Installed:**
   - Make sure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Open a Terminal or Command Prompt:**
   - Navigate to the folder containing your Python script (`students.py`).

3. **Run the Python Script:**
   - Execute the script using Python:
     ```
     python students.py
     ```
   
4. **Follow the Script Prompts:**
   - The script will prompt you to enter a search string. Enter the string and press Enter.

5. **View Results:**
   - The script will query the database (`assignment.db`) and display names and marks of students matching the search string. It will also calculate and display total and average marks.
