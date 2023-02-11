import asyncio
import os

import openai
from aiohttp import ClientSession
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.environ.get('openai_token').rstrip("\n")


class FileClassifier:

    @staticmethod
    async def classify(text: str, labels: dict[str, str]) -> str | None:
        """
        Classifies a given text with into a set of categories
        Returns: the chosen label / None if no label is chosen

        :param str text: The text to be classified
        :param dict[str, str] labels: a dict of labels + summaries 
        """
        # TODO: tweak
        PRE_PROMPT = "Classify the text into one of the following categories:"

        GPT_ARGS = {
            'model': 'text-davinci-003',
            'temperature': 0,
            'max_tokens': 60,
            'top_p': 1.0,
            'frequency_penalty': 0.0,
            'presence_penalty': 0.0
        }

        async with ClientSession() as session:
            openai.aiosession.set(session)
            text = text.replace('\n', ' ')
            labels = labels.copy()
            for l in labels:
                labels[l] = labels[l].strip()

            summaries = [s.strip() for s in labels.values()]

            prompt = f"{PRE_PROMPT} {', '.join(labels.values())}\n\n" \
                f"Text: \n{text}"

            response = openai.Completion.create(
                prompt=prompt,
                **GPT_ARGS,
            )

            try:
                # i hate union types >:(
                cat = response.get('choices')[0].text.strip()
                for k, v in labels.items():
                    if cat.find(v) != -1:
                        return k
                return None
            except (KeyError, IndexError):
                return None

    @staticmethod
    async def summarize(text, max_chars=100, max_words=5):
        """
        Summarizes the text
        Returns: summary

        :param str text: The text to be classified
        :param int max_chars: a dict of labels + summaries 
        """
        # TODO: tweak
        PRE_PROMPT = f"Write a short summary (within {max_chars} characters and {max_words} words) for the following text:"

        GPT_ARGS = {
            'model': 'text-davinci-003',
            'temperature': 0,
            'max_tokens': 60,
            'top_p': 1.0,
            'frequency_penalty': 0.0,
            'presence_penalty': 0.0
        }

        async with ClientSession() as session:
            openai.aiosession.set(session)

            prompt = f"{PRE_PROMPT}\n\n" \
                f"Text: \n{text}"

            response = openai.Completion.create(
                prompt=prompt,
                **GPT_ARGS
            )

            try:
                return response.get('choices')[0].text.strip()
            except (KeyError, IndexError):
                return None