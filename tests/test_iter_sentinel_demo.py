import io

from iter_sentinel_demo  import read_bytes_until


def test_read_bytes_until_stop_value():
    bytes_io = io.BytesIO(b'AAAABBBBSTOPCCCC')
    assert list(read_bytes_until(bytes_io, 4, b'STOP')) == [b'AAAA', b'BBBB']

def test_read_bytes_until_beginning_with_stop_value():
    bytes_io = io.BytesIO(b'STOPAAAABBBBCCCC')
    assert list(read_bytes_until(bytes_io, 4, b'STOP')) == []
