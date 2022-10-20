#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import logging
import re
import glob
import json

# Set file path as current path
os.chdir(os.path.dirname(os.path.abspath(__file__)))

logger = logging.getLogger(__name__)


def init_log():
    """set logging"""
    formatter = logging.Formatter(
        '%(asctime)s %(filename)s %(levelname)s [line:%(lineno)d] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
    )
    logfile = logging.FileHandler(f'{os.path.splitext(__file__)[0]}.log')
    logfile.setFormatter(formatter)
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    logging.basicConfig(level=logging.INFO, handlers=[logfile, console])
    logger.setLevel(logging.DEBUG)


def init_log_console():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(filename)s %(levelname)s [line:%(lineno)d] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
    )


def parse(content):
    for line in content.split('\n'):
        line = line.strip().strip('^')
        if line.startswith('#'):
            continue
        if not line:
            continue
        line = line.split(' ')[0]

        if not line.startswith('http'):
            line = f'http://{line}'
        from urllib.parse import urlparse

        result = urlparse(line, scheme='http')
        yield f'    "{result.netloc}",'


def parser(data):
    for k, v in data.items():
        yield from parse(v)


def handle(data):
    return '\n'.join(sorted(set(parser(data))))


def generate(new_content):
    with open('wpad.dat') as r:
        content = r.read()
        content = re.sub(
            "//generate start[\\s\\S]*//generate end",
            f'//generate start\n{new_content}\n    //generate end',
            content,
        )
        with open('wpad.dat', 'w') as w:
            w.write(content)


def main():
    for filepath in glob.iglob('rules*.txt'):
        logger.info(f'reading from {filepath}')
        with open(filepath, encoding='utf-8') as r:
            data = json.load(r)
            new_content = handle(data)
            generate(new_content)


if __name__ == '__main__':
    init_log_console()
    main()
