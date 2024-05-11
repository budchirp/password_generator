#!/usr/bin/env python

import random
import shutil
import string
import time


class PasswordGenerator:
    colors = {
        "white": "\033[1;37m",
        "green": "\033[32m",
        "gray": "\033[30m",
        "blue": "\033[34m",
        "red": "\033[31m",
        "endc": "\033[0m",
    }

    dictionary = {
        "en": {
            "length_input": f"{colors['green']}Enter password length (default: 8): {colors['gray']}",
            "length_error": f"{colors['red']}Password length cannot be lower than 8 characters!",
            "done": f"{colors['green']}Your generated password is: {colors['gray']}%password%{colors['endc']}",
        },
        "tr": {
            "length_input": f"{colors['green']}Şifre uzunluğunu girin (varsayılan: 8): {colors['gray']}",
            "length_error": f"{colors['red']}Şifre uzunluğu 8 karakterden az olamaz!",
            "done": f"{colors['green']}Oluşturulan şifreniz: {colors['gray']}%password%{colors['endc']}",
        },
    }

    def __init__(self):
        self.lower = string.ascii_lowercase
        self.upper = string.ascii_uppercase
        self.symbol = "(){}[]-&!?*%+:/#"
        self.number = string.digits

        self.all = self.lower + self.upper + self.number + self.symbol

        self.lang = "en"
        self.length = 8

        self.columns, self.rows = shutil.get_terminal_size((80, 25))

    def separator(self):
        print(f"{self.colors["gray"]}-" * self.columns)

    def select_length(self):
        self.length = input(self.dictionary[self.lang]["length_input"]) or 8

        self.length = int(self.length)

        if int(self.length) < 8:
            print(self.dictionary[self.lang]["length_error"])

            self.select_length()

    def select_lang(self):
        print(f"{self.colors["white"]}Please enter a language")
        print(f"{self.colors["white"]}Lütfen bir dil girin\n")

        lang = input(f"{self.colors["green"]}[EN] English [TR] Türkçe: {
        self.colors["gray"]}").lower()

        if lang == "tr" or lang == "türkçe":
            self.lang = "tr"
        elif lang == "en" or lang == "english":
            self.lang = "en"

    def generate(self, length):
        all_listed = list(self.all)

        random.shuffle(all_listed)

        password = random.choices(all_listed, k=length)
        password = "".join(password)

        return password

    def main(self):
        self.separator()

        print(f"""{self.colors["blue"]}____                                     _
|  _ \\ __ _ ___ _____      _____  _ __ __| |
| |_) / _` / __/ __\\ \\ /\\ / / _ \\| '__/ _` |{self.colors["red"]}
|  __/ (_| \\__ \\__ \\ V  V / (_) | | | (_| |
|_|   \\__,_|___/___/ \\_/\\_/ \\___/|_|  \\__,_|{self.colors["green"]}

    ____                           _
    / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __
| |  _ / _ \\ '_ \\ / _ \\ '__/ _` | __/ _ \\| '__|{self.colors["gray"]}
| |_| |  __/ | | |  __/ | | (_| | || (_) | |
    \\____|\\___|_| |_|\\___|_|  \\__,_|\\__\\___/|_|{self.colors["endc"]}
""")

        self.separator()

        self.select_lang()
        self.separator()

        self.select_length()
        self.separator()

        password = self.generate(self.length)

        time.sleep(1)

        print(self.dictionary[self.lang]["done"].replace("%password%", password))


if __name__ == "__main__":
    generator = PasswordGenerator()

    generator.main()
