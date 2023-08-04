import nltk
from nltk.tokenize import word_tokenize


def tokenize_text(text):
    tokens = word_tokenize(text)
    return tokens


def remove_stopwords(tokens):
    stopwords = nltk.corpus.stopwords.words('english')
    filtered_tokens = [token for token in tokens if token.lower() not in stopwords]
    return filtered_tokens


def lemmatize_tokens(tokens):
    lemmatizer = nltk.stem.WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return lemmatized_tokens


def preprocess_text(text):
    tokens = tokenize_text(text)
    filtered_tokens = remove_stopwords(tokens)
    lemmatized_tokens = lemmatize_tokens(filtered_tokens)
    return lemmatized_tokens


def main():
    text = 'This is an example sentence.'
    preprocessed_text = preprocess_text(text)
    print(preprocessed_text)


if __name__ == '__main__':
    main()
