from asana import asana
asanaAPI = asana.AsanaAPI('1OK6Xjei.8e0ZQh51ZBhyf2hur4vJn47', debug=True)

# see your workspaces
#Result: [{u'id': 123456789, u'name': u'asanapy'}]
myspaces = asanaAPI.list_workspaces()
workspaceID = myspaces[0]["id"]
listOfTasks = asanaAPI.get_project_tasks(7072037251049)
taskList = []
for dictionaryTask in listOfTasks:
    taskList.append(str(dictionaryTask["name"]))

for task in taskList:
    if task[-1] != ":":
        print "    "+task.title()
    else:
        print task

# create a new project
# asanaAPI.create_project('test project', myspaces[0]['id'])

# create a new task
# asanaAPI.create_task('5:31 created this task remotely', myspaces[0]['id'],
                      # assignee_status='later', notes='some notes')

# add a story to task
# asanaAPI.add_story(mytask, 'omgwtfbbq')
