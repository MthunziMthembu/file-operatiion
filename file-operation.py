names ="C:/Users/Admin/Desktop/names.txt"
output = "C:/Users/Admin/Desktop/output.txt"

#reading file and display
with open(names, 'r')as file:
    text = file.read()
    wordCount = len(text.split())
    print(text)
    print("word count:", wordCount)

#Writing a file
with open(output, 'w')as file:
    line1 = file.write('Careers IT\n')
    line2 = file.write('Systems Developers\n')
    line3 = file.write('Assessor - Nicky Masiya\n')
    file.close()
