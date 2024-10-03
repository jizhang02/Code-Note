# Insatall Tensorflow 2.12, CUDA 12 on WSL
### Install CUDA Toolkit and CuDNN
0. Make sure `nvidia-smi` worked after installing the NVIDIA GPU driver
1. `conda install -c nvidia cuda-toolkit` See [https://anaconda.org/nvidia/cuda-toolkit](https://anaconda.org/nvidia/cuda-toolkit)
2. `pip install nvidia-cudnn-cu12` See [https://pypi.org/project/nvidia-cudnn-cu12/](https://pypi.org/project/nvidia-cudnn-cu12/)

### Configure system paths at terminal
0. `mkdir -p $CONDA_PREFIX/etc/conda/activate.d`
1. `echo 'CUDNN_PATH=$(dirname $(python -c "import nvidia.cudnn;print(nvidia.cudnn.__file__)"))' >> $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh`
2. `echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/:$CUDNN_PATH/lib' >> $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh`
3. `source $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh`

### Install Tensorflow
0. `pip install --upgrade pip`
1. `pip install tensorflow==2.12.*`

### Test
```
import tensorflow as tf
print(tf.__version__)
print(tf.test.is_built_with_cuda()) # check if CUDA is used
print(tf.config.list_physical_devices('GPU')) # show GPU numbers
print(tf.test.is_gpu_available(cuda_only=False, min_cuda_compute_capability=None)) # check if GPU is available
```
