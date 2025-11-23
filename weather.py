#So basically this will be my first py script to use an API, I guess we making strides.
#Still on my learning path of Modules and packages

import requests
response = requests.get("https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&appid={e4b152da92ba1158b5ce1f18e62e4bea}")

print(response)