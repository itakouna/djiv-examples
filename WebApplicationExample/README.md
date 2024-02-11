# Containerize A Spring Boot Todo Application

- clone this repo https://github.com/llutsefer/TodoWebApplication
  ```bash
  git clone https://github.com/llutsefer/TodoWebApplication.git
  ```
- use the Dockerfile to build an image for TodoWebApplication
- run the application
  ```bash
  docker run -v $PWD:/tmp -p 8080:8080 tasks
  ```
