"""
Created by adam on 9/20/18
"""
__author__ = 'adam'

import requests
import json

import environment

def send_get_request(url):
    head = {'Authorization': 'Bearer {}'.format(environment.TOKEN)}
    response = requests.get(url, headers=head)
    return response.json()

def send_post_request(url, data):
    head = {'Authorization': 'Bearer {}'.format(environment.TOKEN)}
    response = requests.post(url, headers=head, json=data)
    return response.json()



if __name__ == '__main__':
    pass