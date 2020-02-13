# To get AWS Credentials of a MFA forced user use below command to get dynamic credentials given back by this command

```aws sts get-session-token  --serial-number arn:aws:iam::XXXXXXX:mfa/user.name --token-code```

this will give response as below and we have to use it in our programs to make successful aws cli calls

```
{
    "Credentials": {
        "SecretAccessKey": "secret-access-key",
        "SessionToken": "temporary-session-token",
        "Expiration": "expiration-date-time",
        "AccessKeyId": "access-key-id"
    }
}
```


#To create a CloudFormation stack use below commands 
here the json template will be stored on aws s3 bucket who's location we have to pass to this command

```aws cloudformation create-stack --stack-name TESTSTACK --template-url  https://some-bucket.s3.amazonaws.com/CFT-TEMPLATE.json --parameters file://params.json --capabilities CAPABILITY_IAM --disable-rollback --region us-east-2```

here if you see we are also passing parameters file in the command it self and that parameters.json file is stored locally where i'm executing this command

the update od CloudFormation stack is also same where we just have to use ```  update-stack ``` inplace of ``` create-stack ```

Use below command to login to AWS ECR

Inorder to push/pull a image to/from ECR docker must first login to repository

```  
    aws ecr get-login --region us-east-1 > docker-login.sh
    sed  "s/\ ^-e//g" docker-login.sh
    sed -i "s/none//g" docker-login.sh 
```
