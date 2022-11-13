# log_compression_tool

Free up space in given directory by compressing log files (with gzip).

## Installation

requires python3

## Usage

Use a `crontab -e` command to run a script.

for example once a month:

```
0 0 1 * * /usr/bin/log_compression_tool.py /var/log
```

## Contributing

Install pytest in order to run tests:

```bash
pip install -r requirements-dev.txt
```
