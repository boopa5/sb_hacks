from pdf2image import convert_from_path

def convert_pdf_to_jpeg(pdf_path, output_folder):
    pages = convert_from_path(pdf_path, output_folder=output_folder, fmt='jpeg')

    # The 'pages' variable now contains a list of PIL Image objects
    # Save each page as a separate JPEG file
    for i, page in enumerate(pages):
        page.save(f"{output_folder}/page_{i + 1}.jpg", 'JPEG')


pdf_file_path = "./static/uploads/a.pdf"
output_folder_path = "./static/images"

convert_pdf_to_jpeg(pdf_file_path, output_folder_path)