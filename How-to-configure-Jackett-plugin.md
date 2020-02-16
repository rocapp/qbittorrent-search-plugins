**qBittorrent** comes with few search plugins. Although it is enough for most users, if you wish to add more search engines you can configure the **Jackett plugin**.

**[Jackett](https://github.com/Jackett/Jackett)** provides support for more than 400 torrent sites (public and private).

### Disable Jackett plugin
By default, Jackett plugin is enabled. If you want to disable it, follow the next steps:
1. In `Search tab`, click in the `Search plugins...` button (bottom right)
2. Right click over the `Jackett` plugin
3. Uncheck the `Enabled` checkbox
4. Close the modal window

### Configuration file
Jackett plugin uses an external configuration file. This allows to update the plugin without losing the settings.

The file `jackett.json` should be located in qBittorrent search engines folder:
* Windows: `%localappdata%\qBittorrent\nova3\engines\`
* Linux: `~/.local/share/data/qBittorrent/nova3/engines/`
* OS X: `~/Library/Application Support/qBittorrent/nova3/engines/`

Note: If you use Python 2 instead of Python 3, replace `nova3` with `nova`

Note 2: If the file doesn't exist, you can create it copying the following json:
```
{
    "api_key": "YOUR_API_KEY_HERE", 
    "tracker_first": false, 
    "url": "http://127.0.0.1:9117"
}
```

### Configuration properties
| Property |  Default value |  Description |
|---|---|---|
| api_key | YOUR_API_KEY_HERE | Jackett API Key (you can find it on top of Jackett UI) |
| tracker_first | false | (false/true) add tracker name to the beginning of search result |
| url | http://127.0.0.1:9117 | Jackett URL (without the end slash) |

### Screenshot
![](https://i.imgur.com/uCawgLa.png)
