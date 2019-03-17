# py-system-check
Python 3 script for system checks

## Requirements

* [Python 3](https://www.python.org/)
* [PyYAML](https://pyyaml.org/)

    ```bash
    $ pip install PyYAML
    ```

## Installation

Create configuration file:

```bash
$ mv config.yml.dist config.yml
```

## Configuration

You can configure your commands in `config.yml` file.

## Execution

* Install script on target system
* Run check

```bash
$ python3 check.py
```