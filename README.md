This program is designed to be executed in Linux.

This program returns an IP's latitude and longitude values, using the API provided by https://ipstack.com/.

With the base URL "http://api.ipstack.com/", the API key, and the IP address, we got the endpoint URL.

Before running the program we must confirm the following things:
•	The latest versions of the packages are installed, "sudo apt-get update" and "sudo apt-get updgrade"
•	Know the version of Python that we have installed. To do this, we must type in the Linux command line "python3 --version" for Python 3 or "python --version" for oldest Python versions. 
•	If is the first time that we are going to run the app, we must install the PIP (package manager for Python packages) we must type in the Linux command line "sudo apt install python3-pip" for Python 3 or "sudo apt install python-pip" for oldest Python versions. 
•	If we don't have the "requests" library installed, in the Linux command line we must type "pip3 install requests" for Python 3 or "pip install requests" for oldest Python versions.

To run this program, in the Linux command line, we must type "python3 get_latitude_longitude.py 'ip'" for Python 3 or "python get_latitude_longitude.py 'ip'" for oldest Python versions, in the 'ip' field, must type the IP from which you want to know the latitude and longitude.

As a manner of increasing security, the program has the next characteristics:
•	The program also checks that is executing independently.
•	The program checks if the call of the app is correctly input in the prompt line.
•	The program checks if the correct quantity of arguments is inputted.
•	The program manages exceptions which include:
        - HTTP request error.
        - Errors when making requests.
        - Error analyzing the JSON response.

As an example of running, in the Linux command line, we write: "python3 get_latitude_longitude.py 186.96.147.58" and we should get the output:
20.785789489746094 -103.4727783203125