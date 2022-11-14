# log_compression_tool

Free up space in given directory by compressing log files (with gzip).

## Installation

Requires python3 and argh library.

To install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Use a `crontab -e` command to run a script.

For example once a month:

```
0 0 1 * * /usr/bin/log_compression_tool.py /var/log
```
It will delete the original non-compressed files.

If you want to keep them, use the `--no-remove` argument:

```
0 0 1 * * /usr/bin/log_compression_tool.py /var/log --no-remove
```

## Contributing

Install pytest in order to run tests:

```bash
pip install -r requirements-dev.txt
```
