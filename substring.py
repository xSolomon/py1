def is_substring(source : str, substring : str) -> bool:
    ''' Finds whether first string contains second as a substring. '''
    for i in range(0, len(source) - len(substring) + 1):
        for j in range(len(substring)):
            if source[i + j] != substring[j]:
                break
        else:
            return True
    return False
