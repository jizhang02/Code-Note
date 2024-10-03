# CuPy --accelerated Numpy


### Install CuPy
CuPy is a NumPy compatible library for GPU acceleration. If your computing tasks require a lot of matrix operations and you have GPU resources available, Cupy can help you accelerate these operations.

install steps: 
* `python -m pip install -U setuptools pip`
* `pip install cupy-cuda12x`
  
For more details: see [https://docs.cupy.dev/en/stable/install.html](https://docs.cupy.dev/en/stable/install.html)
### Install CUDA
* install: go to the official website [https://developer.nvidia.com/cuda-downloads](https://developer.nvidia.com/cuda-downloads)
* check:  `nvcc --version`
### Example
```
import cupy as cp
from cupyx.scipy.signal import convolve2d
from cupyx.scipy import ndimage
```
almost all the numpy functions are compatible to cupy.
### Docker
Use NVIDIA Container Toolkit to run CuPy image with GPU.    
☑️ Strategy 1: `docker run --gpus all -it cupy/cupy /bin/bash`  
☑️ Strategy 2: `docker run --gpus all -it cupy/cupy /usr/bin/python3`   
☑️ Strategy 3: use Singularity to build a `sif` image   
   * `sudo singularity -d build --sandbox sandbox_cupy/ docker://cupy/cupy`
   * `sudo singularity shell --writable sandbox_cupy/`
   * `pip install pythonlibs` pythonlibs that you need
   * `sudo singularity build cupy.sif sandbox_cupy/`

