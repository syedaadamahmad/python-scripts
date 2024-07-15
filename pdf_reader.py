import PyPDF2

# Path to the uploaded PDF file
pdf_path = "/mnt/data/IB_19_6_KichlooETAL_JandK_Checklist.pdf"

# Extracting text from the PDF
def extract_text_from_pdf(pdf_path):
    pdf_text = ""
    with open(pdf_path, "rb") as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            pdf_text += page.extract_text()
    return pdf_text

pdf_text = extract_text_from_pdf(pdf_path)
pdf_text[:2000]  # Displaying the first 2000 characters for context
