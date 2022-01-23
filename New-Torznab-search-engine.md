This guide will help you to configure the the new qBittorrent search engine.

## Deprecation notice

Until version 4.5.0, qBittorrent had a native search engine based on Python. qBittorrent team was in charge of checking the installation of Python and the maintenance of the [search plugins](https://github.com/qbittorrent/search-plugins) for the torrent sites. There were also [unofficial plugins](https://github.com/qbittorrent/search-plugins/wiki/Unofficial-search-plugins) maintained by the community.

Over the time, maintaining this system has become a burden due to the large number of torrent sites and the lack of developers with knowledge of Python.
Since version 4.5.0 the native search engine is replaced with a new search engine that makes calls to [Torznab compatible APIs](https://torznab.github.io/spec-1.3-draft/torznab/Specification-v1.3.html). This implies that the end user has to install additional software to perform searches in qBittorrent.

## Torznab clients

[Torznab](https://torznab.github.io/spec-1.3-draft/torznab/Specification-v1.3.html) is an API specification based on the Newznab WebAPI. The API is built around a simple XML/RSS feed with filtering and paging capabilities.

There are several software compatible with this specification. Its goal is to support as many torrent sites as possible, parse the content and convert the format into Torznab format so it can be consumed by other applications such as qBittorrent. 

These are the most popular applications:
* [Jackett](https://github.com/Jackett/Jackett): **(recommended)**. It supports more than 500 torrent sites.
* [Prowlarr](https://github.com/Prowlarr/Prowlarr): It supports the same sites as Jackett but with more modern UI.
* [NZB Hydra](https://github.com/theotherp/nzbhydra2): It includes more features but supports less torrent sites.
* [Cardigann](https://github.com/cardigann/cardigann): Some sites still work, but it is no longer maintained.