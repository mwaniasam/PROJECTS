from collections import Counter
import string


def clean_words(document):
    """Return lowercase words with punctuation removed for word analysis."""
    return [word.strip(string.punctuation).lower() for word in document.split() if word.strip(string.punctuation)]


def count_words(document):
    """Count how many words are in the document."""
    return len(clean_words(document))


def count_sentences(document):
    # Note: abbreviations like Mr. or Dr. will be
    # counted as sentence endings; known limitation
    """Count sentences using ., !, and ? as sentence endings."""
    sentence_endings = ".!?"
    return sum(1 for char in document if char in sentence_endings)


def count_paragraphs(document):
    """Count non-empty paragraphs separated by new lines."""
    paragraphs = [line for line in document.split("\n") if line.strip()]
    return len(paragraphs)


def find_longest_word(document):
    """Return the longest word in the document, or None when empty."""
    words = clean_words(document)
    if not words:
        return None
    return max(words, key=len)


def find_most_common_word(document):
    """Return the most common word in the document, or None when empty."""
    words = clean_words(document)
    if not words:
        return None
    return Counter(words).most_common(1)[0][0]


def text_statistics(document):
    """Run all text statistics and print a readable summary."""
    stats = {
        "word_count": count_words(document),
        "sentence_count": count_sentences(document),
        "paragraph_count": count_paragraphs(document),
        "longest_word": find_longest_word(document),
        "most_common_word": find_most_common_word(document),
    }

    print("Text Statistics:")
    print(f"- Words: {stats['word_count']}")
    print(f"- Sentences: {stats['sentence_count']}")
    print(f"- Paragraphs: {stats['paragraph_count']}")
    print(f"- Longest word: {stats['longest_word']}")
    print(f"- Most common word: {stats['most_common_word']}")

    return stats


if __name__ == "__main__":
    user_text = input("Enter text: ")
    text_statistics(user_text)
