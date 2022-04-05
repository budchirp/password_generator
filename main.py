#!/usr/bin/env python

import random
import signal
import time
import sys
import os

if os.name == "posix":
    class colors:
        white = "\033[1;37m"
        green = "\033[32m"
        gray = "\033[30m"
        blue = "\033[34m"
        red = "\033[31m"
        endc = "\033[0m"
else:
    class colors:
        white = ""
        green = ""
        blue = ""
        gray = ""
        endc = ""
        red = ""


class PasswordGenerator:
    def __init__(self):
        self.lower = "abcdefghijklmnopqrstuvwxyz"
        self.upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.symbol = "(){}[]-&!?*%+:/#"
        self.number = "0123456789"

        self.all = self.lower + self.upper + self.number + self.symbol

        self.lang = "EN"
        self.length = 8

        if os.name == "posix":
            self.rows, self.columns = os.popen("stty size", "r").read().split()
        else:
            self.rows, self.columns = 30, 100

    def select_length(self):
        if self.lang == "EN":
            length = input(
                f"{colors.green}Enter password length (default: 8): {colors.gray}")
        elif self.lang == "TR":
            length = input(
                f"{colors.green}Şifre uzunluğunu girin (varsayılan: 8): {colors.gray}")

        if length is None or length == "":
            self.length = 8
        else:
            self.length = int(length)

    def generate(self, length):
        all_listed = list(
            self.all)

        random.shuffle(
            all_listed)

        password = random.choices(all_listed, k=length)
        password = "".join(password)

        return password

    def main(self):
        banner = ("""{}
____                                     _
|  _ \ __ _ ___ _____      _____  _ __ __| |
| |_) / _` / __/ __\ \ /\ / / _ \| '__/ _` |{}
|  __/ (_| \__ \__ \\\ V  V / (_) | | | (_| |
|_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_|{}

  ____                           _
 / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __
| |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|{}
| |_| |  __/ | | |  __/ | | (_| | || (_) | |
 \____|\___|_| |_|\___|_|  \__,_|\__\___/|_|
        {}""".format(colors.blue, colors.red, colors.blue, colors.green, colors.endc))

        print(banner)

        print(f"{colors.white}Please enter a language")
        print(f"{colors.white}Lütfen bir dil girin\n")

        lang = input(f"{colors.green}[EN] English [TR] Türkçe: {colors.gray}")

        if lang.lower() == "tr" or lang.lower() == "türkçe":
            self.lang = "TR"
        elif lang.lower() == "en" or lang.lower() == "english":
            self.lang = "EN"

        print(f"{colors.gray}-" * int(self.columns))

        self.select_length()

        if int(self.length) < 8:
            if self.lang == "EN":
                print(
                    f"{colors.red}Password length cannot be lower than 8 characters!")
            elif self.lang == "TR":
                print(f"{colors.red}Şifre 8 uzunluğu karakterden az olamaz!")

            self.select_length()

        password = self.generate(self.length)

        time.sleep(1)

        if self.lang == "EN":
            print(
                f"{colors.green}Your generated password is: {colors.gray}{password}{colors.endc}")
        elif self.lang == "TR":
            print(
                f"{colors.green}Oluşturulan şifreniz: {colors.gray}{password}{colors.endc}")

        sys.exit(0)


def signal_handler(sig, frame):
    sys.exit(0)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)

    generator = PasswordGenerator()
    generator.main()

    signal.pause()
