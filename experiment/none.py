import json
str = u'[\
  {\
    "assistant_git_dir": null,\
    "backup_path": "",\
    "benchmark": null,\
    "git_dir": "ypxu_src",\
    "ict_data": null,\
    "id": "914",\
    "machine": "Linux16",\
    "subtask_name": "performance",\
    "tracknumber": "IDEAS20161130133532-ypxu-src_20161130"\
  }\
]'

#
# what = json.loads(str)
# print what
# print type(what)
# print what[0]
# print what[0]['ict_data']
# print what[0]['ict_data'] is not None
# if what[0]['ict_data']:
#     print 1
# else:
#     print 2


what = json.loads('121')
print what
print type(what)