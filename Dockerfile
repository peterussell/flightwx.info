# Build the project using maven container
FROM maven:3.8.4-openjdk-17-slim as MAVEN_BUILD
COPY ./fetcher/ ./
RUN mvn clean package
