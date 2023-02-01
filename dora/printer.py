import re
from colorama import Fore, Style

class Printer:
    def __init__(self, color, verbose):
        self.color = color
        self.verbose = verbose

    def content(self, text: str) -> None:
        text = re.sub("^", " | ", text)
        text = text.replace("\n", "\n | ")
        print(text)


    def positive(self, text: str):
        if self.color:
            print("{0}[+]{1} {2}".format(Fore.GREEN, Style.RESET_ALL, text))
        else:
            print("[+] {}".format(text))


    def negative(self, text: str):
        if self.color:
            print("{0}[-]{1} {2}".format(Fore.RED,Style.RESET_ALL,text))
        else:
            print("[-] {}".format(text))


    def good(self, text: str):
        if self.color:
            print("{0}[✔]{1} {2}".format(Fore.GREEN, Style.RESET_ALL,text))
        else:
            print("[✔] {}".format(text))


    def bad(self, text: str):
        if self.color:
            print("{0}[✘]{1} {2}".format(Fore.RED,Style.RESET_ALL,text))
        else:
            print("[✘] {}".format(text))


    def warning(self, text: str):
        if self.color:
            print("{0}[!]{1} {2}".format(Fore.YELLOW,Style.RESET_ALL,text))
        else:
            print("[+] {}".format(text))


    def info(self, text: str):
        if self.color:
            print("{0}[i]{1} {2}".format(Fore.BLUE,Style.RESET_ALL,text), end="\n" if self.verbose else "\r")
        else:
            print("[i] {}".format(text), end="\n" if self.verbose else "\r")
