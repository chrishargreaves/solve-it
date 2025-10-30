import sys
from pathlib import Path
# Edit these to customise the content added to the SOLVE-IT knowledge base


# This should add the SOLVE-IT library path if any extension needs to make use of it
solve_it_root = Path(__file__).parent.parent.parent
if str(solve_it_root) not in sys.path:
    sys.path.insert(0, str(solve_it_root))


# Markdown Code 
# -------------

"""Markdown text to be added to the main page"""
def get_markdown_generic():
    return ""

"""Markdown text to be added to the end of each technique"""
def get_markdown_for_technique(t_id):
    return ""

"""Markdown text to be added to the end of each weakness"""
def get_markdown_for_weakness(w_id):
    return ""

"""Markdown text to be added to the end of each mitigation"""
def get_markdown_for_mitigation(m_id):
    return ""


# HTML Code 
# ---------
"""HTML text to be added to the main page"""
def get_html_generic():
    return ""

"""HTML text to be added to the end of each technique"""
def get_html_for_technique(t_id):
    return ""

"""HTML text to be added to the end of each weakness"""
def get_html_for_weakness(w_id):
    return ""

"""HTML text to be added to the end of each mitigation"""
def get_html_for_mitigation(m_id):
    return ""


# Excel Code
# ----------
"""General modifications to be made to the workbook"""
def get_excel_generic(excel_worksheet, start_row):
    return excel_worksheet

"""Modifications to be made to the workbook for each technique"""
def get_excel_for_technique(t_id, excel_worksheet, start_row):

    excel_worksheet.write_string(start_row, 0, f"SOLVE-IT-X content for {t_id}")

    return excel_worksheet

"""Modifications to be made to the workbook for each weakness"""
def get_excel_for_weakness(w_id, excel_worksheet, start_row):
    return excel_worksheet

"""Modifications to be made to the workbook for each mitigation"""
def get_excel_for_mitigation(m_id, excel_worksheet, start_row):
    return excel_worksheet

