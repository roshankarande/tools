
## References
 - [Cuda Installation for MS Windows](https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/index.html)
 - [Cuda for WSL ](https://docs.nvidia.com/cuda/wsl-user-guide/contents.html)
 - [Cuda for WSL](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/#prepare-wsl)

 - [Downloads](https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=WSL-Ubuntu&target_version=2.0&target_type=deb_local)

## Prerequisites / Helpful
 - [Install cpu-z](https://www.cpuid.com/softwares/cpu-z.html)


## Installation Instructions

/// warning

Remember! Compatibility is Everything...

Hardware :: Cuda Version :: GCC / G++ Version (should all be compatible with each other)
///


```sh
# THIS WORKS!!
wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-keyring_1.1-1_all.deb
sudo dpkg -i cuda-keyring_1.1-1_all.deb

sudo apt-get update
sudo apt-get install cuda-toolkit
# sudo apt install nvidia-cuda-toolkit  # see if it works without this ... should work
https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#post-installation-actions

# SET Environment Variables
# .bashrc
export PATH=/usr/local/cuda-12.4/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda-12.4/lib64

```

```
nvidia-smi
```