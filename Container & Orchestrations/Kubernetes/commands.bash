# ----------------------------------
#   kubectl 
# ----------------------------------

# ------------------------ < BASE > ------------------------ # 
kubectl version --short

kubectl create -f nginx.yaml
kubectl delete -f nginx.yaml -f redis.yaml
kubectl replace -f nginx.yaml

# diff before changes
kubectl diff -f configs/
kubectl apply -f configs/
# same as above but recursively 
kubectl diff -R -f configs/
kubectl apply -R -f configs/

kubectl get ingress --field-selector foo.bar=baz
kubectl get pods --field-selector=status.phase!=Running,spec.restartPolicy=Always
# ------------------------ < CONFIG > ------------------------ # 
kubectl config get-contexts

kubectl config current-context
kubectl config use-context rancher-desktop

kubectl config set-cluster default-cluster --server=https://<host ip>:6443 --certificate-authority <path-to-kubernetes-ca> --embed-certs
kubectl config set-credentials <credential-name> --client-key <path-to-key>.pem --client-certificate <path-to-cert>.pem --embed-certs

kubectl config set-context default-system --cluster default-cluster --user <credential-name>
kubectl config use-context default-system



# ------------------------ < NAMESPACE > ------------------------ #
kubectl get namespaces 

kubectl run nginx --image=nginx --namespace=<insert-namespace-name-here>
kubectl get pods --namespace=<insert-namespace-name-here>

# Namespace preference
kubectl config set-context --current --namespace=<insert-namespace-name-here>
# Validate it
kubectl config view --minify | grep namespace:

# To see which Kubernetes resources are and aren't in a namespace:
# In a namespace
kubectl api-resources --namespaced=true
# Not in a namespace
kubectl api-resources --namespaced=false



# ------------------------ < CLUSTER > ------------------------ # 
kubectl cluster-info

# ------------------------ < NODES > ------------------------ # 
kubectl get nodes
# ------------------------ < PODS > ------------------------ # 
kubectl get pods 
kubectl get po 
kubectl get -w pods
kubectl get po -A

kubectl describe pods
kubectl delete pod nginx

# List the Pods created by the deployment:
kubectl get pods -l app=nginx
# Display information about a Pod:
kubectl describe pod <pod-name>

# equality-based 
kubectl get pods -l environment=production,tier=frontend
# set-based
kubectl get pods -l 'environment in (production),tier in (frontend)'
kubectl get pods -l 'environment in (production, qa)'
kubectl get pods -l 'environment,environment notin (frontend)'

# Field Selector 
kubectl get pods --field-selector status.phase=Running

# ------------------------ < DEPLOY > ------------------------ # 
kubectl get deployments
kubectl get deployments -o yaml


kubectl delete deploy <deploy_name>

# Run an instance of the nginx container by creating a Deployment object
kubectl create deployment nginx --image nginx


# ------------------------ < svc - SERVICES > ------------------------ # 
kubectl get service -o wide

kubectl delete svc <svc_name>

# ------------------------ < pv - PersistentVolumeClaim > ------------------------ # 
kubectl delete pv <pv_name>

# ------------------------ < pvc - PersistentVolumeClaim > ------------------------ # 
kubectl describe pvc <pvc_name>
kubectl delete pvc <pvc_name>

# ------------------------ < RUN > ------------------------ # 
kubectl apply -f .
kubectl apply --watch -f . 

kubectl get all
kubectl get events
kubectl get endpoints


kubectl exec <pod-name> -it --namespace default /bin/bash


kubectl get events --all-namespaces  --sort-by='.metadata.creationTimestamp'

# Start k8s proxy to access control pane
kubectl proxy
kubectl proxy --address="192.168.0.101" -p 8001 --accept-hosts='^*$'


### LOGS
kubectl logs -f -l app=<app_name>
kubectl logs -f deployment.apps/<deploy-name>
kubectl logs -f nginx

# k8s Dasboard
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.7.0/aio/deploy/recommended.yaml
# Getting Bearer Token
kubectl -n kubernetes-dashboard create token admin-user
# start proxy
kubectl proxy
# Enter http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/#/login

# clean up  https://github.com/kubernetes/dashboard/blob/master/docs/user/access-control/creating-sample-user.md
kubectl -n kubernetes-dashboard delete serviceaccount admin-user
kubectl -n kubernetes-dashboard delete clusterrolebinding admin-user

# ----------------------------------
#   minikube
# ----------------------------------

minikube start 
minikube pause
minikube delete 

minikube start --driver=docker
# make docker default driver 
minikube config set driver docker
minikube delete --all --purge


minikube start --base-image "gcr.io/k8s-minikube/kicbase:v0.0.32"


minikube kubectl -- get pods -A


kubectl get po -A

# https://danieliser.com/setup-minikube-on-wsl2-for-windows-10/
sudo apt install -y conntrack



# https://askubuntu.com/a/460027/1166575
 sudo apt-get install w3m w3m-img
 w3m <url_of_the_webpage>


# Starting and stoppig 
 kubectl config current-context
 kct rancher-desktop


# minikube dashboard
/home/fb/projects/python/http_mocker/env/bin/python reverse_minikube.py 38755