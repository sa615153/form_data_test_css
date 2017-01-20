import urllib2
import json

def http_get_from_server(url):
    response=urllib2.urlopen(url).read()
    #print response
    response_json=json.loads(response)
    #print response_json
    return response_json

# task_info = http_get_from_server("http://127.0.0.1:5000/dispatcher/task_info_for_report?tracknumber=IDEAS20161220164810-jpang3-test-report-api")
# print task_info["account"]
# print task_info["status"]
# print task_info["subtasks_dict"]
# print task_info["subtasks_dict"]["ideas_lib_calc"]
# print task_info["subtasks_dict"]["ideas_linux_compile"]
# print task_info["subtasks_dict"]["ideas_linux_compile"]["status"]
# print task_info["subtasks_dict"]["ideas_linux_compile"]["result"]
# print task_info["subtasks_dict"]["ideas_lib_calc"]["ict_subtasks_dict"]["calc"]
# print task_info["subtasks_dict"]["ideas_lib_calc"]["ict_subtasks_dict"]["calc_FinalReport"]
# print task_info["subtasks_dict"]["ideas_lib_calc"]["ict_subtasks_dict"]["calc"]["status"]
# print task_info["subtasks_dict"]["ideas_lib_calc"]["ict_subtasks_dict"]["calc"]["result"]
#
# sd = task_info["subtasks_dict"]
# for k,v in sd.items():  # k-subtask_name v-info_dict
#     print k+": " + v["status"] + ": "+ v["result"]


info = http_get_from_server("http://127.0.0.1:5001/dispatcher/task_info_for_report?tracknumber=IDEAS20161229140458-qa-ttt")
task_info = info["task_info"]
others = info["others"]

ben_hash_value = others["benchmark_hash_value"]
hash_value = others["hash_value"]
server_url = others["server_url"]


print ben_hash_value
print hash_value
print server_url
print "-------------------------"
print task_info["account"]
print task_info["status"]
print task_info["subtasks_dict"]
print task_info["subtasks_dict"]["ideas_lib_calc"]
print task_info["subtasks_dict"]["ideas_linux_compile"]
print task_info["subtasks_dict"]["ideas_linux_compile"]["status"]
print task_info["subtasks_dict"]["ideas_linux_compile"]["result"]
print task_info["subtasks_dict"]["ideas_lib_calc"]["ict_subtasks_dict"]["calc"]
print task_info["subtasks_dict"]["ideas_lib_calc"]["ict_subtasks_dict"]["calc_FinalReport"]
print task_info["subtasks_dict"]["ideas_lib_calc"]["ict_subtasks_dict"]["calc"]["status"]
print task_info["subtasks_dict"]["ideas_lib_calc"]["ict_subtasks_dict"]["calc"]["result"]