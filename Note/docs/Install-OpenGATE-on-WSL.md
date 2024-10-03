# Install OpenGATE
## Install OpenGATE on WSL
### Preface
#### 🧐 What is OpenGATE?
Geant4 is a general particle transport simulation tool, while GATE is a specific application based on Geant4, focusing on simulation and simulation in the field of nuclear medicine. OpenGATE is based on GATE, which is written in Python language, it is a work in progress.

#### 🧐 What is WSL?
Windows Subsystem Linux (WSL). We can regard this system as a duo system (Windows and Linux) or a virtual machine, anyway, it's convenient to use both two systems.

### Installation

1. Install WSL: open CMD, input `wsl --install`, for detail, see [Official tutorial](https://learn.microsoft.com/en-us/windows/wsl/install#Overview) .
2. Install Anaconda in WSL terminal: download the package on Win, then copy to the WSL dirctory like `home/user/`, then install it by `bash package.sh`, then following the instructions.
3. Create conda environment: input  `conda create -n gate python=3.9`
4. Install OpenGATE in the `gate` environment: `pip install -pre opengate`

### Test
5. Test: input `opengate_tests` install the missing lib according to the instructions, mainly `.so` files. e.g. `conda install -c conda-forge libstdcxx-ng` `conda install qt=5` Also pay attention to step 6.
6. Declare path `export PATH="/opt/conda/envs/gate/bin:$PATH"` in the terminal(temporal) or write in the `~/.bashrc`(permanent), then `source ~/.bashrc`, to make it into effect.

## Install OpenGATE on Windows

### Installation

1. Install miniconda or Anaconda on Windows
2. Create conda environment: input  `conda create -n gate python=3.9/3.10/3.11`
3. Install OpenGATE in the `gate` environment: `pip install -pre opengate` `-pre` means the latest version    
Note: if one wants to update the OpenGATE, delete the gate environment and create new conda env then install as step 2. Otherwise error happens~
### Test
4. Test: input `opengate_info`, some missing data will automatically download. And in Windows, no need to declare path.
