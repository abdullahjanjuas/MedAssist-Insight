from PDF_Processing.pdf_utils import (
    extract_text_from_pdf,
    extract_tables_from_pdf,
    extract_text_with_ocr
)
from LLM_Structuring_and_Flagging.llm_structuring_and_flag import (
    run_llm,
    parse_llm_output,
    flag_tests
)
from Rag.insight_generator import generate_insights


def run_full_pipeline(pdf_path: str, pdf_type: str):
    """
    pdf_type: 'text' | 'table' | 'image'
    """

    # 1. Ingestion
    if pdf_type == "text":
        raw_text = extract_text_from_pdf(pdf_path)

    elif pdf_type == "table":
        raw_text = extract_tables_from_pdf(pdf_path)

    elif pdf_type == "image":
        raw_text = extract_text_with_ocr(pdf_path)

    else:
        raise ValueError("Invalid PDF type selected.\nPlease try selecting Text if tabular fails and Image for images converted to pdf format")

    # 2. LLM structuring
    raw_llm_response = run_llm(raw_text)
    parsed_data = parse_llm_output(raw_llm_response)

    # 3. Rule-based flagging
    flagged_tests = flag_tests(parsed_data["tests"])
    abnormal_tests = [t for t in flagged_tests if t["status"] in ("high", "low")]

    # 4. RAG insight generation
    insights = generate_insights(abnormal_tests)

    return {
        "all_tests": flagged_tests,
        "abnormal_tests": abnormal_tests,
        "insights": insights
    }
