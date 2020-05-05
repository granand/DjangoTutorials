# python manage.py migrate
# python manage.py makemigrations music
# python manage.py sqlmigrate music 0001

"""
python manage.py migrate

python manage.py makemigrations music

python manage.py shell

In [1]: from music.models import Album, Song

In [2]: Album.objects.all()
Out[2]: <QuerySet []>



In [4]: a = Album(artist='Ilayaraja',album_title='Nayagan',genre='Melody',album_logo='https://www.pngkit.com/png/full/254-2543115_endrendrum-raja-illayaraja-fridge-magnet-mus
   ...: ic-director-ilayaraja.png')

In [5]: a.save()

In [6]: a.artist
Out[6]: 'Ilayaraja'

In [7]: a.id
Out[7]: 1

In [8]: a.pk
Out[8]: 1

In [9]: b=Album()

In [10]: b.artist="ARRehman"

In [11]: b.album_title='Bombay'

In [12]: b.genre='Rock'

In [13]: b.album_logo='https://static.qobuz.com/images/covers/ya/77/y870vt3ew77ya_600.jpg'

In [14]: b.save()

In [16]: Album.objects.all()
Out[16]: <QuerySet [<Album: Album object (1)>, <Album: Album object (2)>]>

After creating the __str__  method

(base) Anands-MBP:mytunes Anand$ python manage.py shell
Python 3.7.4 (default, Aug 13 2019, 15:17:50)
Type 'copyright', 'credits' or 'license' for more information
IPython 7.8.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from music.models import Album, Song

In [2]: Album.objects.all()
Out[2]: <QuerySet [<Album: Nayagan by Ilayaraja>, <Album: Bombay by ARRehman>]>

In [3]: Album.objects.filter(id=1)
Out[3]: <QuerySet [<Album: Nayagan by Ilayaraja>]>

In [4]: Album.objects.filter(id=2)
Out[4]: <QuerySet [<Album: Bombay by ARRehman>]>

In [5]: Album.objects.filter(id=3)
Out[5]: <QuerySet []>

In [6]: Album.objects.filter(artist__startswith='ARR')
Out[6]: <QuerySet [<Album: Bombay by ARRehman>]>

In [7]: exit

#############

In [2]: from music.models import Album, Song

In [3]: album1 = Album.objects.get(pk=1)

In [4]: print(album1)
Nayagan by Ilayaraja

In [5]: song = Song()

In [6]: song.album = album1

In [7]: song.file_type='mp3'

In [8]: song.song_title='Nila Adhu Vanathumele'

In [9]: song.save()

In [10]: album1.song_set.all()
Out[10]: <QuerySet [<Song: Then Pandi Cheemayile>, <Song: Nila Adhu Vanathumele>]>

In [11]: album1.song_set.create(song_title='Andhi Mazhai Megam',file_type='mp3')
Out[11]: <Song: Andhi Mazhai Megam>

In [12]: album1.song_set.all()
Out[12]: <QuerySet [<Song: Then Pandi Cheemayile>, <Song: Nila Adhu Vanathumele>, <Song: Andhi Mazhai Megam>]>

In [13]: album1.song_set.create(song_title='Naan Sirithal Deepavali',file_type='mp3')
Out[13]: <Song: Naan Sirithal Deepavali>

In [14]: song = album1.song_set.create(song_title='Naan Sirithal Deepavali',file_type='mp3')

In [15]: song.song_title
Out[15]: 'Naan Sirithal Deepavali'

In [16]: album1.song_set.all()
Out[16]: <QuerySet [<Song: Then Pandi Cheemayile>, <Song: Nila Adhu Vanathumele>, <Song: Andhi Mazhai Megam>, <Song: Naan Sirithal Deepavali>, <Song: Naan Sirithal Deepavali>]>

In [17]: album1.song_set.all()
Out[17]: <QuerySet [<Song: Then Pandi Cheemayile>, <Song: Nila Adhu Vanathumele>, <Song: Andhi Mazhai Megam>, <Song: Naan Sirithal Deepavali>, <Song: Naan Sirithal Deepavali>]>

In [18]: album1.song_set.count()
Out[18]: 5

In [19]: exit


"""

from django.db import models

# Create your models here.
from django.db import models


class Album(models.Model):
    artist = models.CharField(max_length=100)
    album_title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=500)

    def __str__(self):
        return self.album_title + ' by ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=100)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title
