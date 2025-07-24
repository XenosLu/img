# https://hub.docker.com/_/python
FROM openjdk:8-jdk-alpine
LABEL maintainer="xenos <xenos.lu@gmail.com>"
WORKDIR /usr/src/app
RUN apk add --no-cache curl && \
    curl -o firestore-emulator.jar https://storage.googleapis.com/firebase-preview-drop/emulator/cloud-firestore-emulator-v1.13.1.jar
EXPOSE 8080
CMD ["java", "-jar", "firestore-emulator.jar", "--host=0.0.0.0", "--port=8080"]
