#!/usr/bin/env python3


import os
import re
import click

theme = {"dark": "Dracula", "light": "Github"}


@click.command()
@click.argument("mode", type=click.Choice(["dark", "light"]))
def main(mode):
    set_terminator_config(mode)


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
    theme_name = theme[mode]
    res = re.sub(regex, r"\1{}".format(theme_name), config)
    with open(path, "w") as f:
        f.write(res)


if __name__ == "__main__":
    main()
