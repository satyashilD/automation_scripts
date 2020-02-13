
Make sure the EC2 instance that you are using to push/pull images from have IAM Role attached having enugh permissions
If you are doing it from local machine then you need to configure your ceredentials first and then folow below steps

If you are using ECS service for your containers deployment then make sure you have below IAM Policies are attached to the IAM Role you have created for ECS

```
"arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
"arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryFullAccess"
```


To push image on ECR

#Docker login: As we are trying to push image to a private repository in this case it's ECR so the very first step is to perform login to get connected to repository


```
 sudo aws ecr get-login --region us-east-1 > docker-login.sh
 sed  -i "s/\ -e//g" docker-login.sh
 sed -i "s/none//g" docker-login.sh
 ubuntu@ip-172-31-45-126:~$ sudo bash docker-login.sh
WARNING! Using --password via the CLI is insecure. Use --password-stdin.
WARNING! Your password will be stored unencrypted in /home/ubuntu/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded
```
or if that is not working then use these commands

```
pwd="$(aws ecr get-login  --region us-east-1 | awk '{print $6}')"
sudo docker login -u AWS -p "$pwd" https://XXXXXXX.dkr.ecr.us-east-1.amazonaws.com

```
Once you successfully get logged into ECR then next step would be to tag your local docker image with ECR repo url
```
1> List your images to choose the one you wanted to push on ECR

ubuntu@ip-172-31-45-126:~$ sudo docker images | head -2
REPOSITORY                                                             TAG                 IMAGE ID            CREATED             SIZE
sample-worker                                                         v2                  ff42c3764de7        2 days ago          111MB

2> tag your image with ECR repo

sudo docker tag ff42c3764de7  XXXXX.dkr.ecr.us-east-1.amazonaws.com/sample:sample-master

3> push the image

sudo docker push XXXXX.dkr.ecr.us-east-1.amazonaws.com/sample:sample-master

Thats all

```

To pull the image the process is simple login and get image url from ECR console and do 

```
docker pull XXXXX.dkr.ecr.us-east-1.amazonaws.com/sample:sample-master
```
