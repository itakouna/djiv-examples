# Use a base image from the official mavenDocker Hub repository
FROM maven:3.8.4-openjdk-17
# Set the working directory inside the container
WORKDIR /app
# Copy package.json and package-lock.json to the working directory
COPY TodoWebApplication/ .
# Build Java package
RUN mvn clean package
# Define the command to start the application when the container starts
ENTRYPOINT [ "mvn", "spring-boot:run"]
