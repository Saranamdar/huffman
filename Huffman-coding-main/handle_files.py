def modify_cmp_content(content):
    # get lines from content
    content_list = content.split('\n')
    char_n_dict = {}
    for line in content_list:
        if line =='--':
            # char_n_dict completed and now we have the binary codes
            content = '\n'.join(content_list[content_list.index(line)+1:])
            print(content)
            break
        char_n_dict[line[0]] = int(line[2:])

    return content,char_n_dict


def open_file(file_dir):
    # open file and return the content
    with open(file_dir,"r") as file:
        content = file.read()
    return content

def write_file(content,dir,name):
    # write content in a file with given format and save it in given dir
    with open(dir+name,"w") as file:
        file.write(content)




