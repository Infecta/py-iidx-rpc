# py-iidx-rpc
**py-iidx-rpc** is a simple rpc implementation which works together with [Radioo's ](https://github.com/Radioo/TickerHook) TickerHook to show your friends what charts you're playing on discord.

![Picture of RPC in Action](https://cdn.discordapp.com/attachments/832618563226304582/1062439241155608646/image.png)

## Credits
[Radioo](https://github.com/Radioo) for developing [TickerHook](https://github.com/Radioo/TickerHook)

## How to use

### This assumes you already got [TickerHook](https://github.com/Radioo/TickerHook) up and running

### NOTE: Currently the game has to run before running the rpc

### From the [Releases](https://github.com/Infecta/py-iidx-rpc/releases) section
1. Place `py-iidx-rpc.exe` into a folder and run
2. A `config.json` should be generated and you should edit that to suit your needs
Scroll down to see how to configure
3. Run it!

### From Source

Pre-Requisites: Python 3.11.1

1.  Clone or download the repo
2.  [OPTIONAL, BUT RECOMMENDED] Create a virtual environment
3. Open a terminal and run `pip install -r requirements	`
4. Edit `config.json` to suit your needs
5. Run `py main.py`

## Configuration
When running the program for the first time, It will generate a `config.json` file

```
# config.json 
{

"ip":  "localhost",

"port":  "10573",

"appID":  "1062281237269598288",

"image":  "main-image",

"image_text":  "beatmania IIDX",

"other_text":  "Grinding Kaiden Probably"

}
```

- `ip` refers to the IP address of where the hook is running on. You shouldn't need to edit this because you would most likely run this on the same computer where the game is running on
- `port` refers to the Hook's websocket port, unless you're running a custom build of [Radioo's Ticker Hook](https://github.com/Radioo/TickerHook) which is running on a different port, there is no need to change this.
- `appID` refers to the [Discord Application](https://discord.com/developers/applications) client ID to source it's assets. By default it uses my application, it's also possible to use your own. Do your own research on this one.
- `image` refers to the name of the art assets that are uploaded in the discord application's rich presence art assests section
- `image-text` refers to the text that appears when hovering over the image in the RPC
- `other-text` is the text below the ticker output




