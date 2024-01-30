FROM maven:3.8.4-openjdk-17
WORKDIR /app
COPY TodoWebApplication/ .
RUN mvn clean package
ENTRYPOINT [ "mvn", "spring-boot:run"]
