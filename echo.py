#!/usr/bin/env python
import sys
import json

# response - creates json structure
def response(body, status):
    resp = {
        'status': status,
        'body': body,
        }
    # converting to json        
    print(json.dumps(resp))    


def main():
    data = sys.stdin.readlines()
    # this is a json string in one line so we are interested in that one line, qq
    payload = data[0]
    
    request = json.loads(payload)
    
    response('%s updated 2nd ' % (request['body']), 201)

if __name__ == "__main__":
    main()
