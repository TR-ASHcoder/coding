import azapi

API = azapi.AZlyrics('google', accuracy=1.0)

API.artist = 'kanye wes'
API.title = 'bound 2'

API.getLyrics(save=True, ext='lrc')

print(API.lyrics)

# Correct Artist and Title are updated from webpage
print(API.title, API.artist)