
## Running on the dataset

```
cd C:\Users\admin\Desktop\target\genie\demo
```

```
python ./benchmark.py --runs 1 --backend "npu" --verbose "true" --dataset "dataset.json"
```

```
python ./benchmark.py --runs 1 --backend "cpu" --verbose "true" --dataset "dataset.json"
```


## Giving prompts explicitly

```
python ./benchmark.py --runs 1 --backend "cpu" --verbose "true" --prompt "What is the capital of America"
```


```
python ./benchmark.py --runs 1 --backend "npu" --verbose "true" --prompt "What is the capital of America"
```
