import os

commands = ["pdflatex main.tex ", "makeglossaries main", "bibtex main","rm *.aux"]

print commands[3]
os.system(commands[3])

print commands[0]
os.system(commands[0])
print commands[1]
os.system(commands[1])
print commands[2]
os.system(commands[2])

print commands[0]
os.system(commands[0])
print commands[0]
os.system(commands[0])
