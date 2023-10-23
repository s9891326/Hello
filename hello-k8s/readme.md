## K8s學習指令

- [教學](https://chengweihu.com/kubernetes-tutorial-2-service-deployment-ingress/)


### Pod
- 是k8s可運行的最小`單位`(類似`公分`這個長度單位)。pod內可以跑多個docker container，但還是推薦一個pod內只跑一個docker container
   ```shell
   imagePullPolicy: ifNotPresent 的方式這樣就會先從本地端抓取image了
   ```

### Service
- service 的存在就是建立一個網路連線通道讓應用程式可以正確地連結到正在運行的 Pods，取代 `port-forward` 用法
- 一群 Pod 要如何被連線及存取的元件，可以透過label來篩選要綁定的pod(`selector: app: demoApp`)
- `nodePort`: 只能使用 30000~32767 間，設定url對應的port
- `port`: 設定service對應的port
- `targetPort`: 指定pod對應的port
   ```shell
   kubectl port-forward xxx 3000:3000
   ```

### Deployment
- Deployment: 把一個Pod做橫向擴展時使用(創建pods)，能做到無停機的系統升級(`Zero Downtime Rollout`)

### Ingress
- Ingress: 根據 `hostname` 或是 `pathname` 決定請求要轉發到哪個 Service 上(`類似nginx透過path來轉發各個請求`)，之後就可以利用該 Service 連接到 Pod 做事情了，而 K8s 的 Ingress 會統一開 http 的 80 port 以及 https 的 443 port


- 相關指令
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
minikube service xxx --url  # 取得service url
minikube addons enable ingress  # minikube addons enable ingress
```

- QA
   - Q: E1021 19:15:53.638782   19568 memcache.go:265] couldn't get current server API group list: Get "https://127.0.0.1:52378/api?timeout=32s": dial tcp 127.0.0.1:52378: connectex: No connection could be made beca
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

   - Q: 當運行 `minikube ip` 噴`Unable to resolve the current Docker CLI context "default"`，對應的json config設定位置跑掉
   - A: 使用下面指令校正
     ```shell
     docker context use default
     ```
