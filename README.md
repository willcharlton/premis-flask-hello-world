# Premis Hello World

A simple Hello World Flask app with a couple of other basic jobs to deploy with the [Premis](https://dev.premis.app/docs) application.

## Flask Server Networking Notes

The example job `.premis/jobs/flask-hello-world-server.premis` illustrates how you can deploy a web server or api to your local network. Adding DNS or diode publishing support for global name recognition would require another task in the `service` definition. The flask server's `Network` block uses `Mode: "host"` in order to expose the flask port `5000`. If you wanted to restrict this port to only be available to `localhost`, then you could change the network block to use `bridge` mode like what follows:

```
        "Networks": [
          {
            "Mode": "bridge",
            "DynamicPorts": [],
            "ReservedPorts": [
              {
                "Label": "http",
                "Value": 5000,
                "HostPort": 5000,
                "HostNetwork": "default"
              }
            ]
          }
        ],
```
