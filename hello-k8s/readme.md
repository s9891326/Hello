## K8s學習指令

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

### Volume
- 跟docker上的一樣，提供一個位置讓pod產生的資料有地方可以存。但會有儲存位置的耦合(docker通常都是用local端某個資料夾來當作volume)，這樣就會綁死volume的位置，無法隨時抽換
- 所以k8s提出了`PV/PVC(PersistentVolume/PersistentVolumeClaims)`，來解決Pod與具體存儲Volume耦合
- `PVC` 是 K8s 提供的解耦機制在`Volume`跟`PV`之間多一層抽象
- `PV` 是 K8s持久化的抽象底層可以對接實體儲存
  - PV對應的訪問模式
    ```shell
    RWO: ReadWriteOnce
    ROX: ReadOnlyMany
    RWX: ReadWriteMany
    ```
  - PV 有四種狀態 (STATUS)
    1. Available：表示 PV 為可用狀態
    2. Bound：表示已綁定到 PVC
    3. Released：PVC 已被刪除，但是尚未回收
    4. Failed：回收失敗
  - PV 有三種回收策略 (RECLAIM POLICY)，分別是
    1. Retain：手動回收
    2. Recycle：透過刪除命令 rm -rf /thevolume/*
    3. Delete：用於 AWS EBS, GCE PD, Azure Disk 等儲存後端，刪除 PV 的同時也會一併刪除後端儲存磁碟。
  
### RBAC(Role-Base Access Controller)
- 管制用戶/Group訪問k8s API的機制。透過適當的角色配置與授權分配，管理者可以決定使用者能夠使用哪些功能。例如允許某個角色能新增 Pod 或只能夠察看但是不能新增等等。
- [說明](https://ithelp.ithome.com.tw/articles/10195944)

### 啟動方式
1. 開啟docker、kubectl
2. 開啟minikube
```shell
minikube start
```
4. 開啟對應的連線
```shell
minikube tunnel --cleanup
```

### Helm
- 是一個管理設定檔的工具
    ```shell
    helm create xxx
    helm install --generate-name bitnami/wordpress
    helm install --set name=hello-helm myhelm hello-helm
    helm upgrade myhelm hello-helm
    helm list
    ```

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
    
    kubectl api-resources  # 查看kubectl內各項資源的名稱和內建的簡寫
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
   ```
- A:
    ```shell
    最終重新啟動minikube才啟動成功，並更改對應的port(`56800`)
    minikube start
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

### 參考網站
1. [PV/PVC管理](https://medium.com/k8s%E7%AD%86%E8%A8%98/kubernetes-k8s-pv-pvc-%E5%84%B2%E5%AD%98%E5%A4%A7%E5%B0%8F%E4%BA%8B%E4%BA%A4%E7%B5%A6pv-pvc%E7%AE%A1%E7%90%86-4d412b8bafb5)
2. [30天鐵人賽](https://ithelp.ithome.com.tw/articles/10193550)
3. [PV/PVC介紹](https://blog.toright.com/posts/6541/kubernetes-persistent-volume.html)
4. [教學](https://chengweihu.com/kubernetes-tutorial-2-service-deployment-ingress/)
5. [教學2](https://alankrantas.medium.com/%E7%AD%86%E8%A8%98-%E5%9C%A8%E6%9C%AC%E6%A9%9F-kubernetes-%E7%92%B0%E5%A2%83%E4%BD%88%E7%BD%B2%E5%AE%B9%E5%99%A8%E4%B8%A6%E4%B8%B2%E6%8E%A5%E6%9C%8D%E5%8B%99-ingress-%E4%BC%BA%E6%9C%8D%E5%99%A8-%E4%BD%BF%E7%94%A8-minikube-%E8%88%87%E5%96%AE%E4%B8%80-yaml-%E6%AA%94%E5%AF%A6%E4%BD%9C-1d25228e6416)
6. [官方教學](https://kubernetes.io/docs/tasks/access-application-cluster/ingress-minikube/#what-s-next)
