import glob
import shutil

# find all .include_hugo files in content folder
files = glob.glob('content/**/.include_hugo', recursive=True)
# iterate over all files(.include_hugo) that were founded
for file in files:
    # read content
    with open(file, 'r') as f:
        content = f.readlines()

    content = [x.strip() for x in content]
    # save location(path) of file
    location = file.split('.')[0]

    # iterate over files included in .include_hugo file
    for x in content:
        # copy all files from folder
        if '*' not in x and '.' not in x:
            #
            files_in_folder = glob.glob(x+'/**', recursive=True)
            for file_to_copy in files_in_folder:
                if '.' in file_to_copy:
                    shutil.copy2(file_to_copy, location)
        # copy file
        elif '*' not in x and '.' in x:
            shutil.copy2(x, location)
        # copy all files recursive from folder
        elif '**' in x:
            files_in_folder = glob.glob(x, recursive=True)
            for file_to_copy in files_in_folder:
                if '.' in file_to_copy:
                    shutil.copy2(file_to_copy, location)
