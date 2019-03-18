# py-system-check
Python 3 script for system checks

## Requirements

* [Python 3](https://www.python.org/)
* [PyYAML](https://pyyaml.org/)

    ```bash
    $ pip install PyYAML
    ```

## Usage

1. Download package with wget or curl

    ```bash
    $ wget https://github.com/hirnsturm/py-system-check/archive/master.zip -O py-system-check.zip
    ```  
    
    ```bash
    $ curl https://github.com/hirnsturm/py-system-check/archive/master.zip -o py-system-check.zip
    ```  

2. Create configuration file

    ```bash
    $ mv config.yml.dist config.yml
    ```

3. Create your check commands in `config.yml` file.

3. Run your checks

    ```bash
    $ python3 check.py
    ```
