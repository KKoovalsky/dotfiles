set nocompatible              " be iMproved, required
filetype off                  " required

" Set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

" Let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'
Plugin 'Valloric/YouCompleteMe'
Plugin 'rhysd/vim-clang-format'
Plugin 'honza/vim-snippets'
Plugin 'SirVer/ultisnips'
Plugin 'vim-scripts/bash-support.vim'
Plugin 'vim-scripts/bats.vim'
Plugin 'kawaz/batscheck.vim'
Plugin 'vim-syntastic/syntastic'
Plugin 'tomtom/tcomment_vim'
Plugin 'machakann/vim-highlightedyank'
Plugin 'itchyny/lightline.vim'
Plugin 'majutsushi/tagbar'
Plugin 'ctrlpvim/ctrlp.vim'
Plugin 'tpope/vim-fugitive'
Plugin 'skywind3000/asyncrun.vim'
Plugin 'skywind3000/asynctasks.vim'
Plugin 'tell-k/vim-autopep8'
Plugin 'ludovicchabant/vim-gutentags'
Plugin 'dracula/vim', { 'name': 'dracula' }
Plugin 'francoiscabrol/ranger.vim'

" All of Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required
" To ignore plugin indent changes, instead use:
"filetype plugin on
"
" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line

set exrc
set secure

set tabstop=8
set softtabstop=0
set expandtab
set shiftwidth=4
set smarttab

:imap jk <Esc>

" Set this shortcuts to easily navigate through panes
nnoremap <c-j> <c-w><c-j>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>

" Save file on Ctrl-s
:nmap <C-s> :w<CR>
:imap <C-s> <Esc>:w<CR>

" Copy and paste on Ctrl-c and Ctrl-v
:vnoremap <C-c> "+y 
:inoremap <C-v> <C-o>"+p

" Map Ctrl-E for file explorer
:map <C-e> :Ranger<CR>

" File explorer customization
let g:netrw_banner = 0
let g:netrw_liststyle = 3

" Tab navigation like Firefox.
nnoremap <C-t> :tabnew<CR>:Explore<CR>
inoremap <C-t> <Esc>:tabnew<CR>:Explore<CR>

" Show me line numbers for better navigataion and debugging
set number
" Set its width
set numberwidth=2
" Enable 256 color palette
set t_Co=256

:colorscheme dracula
" Set colors for the bar
highlight LineNr term=bold cterm=NONE ctermfg=yellow ctermbg=darkgrey gui=NONE guifg=DarkGrey guibg=NONE

" Add vertical rule
set colorcolumn=80,120
highlight ColorColumn ctermbg=240

" UltiSnips shortcuts config
let g:UltiSnipsExpandTrigger="<c-k>"
let g:UltiSnipsJumpForwardTrigger="<c-m>"
let g:UltiSnipsJumpBackwardTrigger="<c-b>"
let g:UltiSnipsListSnippets="<c-n>"

let g:BASH_Ctrl_j="<c-p>"

" Set this shortcuts to easily navigate through panes
nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>

" Syntastic configuration
set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*
let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 0
let g:syntastic_check_on_open = 0
let g:syntastic_check_on_wq = 0
let g:syntastic_python_checkers=['flake8']

let g:ycm_extra_conf_globlist = ['~/.vim/*','~/Workspace/AgriWatch/*','~/Workspace/Dynks*','~/Workspace/Blinker*','~/Workspace/Therm*','~/Workspace/Magnetoblinker*','~/Workspace/Beeblinker*', '~/Workspace/BeeBlinker*', '~/Workspace/LivyPro*',]
let g:ycm_max_diagnostics_to_display = 1000
let g:ycm_complete_in_comments = 1
let g:ycm_complete_in_strings = 1
let g:ycm_collect_identifiers_from_comments_and_strings = 1
let g:ycm_seed_identifiers_with_syntax = 1
let g:ycm_add_preview_to_completeopt = 1
let g:ycm_show_diagnostics_ui = 1
let g:ycm_collect_identifiers_from_tags_files = 1
let g:ycm_always_populate_location_list = 1

" :nmap <c-i> :YcmCompleter GoToInclude<CR>
:nmap <F3> :YcmCompleter GoToDefinition<CR>
:nmap <c-d> :YcmCompleter GoToDeclaration<CR>

" Highlight yanked region with timeout
let g:highlightedyank_highlight_duration = 2000
hi HighlightedyankRegion cterm=reverse gui=reverse ctermfg=187

" Highlight search result
:set hlsearch

" Show filename in statusline
:set statusline=%f

" Show character count in visual mode
:set showcmd

" For the lightline plugin
set laststatus=2
let g:lightline = {
      \ 'colorscheme': 'powerline',
      \ 'active': {
      \   'left': [ [ 'mode', 'paste' ],
      \             [ 'gitbranch', 'readonly', 'filename', 'modified', 'absolutepath' ] ]
      \ },
      \ 'component_function': {
      \   'gitbranch': 'fugitive#head'
      \ },
      \ }

