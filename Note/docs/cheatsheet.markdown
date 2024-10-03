### Odyssey in computer science
---
####  Pytorch
* `torch.cuda.is_available()` check cuda
* `tensorboard --logdir=/home/jing/python_code/DeepRT/torch/runs` use tensorboard web graph
* 
#### Conda
* `conda --version` check version
* `conda env list` exsisted environments
* `conda install python==3.6` install specific python
* `conda create -n name python=3.9` create a conda env
* `conda create -n newenv --clone oldenv` copy a conda env
* `conda remove -n envname --all` delete a conda env
* `conda activate envname` activate a conda env
* `conda deactivate` close a conda env
* export to another machone 
  * `conda env export > envname.yaml`
  * `conda env create -f envname.yaml`
#### Python
* `print(sys.version)` print python version
* `print(glob.glob("path/*.mhd"))` print files names
* ` files = os.listdir(path);    files.sort()` sort the files names
* `for x, y in zip(directory_image, directory_label):` double loop
* `print(f'text {variable:.3f}')` print in specific format
#### Terminal
* `hostname -I` ip address
* `ps` or `top` show running programs
* `sudo vi /etc/hostname` change hostname, remember to reboot
* `ps -ef | grep ssh` check ssh
* `python --version` check python version
* `nvidia-smi` check GPU info
* `nvidia-smi -L` check available GPU
* `htop` check memory
* `touch test.py` create a new file
* `vi test.py` edit a file
* `cd ~` come to home
* `bash xxx.sh` run .sh file
* `sudo vim /home/jing/.bashrc` modigy environment variables
* `export PATH=path1:path2: ...... :$PATH` add multiple variables
* `source ~/.bashrc` make it into effect
* `unset PYTORCH_CUDA_ALLOC_CONF` cancel the previous command
* `sudo apt-get update` update software
* `pip install opengate -U` update lib
* `sudo apt-get remove --auto-remove qtcreator` uninstall software
* `scp -r /datapath/* username@ip address:/savepath/` upload data to cluster
* `scp -r username@ip address:'/remotepath/file_{367..497}.root' savepath` batch download files to local
* `scp -r phantom*_atn_1.bin username@ip address:remotepath/` upload specific type files
* `ls -l . | egrep -c '^-'` check file numbers
* `ls -lh path/file_name` check file size 
* `ffmpeg -i input.mp3 -ss 00:01:00 -to 00:05:23.27 -c copy output.mp3` edit audio length
* `su root`, change to root user
* `su jing`, change to other user
* `sudo passwd root`, change password of root
* `passwd`, change password
* `watch -n 10 squeue -u jzhang`, watch slurm jobs every 10 seconds
* `df -h /`, check disk space
* `du -sh /home2/jzhang/`, check total data used of certain path
* `du /home2/jzhang/`, check detail data used of certain path
*  `tree -L 1`, show tree structure in 1 level
*  `tree -d`, show directory only
*  `tree -L 2 > structure.txt` export tree structure to file
*  `tree /A` in Windows, show tree structure with directory only
*  `tree` in Windows, similar as above
*  `tree /F` in Windows, show all information
#### WSL=Windows subsystom linux
* A good subsitute for vmware virtual machine.
* version ` wsl -l -v`
* `sudo apt-get install x11-apps ` to support visualization, `xeyes` for testing.
* in CMD, `ubuntu config --default-user jing or root`, change user or root user.
* in CMD, `wsl --shutdown`, shutdown the wsl system.
* in CMD, `wsl -l`, print info of OS.
  
#### Hybrid programming between python and C/C++
* Essence: python calls dynamic link libraries compiled by C/C++. e.g. convert the data types in python to those in c/c++, pass them to the compiled functions, and then convert returned parameters to the data types in python.
* C/C++ --> dynamic link library (Pybind11) <-- Python


#### LaTeX
adjust blank:

`\setlength{\abovedisplayskip}{3pt} `    
`\setlength{\belowdisplayskip}{3pt}`    
adjust the space between title and fig
`\setlength{\abovecaptionskip}{-0.2cm}`    
adjust the distance between title and the below context
`\setlength{\belowcaptionskip}{-1cm} `

```
\begin{equation}
\setlength{\abovedisplayskip}{3pt}
\setlength{\belowdisplayskip}{3pt}
y(t)=a(t)-b(t).
\end{equation}
```

table:    
`tabular*` can automatically adjust the width to fit the text.    
`{\textwidth}` width of column`{@{\extracolsep{\fill}} ll}` column setting    

```
\begin{table}[htbp]
\caption{Dataset}
\begin{tabular*}{\textwidth}{@{\extracolsep{\fill}} ll}
\toprule
data 1 & data 2 \\
\midrule
 1 &  2 \\
 3 &  4 \\
\bottomrule
\end{tabular*}
\end{table}
```
split a cell into two rows

```
\begin{tabular}[c]{@{}c@{}} part A \\ part B \end{tabular} 
```
