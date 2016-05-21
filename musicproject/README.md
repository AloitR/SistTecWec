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
Library: name, genere
Artist: nomArtista, tags, image, web, similars, summary, Library, user
Album: nomAlbum, tag, releasedate, image, web, artist, Library, user
Track: nomTrack, image, web, duration, playcount, published, summary, artist, album, Library user
```
### Subpages:
```
Main page: http://127.0.0.1:8000/musicapp/librarys
Login screen: http://127.0.0.1:8000/accounts/login
Logout screen: http://127.0.0.1:8000/accounts/logout/
Admin panel: http://127.0.0.1:8000/admin/
API: http://127.0.0.1:8000/musicapp/api/[librarys/artists/albums/tracks]
Media: http://127.0.0.1:8000/media/Music_App/[file]
```
### Default users:
```
Role - Username - Password

Admin: admin password123
User: aloit password123
User: yesid password123
```
