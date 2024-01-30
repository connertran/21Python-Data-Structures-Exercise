def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    result = [phrase[0].upper()]
    for char in phrase[1:]:
        result.append(char)
    return ''.join(result)

