from pypdf import PdfReader

def extract_text(pdf_doc): # to extract the raw text from the input pdf
    try:
        
        pdf=PdfReader(pdf_doc)
        
        raw_text =''
        for index,page in enumerate(pdf.pages):
            
            text=page.extract_text()
            if text:
                
                raw_text += text
                
                
        return raw_text
    except Exception as e:
        return f'Error in extracting text'