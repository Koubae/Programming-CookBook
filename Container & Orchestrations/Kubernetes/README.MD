K8S 
==============




Documentations
-------------


* [Kubernetes Liveness and Readiness Probes](https://github.com/sebinxavi/kubernetes-readiness)
* [Configure Liveness, Readiness and Startup Probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)
* [Kubernetes Cluster API](https://cluster-api.sigs.k8s.io/)
* [Deploying the Dashboard UI](https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/#deploying-the-dashboard-ui)
* [Creating Sample User](https://github.com/kubernetes/dashboard/blob/master/docs/user/access-control/creating-sample-user.md)
* [Client Libraries](https://kubernetes.io/docs/reference/using-api/client-libraries/)
* [API Conventions](https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md)
* [Kubernetes API](https://kubernetes.io/docs/reference/kubernetes-api/)
* [Kubectl book](https://kubectl.docs.kubernetes.io/)

Components
----------

### k8s components high-level

- containers
- pod
- node (worker node)
- master node 
- cluster
- Control Pane


### Software components

- Container Runtime 
- kubelet
- kube-proxy
- [api Server](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-apiserver/)  | cluster gateway 
- Scheduler
- Controller Manager
- Cloud Controler Manager (optional)
- etcd (key-value store of cluser stare, (brain))
- [DNS - Cluster DNS](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/)
- Load Balancer

### Master processes

- api Server
- Scheduler
- Controller Manager
- etcd (key-value store of cluser stare, (brain))


### Workloads

- Deployment 
- ReplicaSet
- StatefulSet 
- DaemonSet
- Job
- Third-Party Workloads

### Services 

- Services
- Ingress


### Other components

- [Node conformance test](https://kubernetes.io/docs/setup/best-practices/node-conformance/#node-conformance-test)
- WebUI (Dashboard)
- Container Resource Monitoring
- Cluster-level Loggin

Projects - Repos
----------------

### k8s 

* [k8s Cluster Autoscaler](https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler#readme)
* [CRI: the Container Runtime Interface](https://github.com/kubernetes/community/blob/master/contributors/devel/sig-node/container-runtime-interface.md)
* [Kubernetes Cluster API](https://cluster-api.sigs.k8s.io/)

### cri-o 

*CRI-O - OCI-based implementation of Kubernetes Container Runtime Interface*

* [cri-o](https://github.com/cri-o/cri-o)



### Locust

* [kubernetes-locust](https://github.com/mosesliao/kubernetes-locust)


### Misc 

* [Flask-Healthz](https://github.com/fedora-infra/flask-healthz)


Related Topics
---------------

* [The Raft Consensus Algorithm](https://raft.github.io/)