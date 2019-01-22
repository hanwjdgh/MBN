import eyed3, glob, os, shutil

artists = {}

files = glob.glob("./src path/*.mp3", recursive=True)

for file_name in files:
    audio = eyed3.load(file_name)

    if audio.tag is None:
        basename = os.path.basename(file_name)
        lst = re.split("[-_]",basename)
        
        audio.initTag()
        audio.tag.artist = lst[0].replace(" ","")
        audio.tag.title = lst[1].split('.')[0][1:]
        audio.tag.save()

    else:
        name = audio.tag.artist
        title = audio.tag.title


        if name is None:
            name = "none"

        new_file_name = file_name
    
        if title is not None:
            new_file_name = "./src path/"+title+".mp3"
            os.rename(file_name, new_file_name) 
    
    c_path = "./dst path/" + name + "/"
   
    if name not in artists:
        artists[name] = 1
        if not(os.path.isdir(c_path)):
            os.mkdir(c_path)
        shutil.copy(new_file_name, c_path)
    else:
        artists[name] += 1
        shutil.copy(new_file_name, c_path)
