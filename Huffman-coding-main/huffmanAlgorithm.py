from collections import Counter
from data_structure import HuffmanTree,Node

def huffman_algorithm(char_n_dict):
    # create nodes
    list_of_nodes= [Node(n=n, char=char) for char,n in char_n_dict.items()]
    # create tree from nodes
    tree = HuffmanTree(list_of_nodes)
    root = tree.create_tree()
    # get codes for characters
    tree.create_binary_codes(root)
    return tree

def encoding(content):
    # count characters in content using Counter from collection lib
    char_n_dict = dict(Counter(content))
    try:
        char_n_dict.pop('\n')
    except:
        pass
    # create tree
    tree = huffman_algorithm(char_n_dict)
    # encoding---------------
    encoded_content = ''
    # add char_n dict to encoded content
    for char,n in char_n_dict.items():
        encoded_content += char +':'+ str(n) + '\n'
    encoded_content += '--\n'
    # replace characters with binary code
    for char in content:
        if char == '\n':
            encoded_content+='\n'
            continue
        code = tree.binary_codes_dict[char]
        encoded_content += code
    return encoded_content


def decoding(encoded_content,char_n_dict):
    # create tree
    tree = huffman_algorithm(char_n_dict)
    # create decode dict {code:char}
    chars = list(tree.binary_codes_dict.keys())
    codes = list(tree.binary_codes_dict.values())
    decode_dict = dict(zip(codes,chars))
    # decoding -----------------
    decoded_content = ''
    select_code = ''
    for c in encoded_content:
        select_code += c
        if c == '\n':
            decoded_content+='\n'
            select_code =''
        try:
            decoded_content+=decode_dict[select_code]
            select_code=''
        except:
            pass
    return decoded_content
