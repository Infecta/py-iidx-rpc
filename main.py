import websocket  # Websocket Lib
from pypresence import Presence  # Main RPC Lib
import json  # JSON Parsing
from os.path import exists  # File Existence Check

# Check if config.json exists, if not create one with a template, else continue execution
configCheck = exists('./config.json')

if not configCheck:
    configSchema = {
        "ip": "localhost",
        "port": "10573",
        "appID": "1062281237269598288",
        "image": "main-image",
        "image_text": "beatmania IIDX",
        "other_text": "Grinding Kaiden Probably"
    }

    with open('config.json', 'w') as outfile:
        json.dump(configSchema, outfile, indent=4)

    print('Please edit config.json to fit your needs!')
    input("Press Enter to continue...")
    quit()
else:
    pass

# Import Config File
configFile = open('./config.json')
config = json.load(configFile)

# Initialize RPC Client
appID = config['appID']
rpcClient = Presence(appID)
rpcClient.connect()

# Connection URI (Configurable in config.json)
uri = "ws://" + config['ip'] + ":" + config['port']

# Print somthing so user doesn't freak out like it's not working
print(r'=================================')
print(r'|        python-iidx-rpc        |')
print(r'|        </> by Infecta         |')
print(r'=================================')
print('[INFO] RPC Running')



# RPC Updating Shenanigans
def on_message(ws, ticker_response):
    rpcClient.update(
        large_image=config['image'],
        large_text=config['image_text'],
        details=ticker_response,
        state=config['other_text']
    )


ws = websocket.WebSocketApp(uri, on_message=on_message)
ws.run_forever()
