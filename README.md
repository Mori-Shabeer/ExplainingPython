# **Python**
![hello-world](https://github.com/user-attachments/assets/32a87345-b105-4a63-88ec-badcd19bd2eb)

## **Get Started**
-	To get started we will need to first download Python onto our local system. To do so, please go on https://www.python.org/downloads/, there you will find the download link.<br>
  **NOTE: The website will automatically recognise what type of operating system your local machine is using (MacOS, Windows or Linux)**
-	Once you have downloaded Python please download Pycharm, type into Google Pycharm Download and you should find the website to download. <br>
  **NOTE: Please ensure you download the Community Edition of Pycharm**

### **What is Python** 
-	**High-level programming language:** Python is known for its clear and readable syntax, making it easier to learn and use compared to many other languages. 
-	**Versatile:** Python can be used for a wide range of applications, including web development, data science and machine learning, scripting, automation, and more. 
-	**Object-Oriented:** Python supports object-oriented programming principles like classes, objects, and inheritance, allowing you to structure your code in a modular and organized way. 
-	**Interpreted:** Python code is executed line by line, making it easier to debug and test. 
-	**Large and active community:** Python has a vast and supportive community, providing extensive documentation, libraries, and resources for developers. 
-	**Open-source:** Python is open-source and free to use, making it accessible to everyone.

### **Python & Pycharm**
-	When you start Pycharm to test that your Python is operating properly we will do the ‘Hello World’ test.
-	Start a new Python file on Pycharm and lets name Python practise. Pycharm will automatically make it a .pd file. Once the new python file is made please type in PRINT(‘Hello World’)
-	Once you type it out please run it and one of two results should happen. If you have successfully downloaded everything you should see ‘Hello World’. If not you should see an error message, if so please re-download Python and Pycharm if needed.

![Screenshot 2025-01-27 at 10 57 49](https://github.com/user-attachments/assets/59cce9d3-653f-47e1-ad78-7aca1b7a779b)


### **Data Types**
-	**Numbers:** There two type of number data types we tend to do deal with in Python they are integers which are whole numbers or floating point numbers which deal with number with decimals
-	**String:** Which deal with characters or text
-	**Boolean:** Which are either true or false statements
-	To view what type of data you are dealing with you can run this code; PRINT(type(Enter a statement or number))<br>
  **NOTE: There many type of data we can deal with in Python but these are the 3 most common.**

![Screenshot 2025-01-27 at 11 09 07](https://github.com/user-attachments/assets/d10bec2a-78c6-4490-8329-d309e0beac23)


### **Numbers in Python** 
Numbers are used to represent quantities, measurements, and perform mathematical calculations in Python.<br>
There are two main types of numbers:
* **Integers (int):** Whole numbers, like 10, -5, and 0. 
* **Floats (float):** Numbers with decimal points, like 3.14 and -2.5. 

### **Strings in Python** 
- A string is a sequence of characters, including letters, numbers, symbols, and spaces, enclosed within single quotes (') or double quotes (").   '"This is a string!"' 🗨
- Strings are immutable, meaning that once created, their content cannot be changed. Any operation that appears to modify a string actually creates a new string. 🔒
- Strings are fundamental for representing text data like names, messages, file paths, and more. 📄  ℹ️  📁<br>
**NOTE:** String types: https://docs.python.org/3/library/stdtypes.html#string-methods

### Variables in Python 
- Variables are like containers that store data within a Python program.  📦
- You can give variables meaningful names to represent the information they hold (e.g., `age`, `name`, `price`).  🏷️
- Python uses **dynamic typing**, meaning it automatically determines the data type (integer, string, etc.) of a variable based on the value assigned to it. 🪄
- You create a variable by assigning a value to it using the = operator (e.g., `age = 30`, `name = "John"`).  🔨
- Variable names are **case-sensitive**. This means that `age` and `Age` are considered different variables.  `age != Age`
- Use descriptive names for better readability (e.g., `customer_name` instead of `c`).  📖 ❌ c  ✅ customer_name
- The value stored in a variable can be changed at any time.  🔄<br>
**NOTE:** Python style guide: https://peps.python.org/pep-0008/

### if Statements in Python 🤔
**if statements** allow you to control the flow of your program based on whether a condition is true or false. <br>
**elif statements** are used to check for multiple conditions sequentially. <br>
**Key Points** 🔑
* **if statements** are essential for making decisions in your Python programs.  ✔️
* **elif statements** provide a concise way to check for multiple conditions.  ✨
* The **else block** is optional and executes when none of the preceding if or elif conditions are true.  🤷‍♂️

### Collections  🗃️
Collections are a framework for working with groups of objects in Python. They provide efficient ways to store, access, and manipulate data. Common collection types include lists, tuples, sets, and dictionaries. <br>
#### Lists  📃
A list is an ordered, mutable sequence of objects.  They are enclosed in square brackets `[]` and can store elements of different data types (e.g., integers, strings, other lists).  Lists are accessed by index (zero-based) and support various operations like appending, inserting, removing, and slicing. <br>
#### Dictionaries  📒
A dictionary is an unordered collection of key-value pairs.  They are enclosed in curly braces `{}`. Keys are unique and immutable (often strings or numbers), while values can be of any data type. Dictionaries are accessed by their keys and are efficient for looking up values based on those keys.  🔑  🔎

# Loops in Python 🔁
Loops are used to execute a block of code repeatedly.
* **While Loops**  🔄
    * A `while` loop continues to execute a block of code as long as a given condition is True. Be careful to avoid infinite loops!  ⚠️
* **For Loops**  🔜
    * A `for` loop iterates over a sequence, executing a block of code for each item in the sequence (e.g., list, tuple, string).  ✅


### **Commands in Python**

| Command | Description |
|---|---|
| `# (Followed by any statement)` | Allows Python to recognize that this is not a piece of code it needs to run as you are just commenting. |
| `print('Followed by text')` | Allows you to display text, or an answer you are seeking. |
| `print(type(Enter a statement or number))` | Allows to see what data type you are dealing with. |
| `print(len(Followed by statement))` | Allows you to find out the length or total characters in your string statement. |
| `print(string.upper())` | Converts all characters in the string to uppercase. |
| `print(string.lower())` | Converts all characters in the string to lowercase. |

### **Arithmetic Operators in Python**

| Operator | Description | Example |
|---|---|---|
| `+` | Addition | `5 + 3 = 8` |
| `-` | Subtraction | `10 - 4 = 6` |
| `*` | Multiplication | `2 * 5 = 10` |
| `/` | Division | `10 / 2 = 5.0` |
| `//` | Floor Division | `10 // 3 = 3` |
| `%` | Modulus | `10 % 3 = 1` |
| `**` | Exponentiation | `2 ** 3 = 8` |
