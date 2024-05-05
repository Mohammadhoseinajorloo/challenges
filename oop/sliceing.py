import sys

def eslice_base_ext(filename: str):
    '''
    filename:str -> `base.extention`
    '''
    dot = filename.find(".")
    base = filename[:dot]
    extention = filename[dot+1:]
    return base, extention

if __name__ == "__main__":
    filename = sys.argv[1]
    base, extention = eslice_base_ext(filename)
    print(f'base: {base}\nextention: {extention}')
