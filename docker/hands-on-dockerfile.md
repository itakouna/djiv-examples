Hands-on example of using a Dockerfile to build a simple Docker image and then running a container from that image:

1. Create a new directory for your Docker project:
```
mkdir docker-hands-on
cd docker-hands-on
```

1. Create a file named `Dockerfile` (without any file extension) in the directory and open it in a text editor:
```
touch Dockerfile
nano Dockerfile
```

1. Add the following content to the `Dockerfile`:
```Dockerfile
# Use the official Python image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Run app.py when the container launches
CMD ["python", "app.py"]
```

4. Create a Python script named `app.py` in the same directory:
```
echo "print('Hello, Docker!')" > app.py
```

5. Build the Docker image using the `docker build` command:
```
docker build -t my-python-app .
```
This command builds a Docker image based on the instructions in the `Dockerfile` and tags it with the name `my-python-app`.

6. Once the image is built, you can run a container from it using the `docker run` command:
```
docker run my-python-app
```
This command starts a new container based on the `my-python-app` image and executes the `app.py` script inside the container, which prints "Hello, Docker!" to the console.
