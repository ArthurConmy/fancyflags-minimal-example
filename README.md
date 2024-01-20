# `fancyflags` minimal example

This repo shows a minimal example of using `fancyflags` to create two files that can independently be run as CLIs, and one file implictly calls the other file.

# Examples:

Basic usage:

```bash
python true_main.py -- --replay.capacity=10
```

Nested usage:

```bash
python cli_script_that_calls_main.py -- --replay.capacity=10
```
