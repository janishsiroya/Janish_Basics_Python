import os
for dirname in os.listdir("."):
    if os.path.isdir(dirname):
        for i, filename in enumerate(os.listdir(dirname)):
            os.rename(dirname + "/" + filename, dirname + "/" + str(i) + ".jpg")