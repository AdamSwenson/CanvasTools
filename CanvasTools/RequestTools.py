"""
Created by adam on 9/20/18
"""
__author__ = 'adam'

import requests
import json
from CanvasTools.UrlTools import make_url

import environment


def make_request_header():
    """Creates the request header with Authorization value expected by canvas"""
    return {'Authorization': 'Bearer {}'.format(environment.TOKEN)}

def send_get_request(url, data={}):
    head = {'Authorization': 'Bearer {}'.format(environment.TOKEN)}
    response = requests.get(url, headers=make_request_header(), json=data)
    return response.json()

def send_post_request(url, data):
    head = {'Authorization': 'Bearer {}'.format(environment.TOKEN)}
    response = requests.post(url, headers=head, json=data)
    return response.json()


# Assignments
# Get assignment list
def get_all_course_assignments(course_id):
    """Returns a list of all the assignments for the course
    Uses api: GET /api/v1/courses/:course_id/assignments
    """
    url = make_url(course_id, 'assignments')
    return send_get_request(url, {'include': 'submissions'})


def get_assignment(course_id, assignment_id):
    """Retrieves the specified assignment and returns it as a dictionary"""
    url = make_url(course_id, 'assignments')
    url = "%s/%s" % (url, assignment_id)
    #     print(url)
    return send_get_request(url)


if __name__ == '__main__':
    pass