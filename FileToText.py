from PyPDF2 import PdfReader


class FileToText:

    @staticmethod
    def pdf_to_text(path, GET_PAGES=True, pages_to_get=1):
        DEBUG = True
        file_text = ""
        # note: only works with pdfs where text is not an image
        reader = PdfReader(f"{path}")

        # GET_PAGES bool specifies whether to extract text from the whole document
        if GET_PAGES:
            # in a given pdf doc
            number_of_pages = len(reader.pages) 
        else:
            number_of_pages = pages_to_get 

        for page in reader.pages:
            text = page.extract_text().replace("\n", " ")
            file_text += text

        return file_text


# print(FileToText.pdf_to_text("./test.pdf", True))
# print(FileToText.pdf_to_text("./loremipsum.pdf", True))
