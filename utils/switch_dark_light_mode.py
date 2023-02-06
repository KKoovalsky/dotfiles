#!/usr/bin/env python3


import os
import re
import click

theme = {
    "dark": ("Dracula", "rgb(200, 200, 200)", "default"),
    "light": ("Github", "rgb(20, 20, 20)", "light"),
}


@click.command()
@click.argument("mode", type=click.Choice(["dark", "light"]))
def main(mode):
    set_terminator_config(mode)
    set_terminator_border_color(mode)
    set_powerline_colortheme(mode)


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
    gtk_css_path = os.path.join(get_dotfiles_path(), "gtk.css")
    regex = re.compile(
        r"(:root {\s+" r"--terminator-separator-color: )(.*)([\n\r])"
    )
    with open(gtk_css_path) as f:
        gtk_css = f.read()
    border_color = theme[mode][1]
    res = re.sub(regex, r"\1{}\3".format(border_color), gtk_css)
    with open(gtk_css_path, "w") as f:
        f.write(res)


def set_powerline_colortheme(mode):
    powerline_config_path = os.path.join(
        get_dotfiles_path(), "powerline", "config.json"
    )
    with open(powerline_config_path) as f:
        config = f.read()
    regex = re.compile(r'("colorscheme": )"(\w+)"')
    theme_name = theme[mode][2]
    res = re.sub(regex, r'\1"{}"'.format(theme_name), config)
    with open(powerline_config_path, "w") as f:
        f.write(res)


def get_dotfiles_path():
    return os.path.join(os.path.dirname(__file__), "..")


if __name__ == "__main__":
    main()
