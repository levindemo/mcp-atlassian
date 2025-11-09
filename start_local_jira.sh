
volumeExist=1
if [ "$volumeExist" == "0" ] ; then
docker volume create jiraVolume
fi

docker run -v jiraVolume:/var/atlassian/application-data/jira --name="jira" -d -p 8080:8080 atlassian/jira-software
