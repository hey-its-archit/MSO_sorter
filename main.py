from PyPDF2 import PdfFileReader, PdfFileWriter

file_name = 'Lect 18'


def script():
    input_file = PdfFileReader(open(file_name + '.pdf', "rb"))
    output = PdfFileWriter()
    number_of_pages = input_file.getNumPages()
    # print(input_file.getNumPages())
    output.addPage(input_file.getPage(0))
    prv_page_no = 1
    for i in range(0, number_of_pages):
        page = input_file.getPage(i)
        text = page.extractText()
        page_no = text.rsplit('2019', 1)[1]
        page_no = page_no.rsplit('/', 1)[0]
        if int(page_no) == int(prv_page_no) + 1:
            print(page_no)
            output.addPage(input_file.getPage(i - 1))
            prv_page_no = page_no
    output.addPage(input_file.getPage(number_of_pages - 1))

    outputStream = open(file_name + '_fixed.pdf', "wb")
    output.write(outputStream)

    # page = input_file.getPage(1);
    # text = page.extractText()
    # page_no = text.rsplit('2019', 1)[1]
    # page_no = page_no.rsplit('/', 1)[0]
    # print(page_no)


if __name__ == "__main__":
    script()
