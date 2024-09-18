import os
import sys
import time
from typing import Any


class View:
    def __init__(self, title: str) -> None:
        self.title: str = title

    def clear(self):
        os.system('cls||clear')

    def show_spinner(self, msg: str):
        spinner = ['|', '/', '-', '\\']
        for _ in range(3):
            for symbol in spinner:
                sys.stdout.write(f'\r{symbol} {msg}')
                sys.stdout.flush()
                time.sleep(0.1)

    def draw_line(self):
        print('————————————————————————')

    def message_error(self, message: str):
        print(f'[❗] - {message}')

    def enter_to_continue(self):
        while True:
            try:
                print('> Pressione \"enter\" para continuar', end=' ')
                if input() == '':
                    self.clear()
                    break
            except KeyboardInterrupt:
                exit(0)

    def custom_input(self, message:str, type: Any):
        while True:
            try:
                data = type(input(f'> {message}'))
                return data
            except KeyboardInterrupt:
                exit(0)
            except:
                self.message_error(message='Valor inválido')

    def confirm_input(self, message: str='') -> bool:
        while True:
            try:
                confirm = input(f'> {message} [y/n]: ')
                if confirm in 'y' or confirm in 'yes' or confirm in 'YES' or confirm in 'Y':
                    return True
                elif confirm in 'n' or confirm in 'no' or confirm in 'NO' or confirm in 'n':
                    return False
            except KeyboardInterrupt:
                exit(0)

    def menu_select_option(self, max_opt: int, min_opt: int):
        while True:
            try:
                opt = int(input(' > Escolha uma das opções acima: '))
                if opt < min_opt or opt > max_opt:
                    raise ValueError
                return opt
            except KeyboardInterrupt:
                exit(0)
            except:
                self.message_error(message='Opção inválida')

    def render(self) -> None:
        self.clear()
        print(f'———————————————————————— [ {self.title.upper()} ] ————————————————————————')
