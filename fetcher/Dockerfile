# Maven build container
FROM maven:3.8.4-openjdk-17-slim as MAVEN_BUILD

COPY pom.xml /tmp/
COPY src /tmp/src/

WORKDIR /tmp/

RUN mvn package

# Build openjdk container
FROM openjdk:17-alpine

COPY --from=MAVEN_BUILD /tmp/target/fetcher-1.0-SNAPSHOT.jar /fetcher.jar

CMD ["java", "-jar", "/fetcher.jar"]
