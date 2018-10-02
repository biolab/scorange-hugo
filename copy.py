import glob
import shutil


def add_front_matter(file):
    front_matter = "+++\n"

    with open(file, 'r+') as f:
        content = f.readlines()
        front_matter += '"title" = "' + content[0].strip()+'"\n'
        icon = next(ele for ele in content if "![]" in ele)
        front_matter += '"icon" = "' + icon[icon.find("(")+1: icon.find(")")]+'"\n'
        front_matter += "+++\n"
        front_matter += ''.join(map(str, content))
        f.close()
    return front_matter


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
                print(file_to_copy)
                if '.' in file_to_copy:
                    text = add_front_matter(file_to_copy)
                    with open(location + file_to_copy.split("/")[-1], 'w') as tmp:
                        tmp.write(text)
                        tmp.close()
        # copy file
        elif '*' not in x and '.' in x:
            text = add_front_matter(x)
            with open(location+x.split("/")[-1], 'w') as tmp:
                tmp.write(text)
                tmp.close()

        # copy all files recursive from folder
        elif '**' in x:
            files_in_folder = glob.glob(x, recursive=True)
            for file_to_copy in files_in_folder:
                if '.' in file_to_copy:
                    print(file_to_copy)
                    text = add_front_matter(file_to_copy)
                    with open(location + file_to_copy.split("/")[-1], 'w') as tmp:
                        tmp.write(text)
                        tmp.close()




