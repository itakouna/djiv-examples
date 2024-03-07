FROM alpine
## Combine ENTRYPOINT with CMD
#ENTRYPOINT ["echo", "Hello"]
#CMD ["Google World"]
# only ENTRYPOINT
ENTRYPOINT ["echo", "my name is"]
#CMD ["echo", "Google World"]
