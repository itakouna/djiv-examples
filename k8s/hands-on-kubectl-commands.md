Perform basic operations with `kubectl`, the Kubernetes command-line tool, you can follow these hands-on steps:

1. **Install `kubectl`:**
   If you haven't already installed `kubectl`, you can follow the official installation guide based on your operating system: [Install and Set Up kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/).

2. **Configure `kubectl` to connect to your Kubernetes cluster:**
   You need to have access to a Kubernetes cluster and its credentials to use `kubectl`. Configure `kubectl` with the credentials of your Kubernetes cluster. This typically involves setting up kubeconfig file, which contains information about the cluster, authentication details, and other configuration options.

   ```bash
   # Example command to set kubeconfig file path
   export KUBECONFIG=/path/to/kubeconfig
   ```

3. **Verify `kubectl` installation and configuration:**
   Run the following command to verify that `kubectl` is correctly installed and configured to connect to your Kubernetes cluster:

   ```bash
   kubectl version --short
   ```

   This command should output the client and server versions of `kubectl` and the Kubernetes API server.

4. **Basic `kubectl` commands:**

   - **View cluster information:**
     ```bash
     kubectl cluster-info
     ```

   - **List all resources in the default namespace:**
     ```bash
     kubectl get all
     ```

   - **List pods in a specific namespace:**
     ```bash
     kubectl get pods -n <namespace>
     ```

   - **Describe a resource:**
     ```bash
     kubectl describe <resource_type> <resource_name>
     ```

   - **Create a resource from a YAML file:**
     ```bash
     kubectl apply -f <yaml_file>
     ```

   - **Delete a resource:**
     ```bash
     kubectl delete <resource_type> <resource_name>
     ```

   - **Scale a deployment:**
     ```bash
     kubectl scale deployment <deployment_name> --replicas=<num_replicas>
     ```

   - **Exec into a pod:**
     ```bash
     kubectl exec -it <pod_name> -- /bin/bash
     ```

   - **Port forwarding:**
     ```bash
     kubectl port-forward <pod_name> <local_port>:<remote_port>
     ```

   - **Logs of a pod:**
     ```bash
     kubectl logs <pod_name>
     ```

   - **Apply rolling updates to a deployment:**
     ```bash
     kubectl set image deployment/<deployment_name> <container_name>=<new_image>:<tag>
     ```

   - **Get information about nodes:**
     ```bash
     kubectl get nodes
     ```

   These are some of the basic `kubectl` commands to get started with managing Kubernetes clusters and resources. You can explore more commands and options in the [kubectl documentation](https://kubectl.docs.kubernetes.io/).