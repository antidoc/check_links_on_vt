This script checks links, provided in links.txt, on VirusTotal and returns links on VirusTotal URL check result pages.

To use this script you should install dependencies from requirements.txt

pip install -r requirements.txt

Then you should add your VirusTotal API key to file called api

Finally you should add links that you need to check, to file called links.txt, every link should be started from new line

Then you should execute main.py, all result will be in result.txt file


Because of VirusTotal API limits(4 requests/min) this script can take long time, so start this script, make some coffee and find some other work to do while script is executing)
