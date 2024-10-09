call plug#begin('~/.vim/plugged')
Plug 'scrooloose/nerdtree'
Plug 'vim-airline/vim-airline'
Plug 'valloric/youcompleteme'
call plug#end()
map <F2> :NERDTreeToggle<CR>

imap jk <Esc>
nmap <Space> :


"切换窗口
map <C-j> <C-W>j
map <C-k> <C-W>k
map <C-h> <C-W>h
map <C-l> <C-W>l


syntax on  "语法高亮
set number "显示作侧行
set numberwidth=1
"set relativenumber "其他行都为相对于该行的相对行号
set showmode "在底部显示当前模式(insert,normal)等
set showcmd  "在命令模式下显示指令
set t_Co=256 "启用256色
set autoindent "按下回车键后，下一行的缩进会自动跟上一行的缩进保持一致
set tabstop=4 "按下 Tab 键时，Vim 显示的空格数
set expandtab "由于 Tab 键在不同的编辑器缩进不一致，该设置自动将 Tab 转为空格
set shiftwidth=4 "在文本上按下>>（增加一级缩进）、<<（取消一级缩进）或者==（取消全部缩进）时，每一级的字符数
set cursorline "高亮当前光标所在行
set textwidth=80 "设置行宽，即一行显示多少个字符
set wrap "自动折行，即太长的行分成几行显示
set scrolloff=5 "垂直滚动时，光标距离顶部/底部的位置（单位：行）
"set sidescrolloff=15 "水平滚动时，光标距离行首或行尾的位置（单位：字符）。该配置在不折行时比较有用
set laststatus=2 "是否显示状态栏。0 表示不显示，1 表示只在多窗口时显示，2 表示显示
set ruler "在状态栏显示光标的当前位置
set showmatch "光标遇到圆括号、方括号、大括号时，自动高亮对应的另一个圆括号、方括号和大括号
set hlsearch "搜索时，高亮显示匹配结果
set incsearch "输入搜索模式时，每输入一个字符，就自动跳到第一个匹配的结果
set ignorecase "搜索时忽略大小写
set smartcase "如果同时打开了ignorecase，那么对于只有一个大写字母的搜索词，将大小写敏感；其他情况都是大小写不敏感。比如，搜索Test时，将不匹配test；搜索test时，将匹配Test
set autochdir "自动切换工作目录。这主要用在一个 Vim 会话之中打开多个文件的情况，默认的工作目录是打开的第一个文件的目录。该配置可以将工作目录自动切换到，正在编辑的文件的目录
set nobackup  "不创建备份文件。默认情况下，文件保存时，会额外创建一个备份文件，它的文件名是在原文件名的末尾，再添加一个波浪号（〜）
set swapfile  "创建交换文件。交换文件主要用于系统崩溃时恢复文件，文件名的开头是.、结尾是.swp
set undofile  "保留撤销历史到一个文件里
"set backupdir=~/.vim/.backup//      "设置备份文件、交换文件、操作历史文件的保存位置。
set directory=~/.vim/.swp//         "结尾的//表示生成的文件名带有绝对路径，
set undodir=~/.vim/.undo//          "路径中用%替换目录分隔符，这样可以防止文件重名。
set noerrorbells  "出错时，不要发出声响
set visualbell    "出错时，发出视觉提示，通常是屏幕闪烁
set history=1000  "Vim 需要记住多少次历史操作
set autoread    "打开文件监视。如果在编辑过程中文件发生外部改变（比如被别的编辑器编辑了），就会发出提示
set listchars=tab:»■,trail:■    "如果行尾有多余的空格（包括 Tab 键），
set list                        "该配置将让这些空格显示成可见的小方块
set wildmenu                    "命令模式下，底部操作指令按下 Tab 键自动补全。
set wildmode=longest:list,full  "第一次按下 Tab，会显示所有匹配的操作指令的清单；第二次按下 Tab，会依次选择各个指令
set clipboard=unnamed    "共享剪贴板



""""""新建.py文件时自动加上下面的内容"""""
func SetTitle()
call setline(2, "!/usr/bin/python")
call setline(1,"############################################################ File Name:".expand("%"))
call setline(3, "\> -*- coding=utf8 -*-")
call setline(4, "###################################################################################")
call setline(5, "\#     >@Author : quhongbin")
call setline(6, "\#     >@Created Time : ".strftime("%Y-%m-%d %H:%M:%S"))
call setline(7, "\#     >@Description : ")
call setline(8, "###################################################################################")
normal G
normal o
normal o
endfunc
autocmd bufnewfile *.py call SetTitle() 
