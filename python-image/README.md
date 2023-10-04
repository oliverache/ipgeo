Instruction to build the docker image:
        "docker build -t ipgeo --rm ."    
        in this case, the image will be called "ipgeo", you can name the image as you want.

Instruction to create and run the docker container from the "ipgeo" image
        "docker run -it --name ipgeo_container --rm ipgeo"

Once inside the bash, to run the program we must type:
        "python get_latitude_longitude.py 123.123.123.123"   
        you must substitute "123.123.123.123" with the IP that you wish to know the latitude and longitude


useful commands
docker ps -a : list all Docker containers
docker ps : list the currently running Docker containers
docker stop "CONTAINER ID" : to stop a container