" Map toggle Tagbar
nmap <F8> :TagbarToggle<CR>

" AsyncRun configuration
:let g:asyncrun_open = 14
:let g:asyncrun_bell = 10
nmap <F10> :AsyncRun 

" =====================================================================================================================
" Autopep config
" =====================================================================================================================
let g:autopep8_disable_show_diff=1

" =====================================================================================================================
" Ranger config
" =====================================================================================================================

" =====================================================================================================================
" Ctrlp config
" =====================================================================================================================
let g:ctrlp_root_markers = [ '.project-root' ]

" =====================================================================================================================
" MACROS FOR C PROGRAMMING
" =====================================================================================================================

" Macros for fast unit tests in C handling
let @q = 'V}ky/EXECUT}kkp}kklllllllllllcRUN_TEST(jkV}kk:s/()/)/g/DECLARATION OF THE TEST CASESjjVjjjy/DEFINITION OF THE TESTjpV}:s/;/{}\r/g:ClangFormat'
let @g = 'V}k"ky/EXECUTION}kk"kp}kktUcRUN_TEST(jkV}:s/()/)/g/DEFINITION OF PRIVATE FUNkk"kPV}:s/;/{}\r/g:ClangFormat:noh'

" Macro which makes definitions of C functions from declarations
let @b = 'V}:s/;/{}\r/g:ClangFormat'

:set wildmenu

let g:gutentags_ctags_exclude = ['build*', 'gendocs', 'compile_commands.json']

py3 from cpp_helpers import * 
py3 from cpp_iface_finder import * 
py3 from cpp_file_navigator import * 
py3 from cpp_file_finder import * 
py3 from cpp_method_definition_maker import * 
py3 from unity_tests_helpers import * 
py3 from cpp_word_replacer_across_project import * 

function MakeCppClassFiles(name_no_extension)
    let path = b:netrw_curdir . '/' . a:name_no_extension
    let header_path = path . '.hpp'
    let source_path = path . '.cpp'
    execute 'args ' . header_path . ' ' source_path . ' | vert all'
    startinsert
endfunction

function FindOccurences(symbol)
    execute ':AsyncRun git grep --untracked -rne ' . a:symbol . ' -- "*.c" "*.cpp" "*.h" "*.hpp"'
endfunction

function FindOccurencesOfSymbolUnderCursor()
    let current_word = expand("<cword>")
    call FindOccurences(current_word)
endfunction

function ReplaceOccurencesOfWordUnderCursor(replacement)
    let current_word = expand("<cword>")
    call py3eval('replace_word_project_wise("' . current_word . '", "' . a:replacement . '")')
endfunction

function ReplaceProjectWise(searched_string, replacement)
    call py3eval('replace_word_project_wise("' . a:searched_string . '", "' . a:replacement . '")')
endfunction

function GoToCorrespondingSourceOrHeaderFile()
    let current_file = expand("%:t")
    let corresponding_file = py3eval('find_corresponding_source_or_header_file("' . current_file . '")')
    execute "tab drop" corresponding_file
endfunction

function CreateMethodDefinition()
    let method_definition_snippet = py3eval('create_snippet_with_method_definition_for_method_under_cursor()')
    call GoToCorrespondingSourceOrHeaderFile()
    norm! Go
    call UltiSnips#Anon(method_definition_snippet)
endfunction()

function RenameCurrentWord(replacement)
    let current_word = expand("<cword>")
    execute '%s/' . current_word . '/' . a:replacement . '/g'
endfunction()

command -nargs=1 MakeCppClassFiles call MakeCppClassFiles(<f-args>)
command FillCorrespondingCppClassSourceFile py3 fill_corresponding_cpp_class_source_file()
command FindOccurences call FindOccurencesOfSymbolUnderCursor()
command -nargs=1 SearchOccurences call FindOccurences(<f-args>)
command FindReferences YcmCompleter GoToReferences
command ImplementInterface py3 implement_interface() 
command OpenCorrespondingSourceOrHeaderFile call GoToCorrespondingSourceOrHeaderFile() 
command CreateMethodDefinition call CreateMethodDefinition()
command -nargs=1 UnityTestCreate py3 create_unity_test(<f-args>)
command -nargs=1 ReplaceOccurencesOfWordUnderCursor call ReplaceOccurencesOfWordUnderCursor(<f-args>)
command -nargs=+ ReplaceProjectWise call ReplaceProjectWise(<f-args>)
command -nargs=1 RenameCurrentWord call RenameCurrentWord(<f-args>)

:augroup autotagbar
:       autocmd! 
:       au BufEnter *.py,*.c,*.cpp,*.h,*.hpp :TagbarOpen
:augroup END
