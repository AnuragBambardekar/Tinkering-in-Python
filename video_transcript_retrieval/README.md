# Tinkering in Python
Just tinkering and finding new things to learn in Python

## `youtube-transcipt-api` 
It is a python API which:
- fetches subtitles (transcripts) from YouTube videos without using the YouTube Data API (No API key, No OAuth)
- supports translating subtitles
- does not require a headless browser like other selenium based solutions
- Under the hood, it hits the same caption endpoints YouTube uses in the browser.

**Perfect for:**
- 🔍 NLP / ML on video content
- 📝 Summarization
- 📚 Building knowledge bases from talks/tutorials
- 🤖 RAG pipelines (YouTube → embeddings → vector DB)
- 📊 Analyzing lecture content
- Library allows CLI usage so users can directly call the API and pass in-line args

```
youtube_transcript_api <first_video_id> <second_video_id> --http-proxy http://user:pass@domain:port --https-proxy https://user:pass@domain:port
```

**Not good for:**
- Private videos
- Members-only / paywalled videos
- Videos with captions disabled
- and rate-limited by YT

## Installation
```
pip install youtube-transcript-api
```

## Major Drawback and potential workaround as referenced in README of the library on GitHub
https://github.com/jdepoix/youtube-transcript-api?tab=readme-ov-file#working-around-ip-bans-requestblocked-or-ipblocked-exception

- You can work around these IP bans using proxies. However, since YouTube will ban static proxies after extended use, going for rotating residential proxies provide is the most reliable option.

- Once you have created a Webshare account and purchased a "Residential" proxy package that suits your workload (make sure NOT to purchase "Proxy Server" or "Static Residential"!), open the Webshare Proxy Settings to retrieve your "Proxy Username" and "Proxy Password". Using this information you can initialize the YouTubeTranscriptApi as follows:

```
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.proxies import WebshareProxyConfig

ytt_api = YouTubeTranscriptApi(
    proxy_config=WebshareProxyConfig(
        proxy_username="<proxy-username>",
        proxy_password="<proxy-password>",
    )
)

# all requests done by ytt_api will now be proxied through Webshare
ytt_api.fetch(video_id)
```

- Using the `WebshareProxyConfig` will default to using rotating residential proxies and requires no further configuration.

You can also limit the pool of IPs that you will be rotating through to those located in specific countries. By choosing locations that are close to the machine that is running your code, you can reduce latency. Also, this can be used to work around location-based restrictions.

```
ytt_api = YouTubeTranscriptApi(
    proxy_config=WebshareProxyConfig(
        proxy_username="<proxy-username>",
        proxy_password="<proxy-password>",
        filter_ip_locations=["de", "us"],
    )
)

# Webshare will now only rotate through IPs located in Germany or the United States!
ytt_api.fetch(video_id)
```

### Using other Proxy solutions
- Alternatively to using Webshare, you can set up any generic HTTP/HTTPS/SOCKS proxy using the GenericProxyConfig class:

```
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.proxies import GenericProxyConfig

ytt_api = YouTubeTranscriptApi(
    proxy_config=GenericProxyConfig(
        http_url="http://user:pass@my-custom-proxy.org:port",
        https_url="https://user:pass@my-custom-proxy.org:port",
    )
)

# all requests done by ytt_api will now be proxied using the defined proxy URLs
ytt_api.fetch(video_id)
```

- Be aware that using a proxy doesn't guarantee that you won't be blocked, as YouTube can always block the IP of your proxy! Therefore, you should always choose a solution that rotates through a pool of proxy addresses, if you want to maximize reliability.

## References
- [Documentation](https://pypi.org/project/youtube-transcript-api/)