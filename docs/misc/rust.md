# Install

* [binstall](https://github.com/cargo-bins/cargo-binstall)
/// details | 👀 Instructions

```sh
# linux
curl -L --proto '=https' --tlsv1.2 -sSf https://raw.githubusercontent.com/cargo-bins/cargo-binstall/main/install-from-binstall-release.sh | bash

# windows
Set-ExecutionPolicy Unrestricted -Scope Process; iex (iwr "https://raw.githubusercontent.com/cargo-bins/cargo-binstall/main/install-from-binstall-release.ps1").Content
```
///


* [uv](https://github.com/astral-sh/uv) 
/// details | 👀 Instructions

```sh
# linux
curl -LsSf https://astral.sh/uv/install.sh | sh 

# windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```
///


* [evcxr_repl](https://github.com/evcxr/evcxr)
* [evcxr_jupyter](https://github.com/evcxr/evcxr)

/// details | 👀 Instructions

//// tab | install
```sh
rustup component add rust-src
sudo apt install jupyter-notebook
cargo binstall evcxr_jupyter
cargo binstall evcxr_repl
evcxr_jupyter --install
```
////

//// tab | config
```sh
jupyter notebook --generate-config

# open it and add the following
 c.NotebookApp.token = ''
 c.NotebookApp.password = u''
# c.NotebookApp.open_browser = True
# c.NotebookApp.ip = 'localhost'
```
////

//// tab | debug
```sh
# jupyter notebook mode
jupyter notebook --no-browser
# either via browser or via vscode - manually enter the url


# repl mode
evcxr
>> :dep num_cpus
    Compiling num_cpus v1.16.0
>> num_cpus::get()
12

```
////


//// tab | todo
```sh
# TODO :: Create a docker container for evcrx and jupyter
# ADD :: python as well to it

# https://hub.docker.com/r/hgfkeep/rust-jupyter
# or docker compose ... and stuff for evcxr_repl // especially jupyter

version: '3.8'
services:
  some_name:
    ports: ['8888:8888']  # docker run -p option
    image: jupyter/minimal-notebook:57f8546c0386
    command: start-notebook.sh --NotebookApp.token=''

```
////
///


* rustup doc - offline doc
/// details | 👀 Instructions

```sh
# wsl
sudo apt-get install -y xdg-utils # https://github.com/4U6U57/wsl-open

# .bashrc :: add :: 
export BROWSER="/mnt/c/Program Files/Google/Chrome/Application/chrome.exe"
rustup doc # should work now
```
///

