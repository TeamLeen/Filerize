import os

import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.environ.get('openai_token')

categories = [
    'C Programming',
    'Assembly',
    'Digital Logic',
    'Discrete Maths'
]

text = '''
Task 4 - Write some code
In the terminal window, enter the following commands:

$ cd comp1005_2022_activity_01
$ gedit task1.c &
The first command changes directory to the project directory which was created when you cloned the project in the previous task. The second command creates and opens a file named task1.c in the gedit graphical text editor.
Your first program is very simple: print the string "hello, world!" to the screen. Here is the code for this program, type it in to gedit and press CTRL-s to save the file.

#include <stdio.h>

int main(int argc, char **argv)
{
	printf("hello, world.\n");

	return 0;
}
Now you have some code in a file, the next step is to add it to your project.

Task 5 - Add the file to the project
In your terminal, type:

$ git add task1.c
This will add the task1.c file to your local copy of your project.
Now we better check your code compiles and runs correctly.

Task 6 - Compile the code
Type the following to compile your code using the gcc compiler:

$ gcc -Wall -ansi -pedantic-errors -o task1 task1.c
Hopefully, it will compile without warnings or errors. If compilation fails, check  you have typed the code in Task 4 correctly (or cut and paste the code if you are totally stuck!).
Now, time to run your compiled code.

Task 7 - Run the code
On the command line, type:

$ ./task1
This command runs your compiled program. Hopefully you will see the string "hello, world." printed out. If not, go back and check you have typed in the code in Task 4 correctly.
Next, we create a snapshot of the task1.c file in your local repository.
'''


"""
Classifies a given text with into a set of categories
:param str text: The text to be classified
:param str categories: a list of summaries 
"""


def classify(text: str, categories: list[str]):
    prompt = f"Classify the text into the following categories: {', '.join(categories)}\n\n" \
        f"Text: {text}"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0
    )

    return response.get('choices')[0].text


print(classify(text, categories))
