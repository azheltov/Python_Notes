import PyPDF2

import re

def search_pdf(file_path, keywords):
    matches = []
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page_num, page in enumerate(reader.pages):
            text = page.extract_text()
            for keyword in keywords:
                for match in re.finditer(rf'\b{re.escape(keyword)}\b', text, re.IGNORECASE):
                    start = max(match.start() - 30, 0)
                    end = match.end() + 30
                    snippet = text[start:end].replace('\n', ' ')
                    matches.append({
                        'page': page_num + 1,
                        'keyword': keyword,
                        'context': snippet
                    })
    return matches





# Example usage:
if __name__ == "__main__":
    file = 'sample.pdf'  # replace with your PDF file path
    terms = ['machine learning', 'data', 'Python']
    results = search_pdf(file, terms)
    for r in results:
        print(f"[Page {r['page']}] {r['keyword']} → ...{r['context']}...")
