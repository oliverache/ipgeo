#import librarys
import requests                         
import sys        

api_key = "75bf8796c92a97d24857a9857dbf1e73" #global variable, security key provided by ipstack
                                            
def get_latitude_longitude(ip, api_key):
    #getting the endpoint_url
    base_url = "http://api.ipstack.com/" 
    endpoint_url = f"{base_url}{ip}?access_key={api_key}"

    try:
        response = requests.get(endpoint_url) # http request to the "endpoint_url"
        response.raise_for_status()  #checking if there is HTTP request error
        data = response.json() #get the JSON to analyze it.
        latitude = data["latitude"] #getting the value of the key "latitude"
        longitude = data["longitude"] #getting the value of the key "longitude"

        return latitude, longitude
    
    except requests.exceptions.HTTPError as e:  #exception to check that the HTTP answer is an error
        print(f"HTTP request error: {e}")
        sys.exit(1) 
    except requests.exceptions.RequestException as e: #exception to check errors in the HTTP request
        print(f"Error when making request: {e}")
        sys.exit(1)
    except KeyError as e: #exception to check that the 'key' that we are checking, exists.
        print(f"Error analizing the JSON response: {e}")
        sys.exit(1)

if __name__ == "__main__":   # checking if the python app is executing independently.
    if len(sys.argv) != 2:   # check that the quantity of arguments is two
        print("something were wrong, the correct call of the app is: python3 get_latitude_longitude.py 'ip'") #message in case of an error in the quantity of arguments in the calling
        sys.exit(1) 
    ip_direction = sys.argv[1] #assigns first value provided to the 'ip_direction' variable.

    latitude, longitude = get_latitude_longitude(ip_direction, api_key) #unpack the values.

    #Output latitude & longitude as text
    sys.stdout.write(f"{latitude} {longitude}")