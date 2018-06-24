def remove_stopwords(tokens):
    from pythainlp.corpus import stopwords

    # Get the stopwords for the specified language
    stop_words = stopwords.words('thai')

    # Remove the stop words from the set of word tokens
    tokens = set(tokens) - set(stop_words)

    return tokens


class SynsetDistanceThai:
    """
    Calculate the similarity of two statements.
    This is based on the total maximum synset similarity between each word in each sentence.

    This algorithm uses the `wordnet`_ functionality of `NLTK`_ to determine the similarity
    of two statements based on the path similarity between each token of each statement.
    This is essentially an evaluation of the closeness of synonyms.
    """

    def __init__(self):
        pass

    def __call__(self, statement_a, statement_b):
        return self.compare(statement_a, statement_b)

    def get_initialization_functions(self):
        """
        Return all initialization methods for the comparison algorithm.
        Initialization methods must start with 'initialize_' and
        take no parameters.
        """
        initialization_methods = [
            (
                method,
                getattr(self, method),
            ) for method in dir(self) if method.startswith('initialize_')
        ]

        return {
            key: value for (key, value) in initialization_methods
        }

    def compare(self, statement, other_statement):
        """
        Compare the two input statements.

        :return: The percent of similarity between the closest synset distance.
        :rtype: float

        .. _wordnet: http://www.nltk.org/howto/wordnet.html
        .. _NLTK: http://www.nltk.org/
        """
        # from nltk.corpus import wordnet
        # from nltk import word_tokenize
        # from chatterbot import utils
        import itertools

        from pythainlp.tokenize import word_tokenize
        from pythainlp.corpus import wordnet

        tokens1 = word_tokenize(statement.text.lower(), engine='newmm')
        tokens2 = word_tokenize(other_statement.text.lower(), engine='newmm')

        # Remove all stop words from the list of word tokens
        tokens1 = remove_stopwords(tokens1)
        tokens2 = remove_stopwords(tokens2)

        # The maximum possible similarity is an exact match
        # Because path_similarity returns a value between 0 and 1,
        # max_possible_similarity is the number of words in the longer
        # of the two input statements.
        max_possible_similarity = max(
            len(statement.text.split()),
            len(other_statement.text.split())
        )

        max_similarity = 0.0

        # Get the highest matching value for each possible combination of words
        for combination in itertools.product(*[tokens1, tokens2]):

            synset1 = wordnet.synsets(combination[0])
            synset2 = wordnet.synsets(combination[1])

            if synset1 and synset2:

                # Get the highest similarity for each combination of synsets
                for synset in itertools.product(*[synset1, synset2]):
                    similarity = synset[0].path_similarity(synset[1])

                    if similarity and (similarity > max_similarity):
                        max_similarity = similarity

        if max_possible_similarity == 0:
            return 0

        return max_similarity / max_possible_similarity


synset_distance_thai = SynsetDistanceThai()
