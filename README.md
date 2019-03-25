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
pip instal -r requirements.txt
```

### Usage

#### Download scrobbles

```
python getScrobbles.py -u 'Your last.fm username' -k 'Your api key'
```

After running this command, you will get all scrobbles saved to .csv format in the /folder_name/data folder.

Parameters  | Description
---    | --- 
Username *-u* *(required)* | The first parameter should be last.fm username. This script collects all scrobbles data. More information about ***used api-endpoint*** ([ here](https://www.last.fm/api/show/user.getRecentTracks))
Api Key *-k* *(required)* | In order to get last.fm data, api key is required. You can easily get your own ([here](https://www.last.fm/api/account/create))





 


