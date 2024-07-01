import requests
import json

# Define the data to send in JSON format




def saveData(name):
    
    data_to_send = {
        'name':name
        
    }

    # URL of your PHP script
    php_script_url = 'http://localhost/project/demo.php'  # Replace with your actual URL

    # Send a POST request to the PHP script
    response = requests.get(php_script_url, params=data_to_send)

    # Print the response from the PHP script

    print(response)
    print(response.text)


# saveData("anu")