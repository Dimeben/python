"""
Reading a File
This opens a file object called cool_doc and creates a new indented block where you can read the contents of the opened file. 
We then read the contents of the file cool_doc using cool_doc.read() and save the resulting string into the variable cool_contents. 
Then we print cool_contents, which outputs the statement Wowsers!.
"""

with open("Files/Resources/real_cool_document.txt") as cool_doc:
    cool_contents = cool_doc.read()
print(cool_contents)

with open("Files/Resources/welcome.txt") as text_file:
    text_data = text_file.read()
print(text_data)


"""
Iterating Through Lines
The script creates a temporary file object called keats_sonnet that points to the file keats_sonnet.txt. 
It then iterates over each line in the document and prints the entire file out.
"""
with open("Files/Resources/keats_sonnet.txt") as keats_sonnet:
    for line in keats_sonnet.readlines():
        print(line)

with open("Files/Resources/how_many_lines.txt") as lines_doc:
    for line in lines_doc.readlines():
        print(line)

"""
Reading a Line
"""

"""
Writing a File
"""

"""
Appending to a File
"""

"""
What's With "with"?
"""

"""
What Is a CSV File?
"""

"""
Reading a CSV File
"""

"""
Reading Different Types of CSV Files
"""

"""
Writing a CSV File
"""

"""
Reading a JSON File
"""

"""
Writing a JSON File
"""
