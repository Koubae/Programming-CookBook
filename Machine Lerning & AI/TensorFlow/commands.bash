# Install TensorFlow
pip install --upgrade tensorflow
# Verify Install 
python -c "import tensorflow as tf;print(tf.reduce_sum(tf.random.normal([1000, 1000])))"


# Install GPU (Ubuntu 20)
sudo apt update
sudo apt upgrade 


# StackOverflow : https://askubuntu.com/a/1303586/1166575
# https://askubuntu.com/a/1298131/1166575
# Source: https://dgpu-docs.intel.com/devices/iris-xe-max-graphics/index.html
apt install linux-oem-20.04 && sudo reboot 0

# Some more instructins (not tested) https://gist.github.com/ranr01/46617b1fd289b5782138f78faf7a0bcd

# Add NVIDIA package repositories
# https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu
# Note: For the Ubuntu version other than 18.04 or CPU architecture other than x86,
# replace `ubuntu1804` and/or `x86_64` as needed in the following URL.
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-keyring_1.0-1_all.deb
sudo dpkg -i cuda-keyring_1.0-1_all.deb
sudo apt-get update

# Install development and runtime libraries (~4GB)
# libnvinfer packages are optional, needed to support TensorRT inference.
sudo apt-get install --no-install-recommends \
    cuda-11-2 \
    libcudnn8=8.1.0.77-1+cuda11.2  \
    libcudnn8-dev=8.1.0.77-1+cuda11.2 \
    libnvinfer8=8.2.4-1+cuda11.4 \
    libnvinfer-dev=8.2.4-1+cuda11.4 \
    libnvinfer-plugin8=8.2.4-1+cuda11.4 \
    libnvinfer-plugin-dev=8.2.4-1+cuda11.4

sudo apt-get -y install cuda
sudo apt install nvidia-cuda-toolkit
# Add cuda to PATH
export PATH=/usr/local/cuda-11.2/bin/:${PATH}
 
# Reboot. Check that GPUs are visible using the command: nvidia-smi
nvidia-smi

# Run nvidia settings
nvidia-settings
sudo apt-get install linux-headers-`uname -r`

# https://www.tensorflow.org/install/docker
# Run Docker TensorFlow Container
docker pull tensorflow/tensorflow:latest  # Download latest stable image
docker run -it -p 8888:8888 tensorflow/tensorflow:latest-jupyter  # Start Jupyter server 