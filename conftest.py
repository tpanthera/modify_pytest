import pytest
from py.xml import html

# Add/modify the HTML-Title

@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('Folder_name', class_='sortable name', col='name'))
    cells.pop()

# Pass values from report to HTML
# Need to improve logic here and also display count of unique test cases with folder name.

@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    folder_name = ''
    for key in report.keywords:
        if key == 'CHATBOT_SERVICES':
            folder_name = 'CHATBOT_SERVICES'
        if key == 'DATABROWSE':
            folder_name = 'DATABROWSE'
        if key == 'MODELZOO_PREBUILT':
            folder_name = 'MODELZOO_PREBUILT'
    cells.insert(1, html.td(folder_name, class_='col-folder_name'))
    cells.pop()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)
