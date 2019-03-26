# Spotify audio features downloader for data analysis projects

This tool **makes easy creating** your personal music dataset. 

```
python getScrobbles.py -u 'Your last.fm username' -k 'Your api key'
```
and..
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


#### Download audio features

```
python getAudioFeatures.py -sk 'Your spotify key' -ss 'Your spotify secret'
```

This script will find all tracks in spotify database based on scrobble.csv file. 

In order to retrieve audio features data we need spotify help.

Get your own spotify credentials ([ here](https://developer.spotify.com/dashboard/login)). We will use its spotify-key and spotify-secret as parameters.

Parameters  | Description
---    | --- 
Spotify key *-sk* *(required)* | self-explenatory
Spotify secret *-ss* *(required)* | self-explenatory





 


