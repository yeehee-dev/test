import os

# def search():
    # file_names = os.listdir(dir)
    # for file_name in file_names:
    #     full_filenames = os.path.join(dir, file_name)
    #     if os.path.isdir(full_filenames):
    #         search(full_filenames)
    #     else: 
    #         ext = os.path.splitext(full_filenames)[-1]
    #         if ext == ".py":
    #             print(full_filenames)



# search("C:/Users/한예희/Desktop/python")
for (path, dir, files) in os.walk("C:/Users/한예희/Desktop/python"):
    for file_name in files:
        ext = os.path.splitext(file_name)[-1]
        if ext == '.py':
            print("%s%s" %(path, file_name))