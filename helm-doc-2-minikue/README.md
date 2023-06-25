# helm-tutorial
## Demo to create and install helm charts for beginners

### In this demo, we will see how to create our own helm chart to start Nginx Server, install and uninstall it.

Ubuntu Version: 21.10

Minikube Version: v1.29.0, 
commit: ddac20b4b34a9c8c857fc602203b6ba2679794d3

Kubectl Version: 1.26

To see how to install minikube and kubernetes, [click here](https://github.com/riddhigala09/Kubectl-Minikube-Ubuntu.git)

Helm Version: v3.11.1

To see how to install helm, [click here](https://github.com/riddhigala09/installing-helm.git)

**This demo has three parts:**

**1. Starting Minikube Cluster**

**2. Creating and Installing Helm Chart for Nginx Server**

**3. Uninstalling Helm Chart.**

### Part 1: Starting Minikube Cluster

   1. To start minikube cluster, enter command:
      
     > minikube start
    
   ![Screenshot from 2023-02-17 13-59-11](https://user-images.githubusercontent.com/122020679/219593055-48b96185-12a5-491f-8ee6-ecd4196ee4e5.png)
    
   Cluster started

   ![Screenshot from 2023-02-17 14-01-45](https://user-images.githubusercontent.com/122020679/219593622-c9d6182f-e337-41d5-9638-928af8cef3c1.png)
    
   Once our cluster has started, we can move to Part 2.
    
 
### Part 2: Creating and Installing Helm Chart

   1. Make Directory: 
    
    > cd Desktop
    
    > mkdir helm-tutorial
      
    > cd helm-tutorial
      
   ![Screenshot from 2023-02-20 11-32-28](https://user-images.githubusercontent.com/122020679/220022914-327e29bb-6c77-449b-8057-61f05b16f4d9.png)
   
   2. Create chart: chart1
    
    > helm create chart1
   
   ![Screenshot from 2023-02-20 11-37-15](https://user-images.githubusercontent.com/122020679/220023887-6188f6fa-3fac-4339-a7eb-556da163dad8.png)
   
   3. Enter Command: 
    
    > tree chart1/
    
   If tree is not installed, Install it using: 
     
    > sudo apt-get install tree
    
   This command will create the entire directory structure with all the files required to deploy nginx. 
      
   ![Screenshot from 2023-02-20 11-54-31](https://user-images.githubusercontent.com/122020679/220028141-37dc00eb-e940-456b-b7a1-37a900a99b6f.png)
   
   4. Make changes in values.yaml
   
      Open values.yaml in text editor.
     
      1. In this file, we will modify pullPolicy from IfNotPresent to Always. We will do this modification so as to avoid pulling an image if it already exits, and to let pull the image everytime a pod is deployed.
   
         From:
   
         ![Screenshot from 2023-02-20 12-05-43](https://user-images.githubusercontent.com/122020679/220030990-87dd9f9e-3d3c-445b-b4d2-90099ba618ae.png)
 
         To: 
   
         ![Screenshot from 2023-02-20 13-03-58](https://user-images.githubusercontent.com/122020679/220041813-37676cd7-0dce-426e-99ea-d3a4f3c62815.png)
   
      2. In service, modify ClusterIP to NodePort
  
         From:
  
         ![Screenshot from 2023-02-20 12-08-52](https://user-images.githubusercontent.com/122020679/220031935-9bfb956a-c750-49da-8af1-8c94c405ff07.png)

         To: 
  
         ![Screenshot from 2023-02-20 12-11-36](https://user-images.githubusercontent.com/122020679/220032175-12ed8674-1255-4f18-a327-1949c9dad6a3.png)
      
      3. In imagePullSecrets, add nameOverride and fullnameOverride
   
         From: 
      
         ![Screenshot from 2023-02-20 12-23-45](https://user-images.githubusercontent.com/122020679/220034396-dfad45c6-47d7-4ad9-847c-79f2e3010771.png)

         To: 
      
         ![Screenshot from 2023-02-20 12-28-34](https://user-images.githubusercontent.com/122020679/220035120-d0b9e81d-fb51-4681-bc24-4fe2998a92b6.png)
      
      4. Add Service Account Name:
    
         From: 
      
         ![Screenshot from 2023-02-20 12-30-56](https://user-images.githubusercontent.com/122020679/220035422-4ce36140-90c1-4d0e-bc3c-8c5795437089.png)

         To:
      
         ![Screenshot from 2023-02-20 12-32-24](https://user-images.githubusercontent.com/122020679/220036191-6a9f2c60-9e9b-452b-a84c-8b208cf2878e.png)
    
   5. Install Helm Chart
   
     > helm install <full name override> <chart name>/ --values <chart name>/values.yaml

   In our case, command will be:
   
     > helm install nginx chart1/ --values chart1/values.yaml
     
   ![Screenshot from 2023-02-20 13-07-53](https://user-images.githubusercontent.com/122020679/220042469-97ab90bc-18d0-4d8b-b512-3327cb14c8ff.png)

   6. Export Node Port and Node IP
   
      Copy and run the the two **"export"** command from helm install output
      
   ![Screenshot from 2023-02-20 13-12-11](https://user-images.githubusercontent.com/122020679/220043256-1bd4f931-2be8-484b-a3da-a56bc8b4a57a.png)
   
   7. View Nginx Server
   
      Copy and run the **"echo"** command.
      
   ![Screenshot from 2023-02-20 13-14-21](https://user-images.githubusercontent.com/122020679/220043712-8602fb2d-9485-4d2e-8f98-20d8470387e7.png)

   8. Open Link
   
   ![Screenshot from 2023-02-20 13-15-56](https://user-images.githubusercontent.com/122020679/220043999-e79a1233-16f3-45a5-9aad-400cd082d47a.png)

   We will be directed to Nginx Server Page
      
   ![Screenshot from 2023-02-20 13-20-29](https://user-images.githubusercontent.com/122020679/220044727-f1d1e08d-90ca-4fa9-88a0-9d859960387d.png)

### Part 3: Uninstalling Helm Chart:

   1. List charts
   
     > helm list

   2. Uninstall chart
   
     > helm uninstall <chart_name>
     
   In our case, it will be:
     
     > helm uninstall nginx
     
   ![Screenshot from 2023-02-20 13-25-54](https://user-images.githubusercontent.com/122020679/220045959-6416875e-5ee2-4a48-bd23-83138585c60c.png)
   
   3. Stop Minikube Cluster
   
     > minikube stop
     
   ![Screenshot from 2023-02-20 13-40-38](https://user-images.githubusercontent.com/122020679/220048944-48cbbad6-0cc0-4915-8d92-8d1a21e0f2c7.png)
     
   4. Delete Minikube Cluster
   
     > minikube delete
     
   ![Screenshot from 2023-02-20 13-41-49](https://user-images.githubusercontent.com/122020679/220049182-e0df60ea-c7e2-42b3-b499-b2eec33c32f4.png)

   

**To learn more helm commands, [click here](https://helm.sh/docs/helm/)**

***We have successfully completed this tutorial!***
