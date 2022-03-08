# envoy-proxy-demo

There are two application here. 

### 1. Green light
This application has been written on node. Just run

```sh buildAndRun.sh```

It will build and run the application in a container. 

### 2. Red light
This application has been written on python. Just run

```sh buildAndRun.sh```

It will build and run the application in a container. 

### Envoy
* Install enovy
* go to envoy directory in this package and run the command below: 
```envoy -c config.yaml```

### Verification
call 
```
curl http://localhost:10000/red 

or 

curl http://localhost:1000/green
```
