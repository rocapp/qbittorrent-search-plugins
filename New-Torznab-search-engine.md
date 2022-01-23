This guide will help you to configure the the new qBittorrent search engine.

## Deprecation notice

Until version 4.5.0, qBittorrent had a native search engine based on Python. qBittorrent team was in charge of checking the installation of Python and the maintenance of the [search plugins](https://github.com/qbittorrent/search-plugins) for the torrent sites. There were also [unofficial plugins](https://github.com/qbittorrent/search-plugins/wiki/Unofficial-search-plugins) maintained by the community.

Over the time, maintaining this system has become a burden due to the large number of torrent sites and the lack of developers with knowledge of Python.
Since version 4.5.0 the native search engine is replaced with a new search engine that makes calls to [Torznab compatible APIs](https://torznab.github.io/spec-1.3-draft/torznab/Specification-v1.3.html). This implies that the end user has to install additional software to perform searches in qBittorrent.

## Torznab clients

[Torznab](https://torznab.github.io/spec-1.3-draft/torznab/Specification-v1.3.html) is an API specification based on the Newznab WebAPI. The API is built around a simple XML/RSS feed with filtering and paging capabilities.
