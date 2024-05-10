# Locust :: Load Testing

- [Website](https://locust.io/)
- [Source code](https://github.com/locustio/locust)


## Basic Setup

```shell
pip install locust
locust --help
locust -f main.py --headless --users 10 --spawn-rate 1 --runtime 200s -H http://api-host
locust -f main.py --users 10 --spawn-rate 1 --runtime 200s -H http://api-host


```

* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.

## Code Blocks
``` py
import tensorflow as tf
```

``` py title="bubble_sort.py"
def bubble_sort(items):
    for i in range(len(items)):
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
```


``` yaml
theme:
  features:
    - content.code.annotate # (1)
```

1.  :man_raising_hand: I'm a code annotation! I can contain `code`, __formatted
    text__, images, ... basically anything that can be written in Markdown.


=== "C"

    ``` c
    #include <stdio.h>

    int main(void) {
      printf("Hello world!\n");
      return 0;
    }
    ```

=== "C++"

    ``` c++
    #include <iostream>

    int main(void) {
      std::cout << "Hello world!" << std::endl;
      return 0;
    }
    ```



/// details | 👀 Full file preview

<!-- //// tab | Python 3.10+ -->

```Python
{!./docs_code/snippets/tutorial_001.py!}
```

<!-- //// -->

<!-- //// tab | Python 3.7+

```Python
{!./docs_code/snippets/tutorial_002.py!}
```

//// -->

///