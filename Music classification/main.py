import eyed3, glob, os, shutil

artists = {}

files = glob.glob("./src path/*.mp3", recursive=True)

for file_name in files:
    audio = eyed3.load(file_name)

    name = audio.tag.artist
    title = audio.tag.title


    if name is None:
        name = "none"

    new_file_name = file_name
    
    if title is not None:
        new_file_name = "./src path/"+title+".mp3"
        print(new_file_name)
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
