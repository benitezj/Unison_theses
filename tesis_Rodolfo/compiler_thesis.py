######Instructions######
#Run as :
#>python3 compiler_thesis.py
#######################
import os
# colorama_demo.py
from colorama import init, Fore, Back, Style

# Initializes Colorama
init(autoreset=True)

print(Style.BRIGHT + Back.WHITE + Fore.RED + "Cleaning Some Files...")
dir_name = os.getcwd()
test = os.listdir(dir_name)

for item in test:
    if item.endswith("~"):
        os.remove(os.path.join(dir_name, item))
    if item.endswith(".toc"):
        os.remove(os.path.join(dir_name, item))
    if item.endswith(".bbl"):
        os.remove(os.path.join(dir_name, item))
    if item.endswith(".log"):
        os.remove(os.path.join(dir_name, item))
    if item.endswith(".out"):
        os.remove(os.path.join(dir_name, item))
    if item.endswith(".blg"):
        os.remove(os.path.join(dir_name, item))
print(Style.BRIGHT + Back.WHITE + Fore.BLUE + "Cleaning... DONE")

print(Style.BRIGHT + Back.BLACK + Fore.RED + "Compiling thesis.tex (1st)")
os.system("pdflatex thesis.tex")
print(Style.BRIGHT + Back.BLACK + Fore.RED + "Compiling thesis.aux")
os.system("bibtex thesis.aux")
print(Style.BRIGHT + Back.BLACK + Fore.BLUE + "Compiling thesis.tex (2nd)")
os.system("pdflatex thesis.tex")
print(Style.BRIGHT + Back.BLACK + Fore.GREEN + "Compiling thesis.tex (3rd)")
os.system("pdflatex thesis.tex")
print(Style.BRIGHT + Back.BLACK + Fore.GREEN + "DONE: thesis.pdf'")
