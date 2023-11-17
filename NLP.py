import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import pos_tag
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')

def format_page(text):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)

    formatted_text = ""

    for sentence in sentences:
        # Tokenize each sentence into words
        words = word_tokenize(sentence)

        # Part-of-speech tagging to identify nouns, verbs, etc.
        tagged_words = pos_tag(words)

        # Remove stopwords (common words that don't contribute much to meaning)
        filtered_words = [word for word, tag in tagged_words if word.lower() not in stopwords.words('english')]

        # Determine if the sentence is a heading or a regular paragraph
        if len(filtered_words) > 0:
            first_word_tag = pos_tag([filtered_words[0]])[0][1]
            if first_word_tag.startswith('N') or first_word_tag.startswith('V'):
                # If the first word is a noun or a verb, consider it a heading
                formatted_text += f"\n\n<h1>{' '.join(filtered_words)}</h1>\n\n"
            else:
                # Otherwise, treat it as a regular paragraph
                formatted_text += f"<p>{' '.join(filtered_words)}</p>\n"

    return formatted_text


