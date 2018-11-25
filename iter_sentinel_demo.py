def read_bytes_until(bytes_io, bytes_to_read, stop_value):
    """
    Return an iterable that yield bytes_to_read bytes from bytes_io untill stop_value is met
    >>> import io
    >>> bytes_io = io.BytesIO(b'XXXYYYZZZAAA')
    >>> for bytes in read_bytes_until(bytes_io, 3, b'ZZZ'): print(bytes)
    b'XXX'
    b'YYY'
    """
