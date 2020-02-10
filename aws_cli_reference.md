# To get AWS Credentials of a MFA forced user use below command to get dynamic credentials given back by this command

```aws sts get-session-token  --serial-number arn:aws:iam::XXXXXXX:mfa/user.name --token-code```

this will give response as below and we have to use it in our programs to make successful aws cli calls

```{
    "Credentials": {
        "SecretAccessKey": "secret-access-key",
        "SessionToken": "temporary-session-token",
        "Expiration": "expiration-date-time",
        "AccessKeyId": "access-key-id"
    }
}```
