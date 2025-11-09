
docker pull atlassian/confluence

docker volume create confluence-data


docker run -v confluence-data:/var/atlassian/application-data/confluence --name="confluence" -d -p 8090:8090 -p 8091:8091 atlassian/confluence