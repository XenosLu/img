#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import logging

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
        yield f'            "{result.netloc}",'

def handle(content):
    return '\n'.join(sorted(set(parse(content))))



def main():
    # logger.info(os.path.dirname(os.path.abspath(__file__)))
    with open('list.txt') as r:
        content = r.read()
        new_content = handle(content)
        with open('result.txt', 'w') as w:
            w.write(new_content)


if __name__ == '__main__':
    init_log_console()
    main()
