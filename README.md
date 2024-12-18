# FakeNewsDS


## Scrap Youtube News Videos(this will download URLs only)

setup a youtube API 3  in google cloud using your account.

https://developers.google.com/youtube/v3/getting-started


```
python 1.ScrapYTNews.py
```

## Download Youtube Videos

For loading ffmpeg on newton:
```
> module avail ffmpeg

ffmpeg/ffmpeg-7.0.2-gcc-12.2.0    ffmpeg/ffmpeg-7.0.2-with-cuda

> module load ffmpeg/ffmpeg-7.0.2-gcc-12.2.0
```

Follow setup from 
1. https://github.com/yt-dlp/yt-dlp or
2. https://github.com/ytdl-org/youtube-dl

use this repo to downlod videos using URLS: https://github.com/SpencerWhitehead/NewsVideoDataset

Change the urls.txt file with the one obtained using 1.ScrapYTNews.py.


## Get video descriptions using Video-LLAVA-OV

clone repo : https://github.com/ajaymin28/LLaVA-NeXT.git
and copy 2.Infer_fake_news_dataset.py to the root of this repo.

Change videos path in 2.Infer_fake_news_dataset.py(line 285) accordingly.

```
CUDA_VISIBLE_DEVICES=0 python LLaVA-NeXT/Infer_fake_news_dataset.py \
    --output_dir=FakeNewsDS/LLLAVA_OV_OUTPUT \
    --conv-mode=qwen_2
```

This will save video descriptions in output directory for each video.


## Get audio transcripts

Change videos path, audio save path as well as transcripts save path in 3.TranscribeVideo.py

```
python 3.TranscribeVideo.py
```

This will save audio transcripts


## Take video captions, audio transcripts to LASER

```
TO DO
```

## References

1. https://github.com/ICTMCG/Awesome-Misinfo-Video-Detection
