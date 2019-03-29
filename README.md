# Spotify audio features downloader for data analysis projects

This tool is part of data-analysis series published on medium. Check it out (here)[https://medium.com/@m.w.bochniewicz/music-analysis-with-python-part-1-create-your-own-dataset-with-lastfm-and-spotify-8223a46fad4b] 

..and create ***your own music dataset*** in few steps.

```
python getScrobbles.py -u 'Your last.fm username' -k 'Your api key'
```
...

```
python getUris.py -sk 'Your spotify key' -ss 'Your spotify secret'
```
And..
```
python getAudioFeatures.py -sk 'Your spotify key' -ss 'Your spotify secret'
```
***That's all!***

Now your own music dataset is ready for some appealing analysis.

### Table of content

* [Pre-requirements](#pre-requirements)
* [Installation](#installation)
* [Usage](#usage)
  * [Download scrobbles](#download-scrobbles)
  * [Download uris](#download-uris)
  * [Download audio features](#download-audio-features)
  
### Pre-requirements

This project is tested with Python 3.6 and more.

### Installation

Git clone the project

Get the python dependecies

```
pip install -r requirements.txt
```

Create data directory
```
python prepare_directory.py
```


### Usage

#### Download scrobbles

```
python getScrobbles.py -u 'Your last.fm username' -k 'Your api key'
```

This script collects all last.fm data saved to .csv format in the /folder_name/data folder. 

More information about ***used api-endpoint*** ([ here](https://www.last.fm/api/show/user.getRecentTracks)) 

Parameters  | Description
---    | --- 
Username *-u* *(required)* | The first parameter should be last.fm username. 
Api Key *-k* *(required)* | In order to get last.fm data api key is required. You can easily get your own ([here](https://www.last.fm/api/account/create))

#### Download uris

```
python getUris.py -sk 'Your spotify key' -ss 'Your spotify secret'
```

This script collects all spotify uris and saved them to .csv format in the /folder_name/data folder. 

In order to retrieve uris data we need spotify help.

Get your own spotify credentials ([ here](https://developer.spotify.com/dashboard/login)). We will use its spotify-key and spotify-secret as parameters.

Parameters  | Description
---    | --- 
Spotify key *-sk* *(required)* | self-explenatory
Spotify secret *-ss* *(required)* | self-explenatory


#### Download audio features

```
python getAudioFeatures.py -sk 'Your spotify key' -ss 'Your spotify secret'
```

This script creates audio features of each track based on uris.csv file. 

Parameters  | Description
---    | --- 
Spotify key *-sk* *(required)* | self-explanatory
Spotify secret *-ss* *(required)* | self-explanatory





 


