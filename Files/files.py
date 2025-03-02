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
This script also creates a file object called sonnet_doc that points to the file millay_sonnet.txt. 
It then reads in the first line using sonnet_doc.readline() and saves that to the variable first_line. 
It then saves the second line (So make the most of this, your little day,) into the variable second_line and then prints it out.
"""
with open("Files/Resources/millay_sonnet.txt") as sonnet_doc:
    first_line = sonnet_doc.readline()
    second_line = sonnet_doc.readline()
    print(second_line)

with open("Files/Resources/just_the_first.txt") as first_line_doc:
    first_line = first_line_doc.readline()
    print(first_line)

"""
Writing a File
Here we pass the argument 'w' to open() in order to indicate to open the file in write-mode. 
The default argument is 'r' and passing 'r' to open() opens the file in read-mode as we've been doing.
"""
with open("Files/Resources/generated_file_original.txt", "w") as gen_file:
    gen_file.write("What an incredible file!")

with open("Files/Resources/bad_bands.txt", "w") as bad_bands_doc:
    bad_bands_doc.write("Taylor Swift!")

"""
Appending to a File
We open it with 'a' for append-mode
In the code above we open a file object in the temporary variable gen_file. 
This variable points to the file generated_file.txt and, since it's open in append-mode, adds the string \n... and it still is to the file. The newline character \n moves to the next line before adding the rest of the string.
"""
with open("Files/Resources/generated_file.txt", "a") as gen_file:
    gen_file.write("\n... and it still is")

with open("Files/Resources/cool_dogs.txt", "a") as cool_dogs_file:
    cool_dogs_file.write("Air Buddy\n")

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
