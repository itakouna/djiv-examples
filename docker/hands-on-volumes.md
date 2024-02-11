Hands-on example demonstrating how to use Docker volumes:

1. **Create a Docker Volume:**
```
docker volume create my_volume
```
This command creates a named volume named `my_volume`.

1. **List Docker Volumes:**
```
docker volume ls
```
This command lists all Docker volumes on your system, including the one you just created (`my_volume`).

1. **Inspect Docker Volume:**
```
docker volume inspect my_volume
```
This command provides detailed information about the `my_volume` volume, including its mountpoint and other metadata.

1. **Run a Container with a Volume Mount:**
```
docker run -it --name my_container -v my_volume:/data ubuntu:latest
```
This command runs a new container named `my_container` based on the Ubuntu image in interactive mode (`-it`) and mounts the `my_volume` volume to the `/data` directory inside the container.

1. **Inside the Container:**
```
# Create a file in the mounted volume
echo "Hello, Docker Volumes!" > /data/hello.txt
```
This command creates a file named `hello.txt` inside the mounted volume `/data`.

1. **Exit the Container:**
```
exit
```
Exit the interactive shell inside the container.

1. **Inspect Volume Data:**
```
docker run -it --rm -v my_volume:/data ubuntu:latest ls /data
```
This command runs a temporary container with the `my_volume` volume mounted and lists the contents of the `/data` directory within the volume. You should see the `hello.txt` file created earlier.

1. **Cleanup:**
```
docker volume rm my_volume
```
This command removes the `my_volume` volume from your system.
