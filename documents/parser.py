def parse_pdf(file_path):
    # TODO: Implement PDF parsing logic
    return []


def parse_pptx(file_path):
    # TODO: Implement PPTX parsing logic
    return []


def parse_csv(file_path):
    # TODO: Implement CSV parsing logic
    return []


def parse_docx(file_path):
    # TODO: Implement DOCX parsing logic
    return []


def parse_text(file_path):
    # TODO: Implement text/markdown parsing logic
    return []


def parse_document(file_path):
    if file_path.endswith(".pdf"):
        return parse_pdf(file_path)
    elif file_path.endswith(".pptx"):
        return parse_pptx(file_path)
    elif file_path.endswith(".csv"):
        return parse_csv(file_path)
    elif file_path.endswith(".docx"):
        return parse_docx(file_path)
    elif file_path.endswith(".md") or file_path.endswith(".txt"):
        return parse_text(file_path)
    else:
        return []
