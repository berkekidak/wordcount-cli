from wordcount import count_text


def test_count_text_basic():
    text = "hello world\nthis is a test\n"
    lines, words, chars = count_text(text)
    assert lines == 2
    assert words == 6
    assert chars == len(text)


def test_count_text_empty():
    lines, words, chars = count_text("")
    assert lines == 0
    assert words == 0
    assert chars == 0
