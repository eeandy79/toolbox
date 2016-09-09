import requests
import time
import sys
import os

def MonitorQueueJob(branch):
	url = 'http://hcde:8081/view/ACP/job/{}/api/json?pretty=true'.format(branch)
	cnt = 1
	while True:
		response = requests.get(url)
		data = response.json()
		queueItem = data['queueItem']
		if queueItem:
			dot = '.' * cnt
			os.system('cls||clear')
			sys.stdout.write('{} pending build job {}'.format(branch, dot))
			sys.stdout.flush()
			cnt = cnt + 1
			time.sleep(1)
		else:
			break;


def MonitorBuildJob(branch):
	url = 'http://hcde:8081/view/ACP/job/{}/api/json?pretty=true'.format(branch)
	response = requests.get(url)
	data = response.json()
	
	buildNum = data['builds'][0]['number']

	url = 'http://hcde:8081/view/ACP/job/{}/{}/api/json?pretty=true'.format(branch, buildNum)

	while True:
		response = requests.get(url)
		data = response.json()
		
		buildStatus = data['building']
		buildResult = data['result']
		
		if buildStatus:
			print '{} building {} ...'.format(branch, buildNum)
			time.sleep(1)
		else:
			print '{} latest build {} {}'.format(branch, buildNum, buildResult)
			break


inputBranch = sys.argv[1]
branch = 'ACPImage-trunk'
if inputBranch == '1.3':
	branch = 'ACPImage-1.3.x.0'

MonitorQueueJob(branch)
MonitorBuildJob(branch)


