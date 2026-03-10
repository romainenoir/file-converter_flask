import chardet


def encodeDetect(file_object=str):
    """_summary_

    Args:
        file__ (_type_, optional): _description_. returns encode detail

    Returns:
        _type_: encoding
    """
    # set pointer at the beginning
    file_object.seek(0)
    
    # the first 10kb should be read only 
    content = file_object.read(10000)
    
    # detect encoding
    result = chardet.detect(content)
    encoding = result.get('encoding')
    
    # reset pointer
    file_object.seek(0)
    
    return encoding if encoding else 'utf-8'
