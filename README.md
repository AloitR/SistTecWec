# SistTecWec

Authors: Aloït Real & Yesid Quiroga

https://github.com/AloitR/SistTecWec

### Start the website
```
cd MusicProject
python manage.py runserver
```
### Data models:
```
Artist: nomArtista, tags, url, similars, summary, user
Album: nomAlbum, tag, releasedate, url, artista, user
Track: nomTrack, url, duration, playcount, published, summary, artista, album, user
```
### Subpages:
```
Main page: http://127.0.0.1:8000/
Login screen: http://127.0.0.1:8000/login/
User page: http://127.0.0.1:8000/user/[username]/
Admin panel: http://127.0.0.1:8000/admin/
JSON Artists: http://127.0.0.1:8000/api/artist.json/
JDON Albums: http://127.0.0.1:8000/api/album.json/
JSON Tracks: http://127.0.0.1:8000/api/track.json/
```
### Default users:
```
Role - Username - Password

Admin: admin password
User: aloit aloit
User: yesid yesid
```
