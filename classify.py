import os

import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.environ.get('openai_token')


"""
Classifies a given text with into a set of categories
Returns the chosen label

:param str text: The text to be classified
:param dict[str, str] labels: a dict of labels + summaries 
"""


def classify(text: str, labels: dict[str, str]) -> str | None:
    text = text.replace('\n', ' ')
    labels = labels.copy()
    for l in labels:
        labels[l] = labels[l].strip()

    summaries = [s.strip() for s in labels.values()]

    prompt = f"Classify the text into one of the following categories: {', '.join(labels.values())}\n\n" \
        f"Text: \n{text}"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    try:
        # TODO: get rid of the linear search
        cat = response.get('choices')[0].text.strip()
        for k, v in labels.items():
            if cat.find(v) != -1:
                return k
        return None
    except (KeyError, IndexError):
        return None


if __name__ == '__main__':
    # TEST FILES
    labels = {
        'comp1005': 'C',
        'comp1006': 'Assembly',
        'comp1007': 'Digital Logic',
        'comp1001': 'Discrete Maths',
        # 'comp1004': 'Databases',
        # 'comp1043': 'Linear Algebra',
        # 'comp1003': 'Software Engineering',
        # 'comp1009': 'Java and Haskell Programming',
        # 'comp1008': 'Artifitial Intelligence'
    }

    # TODO: Async requests
    for i in range(1, 4):
        with open(f'test_files/{i}.txt') as f:
            print(classify(f.read(), labels))

    text = '''
    '''
