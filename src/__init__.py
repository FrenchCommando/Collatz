from colorama import init
from termcolor import colored

# use Colorama to make Termcolor work on Windows too
init()


def red(text, **kwargs):
    print(colored(text=text, color="red"), **kwargs)


def green(text, **kwargs):
    print(colored(text=text, color="green"), **kwargs)


def magenta(text, **kwargs):
    print(colored(text=text, color="magenta"), **kwargs)


def cyan(text, **kwargs):
    print(colored(text=text, color="cyan"), **kwargs)


def yellow(text, **kwargs):
    print(colored(text=text, color="yellow"), **kwargs)
