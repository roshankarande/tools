```
You should be able to use any of the listed mirrors by adding a line to your /etc/apt/sources.list like this:
deb http://cz.archive.ubuntu.com/ubuntu noble main universe
sudo apt update
sudo apt install gcc-14
sudo apt install g++-14
gcc --version
g++ --version

```

```
https://www.cpuid.com/softwares/cpu-z.html
https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/index.html
https://docs.nvidia.com/cuda/wsl-user-guide/contents.html


https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=WSL-Ubuntu&target_version=2.0&target_type=deb_local
https://docs.nvidia.com/cuda/cuda-installation-guide-linux/#meta-packages
```

```
nvidia-smi
https://docs.nvidia.com/cuda/cuda-installation-guide-linux/#prepare-wsl
```

https://learn.microsoft.com/en-us/windows/wsl/basic-commands


```Works

https://docs.nvidia.com/cuda/cuda-installation-guide-linux/#prepare-wsl


wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-keyring_1.1-1_all.deb
sudo dpkg -i cuda-keyring_1.1-1_all.deb

sudo apt-get update
sudo apt-get install cuda-toolkit

sudo apt install nvidia-cuda-toolkit


```
