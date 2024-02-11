Hands-on example demonstrating some common Docker commands:

1. **Pulling an Image:**
```
docker pull nginx:latest
```
This command pulls the latest version of the nginx image from Docker Hub.

1. **Listing Images:**
```
docker images
```
This command lists all locally available Docker images on your system.

1. **Running a Container:**
```
docker run -it nginx:latest
```
This command runs a new container based on the nginx image in interactive mode (`-it`). You'll be dropped into a shell prompt inside the container.

1. **Listing Containers:**
```
docker ps -a
```
This command lists all containers, including those that are currently running and stopped.

1. **Stopping a Container:**
```
docker stop <container_id>
```
Replace `<container_id>` with the ID or name of the container you want to stop. This command stops a running container.

1. **Starting a Stopped Container:**
```
docker start <container_id>
```
This command starts a stopped container. Again, replace `<container_id>` with the ID or name of the container.

1. **Removing a Container:**
```
docker rm <container_id>
```
This command removes a stopped container. Replace `<container_id>` with the ID or name of the container.

1. **Removing an Image:**
```
docker rmi <image_id>
```
This command removes a Docker image. Replace `<image_id>` with the ID of the image you want to remove.

1. **Inspecting a Container:**
```
docker inspect <container_id>
```
This command provides detailed information about a specific container. Replace `<container_id>` with the ID or name of the container.

1.  **Running a Container in Detached Mode:**
```
docker run -d nginx:latest
```
This command runs a new container based on the Nginx image in detached mode (`-d`). The container runs in the background.
