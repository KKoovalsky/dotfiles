# Dotfiles

## To install

* Neovim config: `git clone git@github.com:KKoovalsky/kickstart.nvim.git ~/.config/nvim`
* FantasqueSansMono NerdFont: https://www.nerdfonts.com/
* Universal ctags https://github.com/universal-ctags/ctags
* kitty themes: `git clone --depth 1 https://github.com/dexpota/kitty-themes.git ~/.config/kitty/kitty-themes`
* neovim kickstart: `git clone https://github.com/nvim-lua/kickstart.nvim.git "${XDG_CONFIG_HOME:-$HOME/.config}"/nvim`
* starship: `curl -fsSL https://starship.rs/install.sh | bash` and `eval "$(starship init bash)"` to `~/.bashrc`
* bash-language-server
* flake8

## Paths

* Kitty - `~./config/kitty/kitty.conf`
* Kitty dimmer - `~/.config/kitty/kitty_dim_inactive.py`
* Vim custom C++ helpers: `ln -s ~/Workspace/Dotfiles/vim/pythonx ~/.vim/pythonx`
* Ultisnips: `mkdir ~/.vim/Ultisnips && ln -s ~/Workspace/Dotfiles/vim/UltiSnips/c.snippets ~/.vim/Ultisnips/c.snippets`
* AsyncTasks - `~/.vim/tasks.ini`
