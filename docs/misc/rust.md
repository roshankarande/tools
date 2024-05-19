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

jupyter notebook # run this and then open browser or also in vscode will have to enter the url

```

```rust
evcxr
>> :dep num_cpus
    Compiling num_cpus v1.16.0
>> num_cpus::get()
12

```
