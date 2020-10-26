from flask import Flask, json, request

api = Flask(__name__)

metric_data={
}

# Gets the report
@api.route('/report', methods=['GET'])
def get_report():
  if len(metric_data)==0:
      return "No metrics exists at server", 500

  res=[]
  for key,values in metric_data.items():
      dictlocal = { "ip": key, "max_cpu":values["max_cpu"], "max_memory": values["max_mem"]   }
      res.append(dictlocal)
  return json.dumps(res), 200


# Stores the input metric in In-Memory
@api.route('/metrics', methods=['POST'])
def post_metrics():
  global metric_data
  ip=request.remote_addr
  cpu = request.get_json()["percentage_cpu_used"]
  mem = request.get_json()["percentage_memory_used"]
  try:
      if metric_data.get(ip):
          current_cpu, current_mem = metric_data[ip]["max_cpu"], metric_data[ip]["max_mem"]
          if cpu > current_cpu:
              metric_data[ip]["max_cpu"] = cpu
          if mem > current_mem:
              metric_data[ip]["max_mem"] = mem
      else:
          metric_data = {ip: { "max_cpu": cpu, "max_mem": mem}}

      return json.dumps({"Metric stored for IP": ip}), 200
  except Exception as e:
      return json.dumps({"Could not insert metric. Exception": e}), 500


if __name__ == '__main__':
    api.run(host='0.0.0.0', port="8080")
