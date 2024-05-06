# Dotfiles

## To install

### Apps

* Basic:
```
sudo apt update
sudo apt install vim gcc g++ cmake git nodejs
```

* Rupa/Z: https://github.com/rupa/z
```
mkdir ~/Workspace
git clone https://github.com/rupa/z.git ~/Workspace/RupaZ
# Append to ~/.bashrc:
# . ~/Workspace/RupaZ/z.sh
```

* Neovim; download and run:
```
z Down
tar -xf nvim-linux64.tar.gz
mv nvim-linux64 ~/.local/nvim.app
mkdir -p ~/.local/bin
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
```
z Down
mkdir fonts
unzip FantasqueSansMono.zip -d fonts
cd fonts
mkdir -p ~/.local/share/fonts
mv *.ttf ~/.local/share/fonts/.
fc-cache -f -v
```

## Misc (_not necessary_)

* Universal ctags https://github.com/universal-ctags/ctags
* bash-language-server
* flake8
* clangd (_not really needed_):
```
# Download LLVM and ...
cd <LLVM>
mkdir build && cd build
cmake -G Ninja -DLLVM_ENABLE_PROJECTS="clang;clang-tools-extra" -DCMAKE_BUILD_TYPE=Release ../llvm
# Takes a while ...
cmake --build . --target clangd
export VERSION=<version>
cmake -DCMAKE_INSTALL_PREFIX=~/.local/clangd_${VERSION} ../llvm
cmake --install . --component clangd
sudo update-alternatives --install /usr/bin/clangd clangd ~/.local/clangd_${VERSION}/bin/clangd 20
sudo update-alternatives --config clangd
```

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

# Use neovim as git editor
git config --global core.editor nvim
```

### To be ported  ...

* Vim custom C++ helpers: `ln -s ~/Workspace/Dotfiles/vim/pythonx ~/.vim/pythonx`
* Ultisnips: `mkdir ~/.vim/Ultisnips && ln -s ~/Workspace/Dotfiles/vim/UltiSnips/c.snippets ~/.vim/Ultisnips/c.snippets`
