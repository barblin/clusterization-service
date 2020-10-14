# clusterization-service

Get started with jupyter by going to https://jupyter.org/install.

When the notebook is opening in your browser - Success!

Now pick up a specific notebook from the resources folder and download the data from
https://github.com/JHL-HUST/AdaWaveClustering/tree/master/AdaWave/syntheticData

Make sure to update the paths in the python code to fit your environment.


# Steps to start the service locally
Open Power shell in your root directory

Set up your controller or app file for flask 
```
$env:FLASK_APP = "./sample/cluster_controller.py"
```

At last
```
flask run
```
This will start up the app under http://localhost:5000

# Maintaining your env
Start virtual environment
```
venv\Scripts\activate
```
Then do stuff :D


# Current supported api
```
/api/v1/version

/api/v1/clusters/data

/api/v1/clusters/data/files/<filename>

/api/v1/plots/files/<filename>

/api/v1/plots/clusters/<filename>
```

Example: http://localhost:5000/api/v1/version