Install

```
evcxr_repl - A Rust REPL
evcxr - Common library shared by the above crates, may be useful for other purposes.


https://github.com/evcxr/evcxr

rustup component add rust-src
sudo apt install jupyter-notebook

cargo binstall evcxr_jupyter
# cargo binstall evcxr  --- install only if need be
cargo binstall evcxr_repl
evcxr_jupyter --install

jupyter notebook --no-browser # run this and then open browser or also in vscode will have to enter the url


# TRY THIS OUT
https://github.com/evcxr/evcxr/blob/main/evcxr_jupyter/samples/evcxr_jupyter_tour.ipynb

# if you want to start with vscode... manually start juypter notebook ... and then enter the url while selecting kernel
```


```
jupyter notebook --generate-config

# open it and add the following

 c.NotebookApp.token = ''
 c.NotebookApp.password = u''
# c.NotebookApp.open_browser = True
# c.NotebookApp.ip = 'localhost'

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


```rust
evcxr
>> :dep num_cpus
    Compiling num_cpus v1.16.0
>> num_cpus::get()
12

```
