# Locust :: Load Testing

- [Website](https://locust.io/)
- [Source code](https://github.com/locustio/locust)
- [Docs](https://docs.locust.io/en/stable/installation.html)
- [config](https://docs.locust.io/en/stable/configuration.html)


## Basic Setup

```shell
pip install locust
locust --help
```

## Run locust
```shell
# headless mode -- preferred for speed
locust -f main.py --headless --users 10 --spawn-rate 1 --runtime 200s -H http://api-host

# normal mode -- preferred for interactivity -- browser based control
locust -f main.py --users 10 --spawn-rate 1 --runtime 200s -H http://api-host
```

## Code Snippets

/// details | 👀 Example

//// tab | Simple Example

```python
{!./docs_code/snippets/misc/locust_001.py!}
```

////

//// tab | Complex Example

```Python
{!./docs_code/snippets/misc/locust_002.py!}
```

////

///