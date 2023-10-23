## K8s學習指令

- [教學](https://chengweihu.com/kubernetes-tutorial-2-service-deployment-ingress/)
- [教學2](https://alankrantas.medium.com/%E7%AD%86%E8%A8%98-%E5%9C%A8%E6%9C%AC%E6%A9%9F-kubernetes-%E7%92%B0%E5%A2%83%E4%BD%88%E7%BD%B2%E5%AE%B9%E5%99%A8%E4%B8%A6%E4%B8%B2%E6%8E%A5%E6%9C%8D%E5%8B%99-ingress-%E4%BC%BA%E6%9C%8D%E5%99%A8-%E4%BD%BF%E7%94%A8-minikube-%E8%88%87%E5%96%AE%E4%B8%80-yaml-%E6%AA%94%E5%AF%A6%E4%BD%9C-1d25228e6416)
- [官方教學](https://kubernetes.io/docs/tasks/access-application-cluster/ingress-minikube/#what-s-next)

### Pod
- 是k8s可運行的最小`單位`(類似`公分`這個長度單位)。pod內可以跑多個docker container，但還是推薦一個pod內只跑一個docker container
   ```shell
   imagePullPolicy: ifNotPresent 的方式這樣就會先從本地端抓取image了
   ```

### Service
- 建立一個網路連線通道讓應用程式可以正確地連結到正在運行的 Pods，取代 `port-forward` 用法
- 一群 Pod 要如何被連線及存取的元件，可以透過label來篩選要綁定的pod(`selector: app: demoApp`)
- `nodePort`: 只能使用 30000~32767 間，設定url對應的port
- `port`: 設定service對應的port
- `targetPort`: 指定pod對應的port
   ```shell
   kubectl port-forward xxx 3000:3000
   ```

### Deployment
- 把一個Pod做橫向擴展時使用(創建pods)，能做到無停機的系統升級(`Zero Downtime Rollout`)

### Ingress
- 根據 `hostname` 或是 `pathname` 決定請求要轉發到哪個 Service 上(`類似nginx透過path來轉發各個請求`)，之後就可以利用該 Service 連接到 Pod 做事情了，而 K8s 的 Ingress 會統一開 http 的 80 port 以及 https 的 443 port


### Helm
- 是一個管理設定檔的工具

### 相關指令
- kubectl
    ```shell
    kubectl get pods
    
    kubectl get pods -o wide  # 查看pod所在節點
    
    kubectl get pods --show-labels
    
    kubectl get ingress
    
    kubectl create -f xxx.yaml
    
    kubectl port-forward xxx 3000:3000
    kubectl port-forward service/xxx 3000:3000
    kubectl port-forward deploy/xxx 3000:3000
    
    kubectl delete pod xxx
    kubectl delete service xxx
    kubectl delete deploy xxx
    
    ```

- minikube
    ```shell
    minikube ip
    minikube ssh
    minikube service xxx
    minikube service xxx --url  # 取得service url
    minikube addons enable ingress  # minikube addons enable ingress
    minikube service list
    minikube dashboard
    minikube tunnel --cleanup  # 開啟通道，將minikube環境的cluster ip連到本機的localhost
    ```

### QA
1. E1021 19:15:53.638782   19568 memcache.go:265] couldn't get current server API group list: Get "https://127.0.0.1:52378/api?timeout=32s": dial tcp 127.0.0.1:52378: connectex: No connection could be made beca
use the target machine actively refused it.
- A:
    ```shell
    執行 kubectl get nodes -v=10 發現kubectl config是從這裡拉取設定檔的(C:\Users\eddy\.kube\config)
    查看對應的config檔，終於找到對應的ip了
    
    - cluster:
        certificate-authority: C:\Users\eddy\.minikube\ca.crt
        extensions:
        - extension:
            last-update: Sat, 21 Oct 2023 19:17:11 CST
            provider: minikube.sigs.k8s.io
            version: v1.31.2
          name: cluster_info
        server: https://127.0.0.1:52378
      name: minikube
    
    最終重新啟動minikube才啟動成功，並更改對應的port(`56800`)
    ```

2. 當運行 `minikube ip` 噴`Unable to resolve the current Docker CLI context "default"`，對應的json config設定位置跑掉
- A: 使用下面指令校正
    ```shell
    docker context use default
    ```

3. 當執行 `kubectl exec -ti -n ingress-nginx pod_name -- /bin/bash` 噴 `OCI runtime exec failed: exec failed: unable to start container process: exec: "C:/Program Files/Git/usr/bin/bash"`
- A: 在git bash底下要使用雙/
    ```shell
    kubectl exec -ti -n ingress-nginx pod_name -- //bin//bash
    ```

