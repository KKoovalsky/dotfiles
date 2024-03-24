# Dotfiles

## To install

### Apps

* Rupa/Z: https://github.com/rupa/z
* Neovim; download and run:
```
z Down
tar -xf nvim-linux64.tar.gz
mv nvim-linux64 ~/.local/nvim.app
ln -s ~/.local/nvim.app/bin/nvim ~/.local/bin/nvim
sudo update-alternatives --install /usr/bin/vim vim ~/.local/bin/nvim 20
sudo update-alternatives --config vim
```
* Kitty and its [desktop integration](https://sw.kovidgoyal.net/kitty/binary/#desktop-integration-on-linux), and:
```
sudo update-alternatives --install /usr/bin/x-terminal-emulator x-terminal-emulator ~/.local/bin/kitty 10
sudo update-alternatives --config x-terminal-emulator
```
* FantasqueSansMono NerdFont: https://www.nerdfonts.com/

## Misc

* Universal ctags https://github.com/universal-ctags/ctags
* bash-language-server
* flake8

## Paths

```
# Kitty config
ln -s $(pwd)/kitty.conf ~/.config/kitty/kitty.conf

# Kitty dimmer
mkdir -p ~/.config/kitty
ln -s $(pwd)/kitty_dim_inactive.py ~/.config/kitty/kitty_dim_inactive.py

# Kitty themes
git clone --depth 1 https://github.com/dexpota/kitty-themes.git ~/.config/kitty/kitty-themes

# Neovim config
git clone git@github.com:KKoovalsky/kickstart.nvim.git ~/.config/nvim

# Kitty
ln -s ~/.local/kitty.app/bin/kitty ~/.local/bin/kitty

# Starship
export BIN_DIR=~/.local/bin && curl -fsSL https://starship.rs/install.sh | sh
# Put:
# eval "$(starship init bash)" to ~/.bashrc
```

* Vim custom C++ helpers: `ln -s ~/Workspace/Dotfiles/vim/pythonx ~/.vim/pythonx`
* Ultisnips: `mkdir ~/.vim/Ultisnips && ln -s ~/Workspace/Dotfiles/vim/UltiSnips/c.snippets ~/.vim/Ultisnips/c.snippets`
* AsyncTasks - `~/.vim/tasks.ini`
