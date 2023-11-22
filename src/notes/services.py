from random_word import RandomWords


def get_new_random_title(max_length=50, word_count=4) -> str:
    title = " ".join(RandomWords().get_random_word() for _ in range(word_count))
    return title[:max_length] if len(title) > max_length else title
