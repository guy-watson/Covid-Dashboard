# Covid Dashboard 
A simple covid dashboard that takes data from the UK Covid API (https://developer.api.nhs.uk/coronavirus/api), process it and displays it. 
The Dashboard also displays up-to-date and relevant news articles taken from NewsAPI (https://newsapi.org/).



## Authors

- [@guy-watson](https://github.com/guy-watson)


## Features

- Deletable news stories 
- Live updating data
- Scheduled updates by user
- Cross platform
- Location focus can be changed via config file 
- Logging 
- Simple to edit and modify to use other data sources 


## Installation

Python as well as Flask must be installed for the code to work.

Once the code has been dowloaded and Python is installed https://www.python.org/downloads/,
 use PIP to install flask via the command prompt using the following command:
```bash
pip install Flask
```

Then locate where the code has been installed via command prompt and run the interface using the command:
```bash
python user_interface.py
```
This will initalise the interface, to access the dashboard go to your browser and enter: 
```bash
http://127.0.0.1:5000/
```
You will then be directed to the dashboard. 
## Support

For support, email gw474@exeter.ac.uk
