# airmeet-assignment

How to build and run image:<br>
Method1:
```
git clone git@github.com:abhisoniks/airmeet-assignment.git
cd airmeet-assignment/metric-reporter
docker build -t airmeet-assignment .
docker run --name airmeet-assignment -p 8000:5000 airmeet-assignment
```
Method2:
```
docker pull abhisonidx/airmeet-assignment:latest
docker run --name airmeet-assignment -p 8000:5000 abhisonidx/airmeet-assignment
```

How to Post Metric:
```
curl -k -XPOST -H "Content-Type: application/json" --data '{"percentage_cpu_used": 55, "percentage_memory_used": 990}' http://127.0.0.1:8000/metrics
curl -k -XPOST -H "Content-Type: application/json" --data '{"percentage_cpu_used": 55, "percentage_memory_used": 9900}' http://127.0.0.1:8000/metrics
curl -k -XPOST -H "Content-Type: application/json" --data '{"percentage_cpu_used": 595, "percentage_memory_used": 990}' http://0.0.0.0:8000/metrics
```

How to Get Report:
```
- Access http://localhost:8000/report on the browser
- curl http://localhost:8000/report on terminal
```

