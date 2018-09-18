if [ $# -lt 2 ]
then
	echo "run $0 image release"
	echo "$0 e9700768b6a3 0.14"
	exit
fi

docker_image=$1
release=$2
imagename=yoisho-loan

docker tag $docker_image u1ih/$imagename:$release
docker tag $docker_image u1ih/$imagename:latest

docker login
docker push u1ih/$imagename:$release
docker push u1ih/$imagename:latest
