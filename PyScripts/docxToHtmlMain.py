import mammoth

# Input and Output directories
wordDocsFolderPath = 'C:\\Users\\nikhi\\OneDrive - Arsenalia GmbH\\GIT DocxToHtml python\\PyDocxToHtml\\DocxFiles\\Austria_Diesel-based privacy notice-final_DE_Clean.2022.docx'
outputTestResultPath = 'C:\\Users\\nikhi\\OneDrive - Arsenalia GmbH\\GIT DocxToHtml python\\PyDocxToHtml\\TestOutputs\\result.html'
with open(wordDocsFolderPath, "rb") as docx_file:
    result = mammoth.convert_to_html(docx_file)
    text = result.value # The raw text
    with open(outputTestResultPath, 'w', encoding='utf-8') as text_file:
        text_file.write(text)