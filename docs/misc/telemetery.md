

```sh
git clone -b main https://github.com/SigNoz/signoz.git --depth=1
cd signoz/deploy

# Comment services ::  load-hotrod: hotrod:

docker-compose up -d
# http://localhost:3301/

docker-compose down -v

```

https://signoz.io/docs/operate/docker-standalone/#remove-the-sample-application-from-signoz-dashboard

https://opentelemetry.io/docs/specs/otel/configuration/sdk-environment-variables/
https://opentelemetry.io/docs/languages/python/automatic/example/


https://signoz.io/blog/opentelemetry-docker/
```sh
docker run -p 8080:80 -d nginx:latest
docker run  -p 8081:80 -d httpd:latest

```