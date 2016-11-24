#!/usr/bin/env python
import sys

def main():
    data = sys.stdin.readlines()
    # this is a json string in one line so we are interested in that one line
    payload = data[0]
    response = {'body': payload['body'], 'status': 201}
    print(response)

if __name__ == "__main__":
    main()
