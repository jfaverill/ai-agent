from functions.get_file_content import  get_file_content

content = get_file_content("calculator", "main.py")
print("--------------------------------------------")
print(content)
content = get_file_content("calculator", "pkg/calculator.py")
print("--------------------------------------------")
print(content)
content = get_file_content("calculator", "/bin/cat")
print("--------------------------------------------")
print(content)