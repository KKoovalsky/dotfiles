#!/usr/bin/env python3


import os
import re
import click

theme = {
    "dark": (
        "Dracula",
        "rgb(200, 200, 200)",
        "default",
        "archery",
        "powerline",
    ),
    "light": (  #
        "Github",
        "rgb(20, 20, 20)",
        "light",
        "PaperColor",
        "PaperColor",
    ),
}


@click.command()
@click.argument("mode", type=click.Choice(["dark", "light"]))
def main(mode):
    set_terminator_config(mode)
    set_terminator_border_color(mode)
    set_powerline_colortheme(mode)
    set_vim_colorscheme(mode)


def set_terminator_config(mode):
    path = os.path.expanduser("~/.config/terminator/config")
    with open(path) as f:
        config = f.read()
    regex = re.compile(
        r"(\[layouts\]\s+\[\[default\]\]\s+\[\[\[window0\]\]\]\s+type ="
        r" Window\s+parent ="
        r' ""\s+\[\[\[child1\]\]\]\s+type = Terminal\s+parent ='
        r" window0\s+profile ="
        r" )(\w+)"
    )
    theme_name = theme[mode][0]
    res = re.sub(regex, r"\1{}".format(theme_name), config)
    with open(path, "w") as f:
        f.write(res)


def set_terminator_border_color(mode):
    in_file_path = os.path.join(get_dotfiles_path(), "gtk.css.in")
    out_file_path = os.path.join(get_dotfiles_path(), "gtk.css")
    with open(in_file_path) as f:
        gtk_css_in = f.read()
    border_color = theme[mode][1]
    res = gtk_css_in.replace("TERMINATOR_SEPARATOR_COLOR", border_color)
    with open(out_file_path, "w") as f:
        f.write(res)


def set_powerline_colortheme(mode):
    powerline_config_path = os.path.join(
        get_dotfiles_path(), "powerline", "config.json"
    )
    with open(powerline_config_path) as f:
        config = f.read()
    regex = re.compile(r'("colorscheme": )"\w+"')
    theme_name = theme[mode][2]
    res = re.sub(regex, r'\1"{}"'.format(theme_name), config)
    with open(powerline_config_path, "w") as f:
        f.write(res)


def set_vim_colorscheme(mode):
    vimrc_path = os.path.join(get_dotfiles_path(), "vimrc")
    with open(vimrc_path) as f:
        config = f.read()
    global_scheme_re = re.compile(r":colorscheme \w+")
    global_scheme = theme[mode][3]
    res = re.sub(
        global_scheme_re, r":colorscheme {}".format(global_scheme), config
    )
    lightline_scheme_re = re.compile(r"'colorscheme': '\w+'")
    lightline_scheme = theme[mode][4]
    res = re.sub(
        lightline_scheme_re,
        r"'colorscheme': '{}'".format(lightline_scheme),
        res,
    )
    with open(vimrc_path, "w") as f:
        f.write(res)


def get_dotfiles_path():
    return os.path.join(os.path.dirname(__file__), "..")


if __name__ == "__main__":
    main()
