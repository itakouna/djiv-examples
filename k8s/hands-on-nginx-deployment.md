Hands-on example for deploying a simple application to Kubernetes using `kubectl`. In this example, we'll deploy a "Hello, Kubernetes!" web application:

1. **Create Deployment YAML:**
   Create a file named `hello-deployment.yaml` with the following content:

   ```yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: hello-deployment
   spec:
     replicas: 3
     selector:
       matchLabels:
         app: hello-k8s
     template:
       metadata:
         labels:
           app: hello-k8s
       spec:
         containers:
         - name: hello-container
           image: nginxdemos/hello:latest
           ports:
           - containerPort: 80
   ```

   This YAML defines a Deployment that creates three replicas of an Nginx-based container with the label `app: hello-k8s`.

2. **Apply Deployment:**
   Apply the deployment to your Kubernetes cluster:

   ```bash
   kubectl apply -f hello-deployment.yaml
   ```

3. **Expose Service:**
   Create a file named `hello-service.yaml` with the following content:

   ```yaml
   apiVersion: v1
   kind: Service
   metadata:
     name: hello-service
   spec:
     selector:
       app: hello-k8s
     ports:
       - protocol: TCP
         port: 80
         targetPort: 80
     type: NodePort
   ```

   Apply the service to expose the deployment:

   ```bash
   kubectl apply -f hello-service.yaml
   ```

4. **Access the Application:**
   Wait for the service to get an external IP (for LoadBalancer type). Check the status using:

   ```bash
   kubectl get svc hello-service
   ```

   Once the external IP is available, you can access the application using a web browser or curl:

   ```bash
   curl http://<external-ip>
   ```

   Replace `<external-ip>` with the actual external IP.

5. **Scale the Deployment:**
   You can scale the deployment to more replicas:

   ```bash
   kubectl scale deployment hello-deployment --replicas=5
   ```

   This will increase the number of replicas to 5.

6. **Clean Up:**
   To clean up the resources, you can delete the deployment and service:

   ```bash
   kubectl delete deployment hello-deployment
   kubectl delete service hello-service
   ```
