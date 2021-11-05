#! /usr/bin/env python

# CLI structure

import argparse
import webbrowser
import subprocess
import sys



parser = argparse.ArgumentParser(description='Global CLI for multiple usage', prog='bipbop', usage='%(prog)s [argument]', formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument('-t','--tool', metavar='', type=str,help='Choose the tool you want to use', choices=['excel', 'slack'])
parser.add_argument('-w','--web', metavar='', type=str, help='Choose the web app you want to open', choices=['datafy', 'jira', 'gmail'])

args = parser.parse_args()

# Define web routes URL's

if args.web == 'datafy':
    print('Opening Datafy UI...')
    webbrowser.open('https://app.datafy.cloud/')
    
if args.web == 'jira':
    print('Opening JIRA...')
    webbrowser.open('https://luminus.atlassian.net/jira/projects?selectedProjectType=software')

if args.web == 'gmail':
    print('Opening Gmail...')
    webbrowser.open('https://www.gmail.com')
    
# Define tools path to .exe
if args.tool == 'excel':
    print('Opening Excel...')
    subprocess.run("/mnt/c/Program Files (x86)/Microsoft Office/root/Office16/EXCEL.EXE")
    
if args.tool == 'slack':
    print('Opening Slack...')
    subprocess.run("/mnt/c/Users/kevec/AppData/Local/slack/slack.exe")

if len(sys.argv) < 2 :
    test_input = input('What is your name: ')
    print(f'Dear {test_input}, please get a look at the help below:')
    parser.print_help()
    


