# Create EKS cluster

```
eksctl create cluster \
--name <cluster-name> \
--version 1.17 \
--region <region> \
--nodegroup-name linux-nodes \
--nodes 2 \
--nodes-min 1 \
--nodes-max 2 \
--node-type t3a.medium \
--ssh-access \
--ssh-public-key <ec2-keypair-name> \
--managed
```
WE can always add/remove flags from this commands as per need

# Update kubeconfig
``` aws eks update-kubeconfig --name <eks-cluster-name> ```
