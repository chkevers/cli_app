#! /usr/bin/env python

import click

@click.command()
@click.option('-t', '--test', help='Testing argument')
def test_function(test):
    print(f'Bipbop {test}')

if __name__ == "__main__":
    test_function()