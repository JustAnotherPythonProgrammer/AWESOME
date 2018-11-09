import youtube_dl, mutagen, os
from mutagen.id3 import ID3, TIT2, TALB, TPE1
os.chdir('C:\\Users\\User\\Desktop\\Programming\\Python\\ProgramRelatedStuff\\MusicBotFiles\\Output')
Links = open('C:\\Users\\User\\Desktop\\Programming\\Python\\ProgramRelatedStuff\\MusicBotFiles\\Links.txt', 'r')

Songs = []

def SortInfo(Link, Name, Artist, Album):
    FileName = ''
    for Thing in Name.split():
        FileName += Thing
    return {'Link':Link, 'FileName':FileName, 'Name':Name, 'Artist':Artist, 'Album':Album, 'Options':{'format':'bestaudio/best', 'extractaudio':True, 'outtmpl':FileName, 'noplaylist':True}}

def GetData(File):
    for Line in File:
        LineData = []
        for index, Thing in enumerate(Line.split('|')):
            if not index % 2:
                LineData.append(Thing)
        Songs.append(SortInfo(LineData[0], LineData[1], LineData[2], LineData[3]))

def Download():
    for Index, Song in enumerate(Songs):
        with youtube_dl.YoutubeDL(Songs[Index]['Options']) as ydl:
            ydl.download([Songs[Index]['Link']])
        os.system('rename ' + Songs[Index]['FileName'] + ' ' + Songs[Index]['FileName'] + 'OLD.mp3"')
        os.system('C:\\Users\\User\\Desktop\\Programming\\Python\\ProgramRelatedStuff\\MusicBotFiles\\ffmpeg-20181029-32d021c-win64-static\\bin\\ffmpeg -i C:\\Users\\User\\Desktop\\Programming\\Python\\ProgramRelatedStuff\\MusicBotFiles\\Output\\' + Songs[Index]['FileName'] + 'OLD.mp3 C:\\Users\\User\\Desktop\\Programming\\Python\\ProgramRelatedStuff\\MusicBotFiles\\Output\\' + Songs[Index]['FileName'] + '.mp3')
        os.system('del ' + Songs[Index]['FileName'] + 'OLD.mp3')

def AddMetaData():
    for Song in Songs:
        Tags = ID3('C:\\Users\\User\\Desktop\\Programming\\Python\\ProgramRelatedStuff\\MusicBotFiles\\Output\\' + Song['FileName'] + '.mp3')
        Tags['TIT2'] = TIT2(3, Song['Name'])
        if Song['Album'] != 'NONE':
            Tags['TALB'] = TALB(3, Song['Album'])
        Tags['TPE1'] = TPE1(3, Song['Artist'])
        Tags.save()
        
GetData(Links)
Download()
AddMetaData()
