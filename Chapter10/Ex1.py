def lay_file(path):
    return path.split("\\")[-1]

def lay_ten(path):
    return path.split("\\")[-1].split(".")[0]

print(lay_file("d:\\music\\muabui.mp3"))
print(lay_ten("d:\\music\\muabui.mp3"))