import urllib2
import json
import time


def http_get_tasks_from_server():
    url='http://127.0.0.1:5000/dispatcher/AvailableTaskPCMatch'
    response=urllib2.urlopen(url).read()
    # print "type of origin"
    # print type(response)
    response_json=json.loads(response)
    # print "type after loads"
    # print type(response_json)
    return response_json

def http_post(data):
    url = 'http://127.0.0.1:5000/PC/JobDone'
    json_data = json.dumps(data)
    request = urllib2.Request(url,json_data)
    print json_data
    response = urllib2.urlopen(request)
    return response.read()

if __name__ == "__main__":
    tasks_data = http_get_tasks_from_server()
    # print tasks_data
    # print type(tasks_data)
    for i in tasks_data:
        i["result"] = "success"
    print tasks_data
    re = http_post(tasks_data)


