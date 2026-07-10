import csv
import os

from reportlab.platypus import (
    SimpleDocTemplate,
    Table
)

from openpyxl import Workbook



REPORT_FOLDER = "reports"


if not os.path.exists(REPORT_FOLDER):

    os.makedirs(REPORT_FOLDER)



# ==========================
# CSV EXPORT
# ==========================

def export_csv(
    report_id,
    data
):

    file_path = (
        f"{REPORT_FOLDER}/report_{report_id}.csv"
    )


    with open(
        file_path,
        "w",
        newline=""
    ) as file:


        writer = csv.writer(file)


        writer.writerow(
            ["Report ID", "Value"]
        )


        for item in data:

            writer.writerow(
                [
                    report_id,
                    str(item)
                ]
            )


    return file_path



# ==========================
# EXCEL EXPORT
# ==========================

def export_excel(
    report_id,
    data
):

    file_path = (
        f"{REPORT_FOLDER}/report_{report_id}.xlsx"
    )


    workbook = Workbook()


    sheet = workbook.active


    sheet.append(
        [
            "Report ID",
            "Value"
        ]
    )


    for item in data:

        sheet.append(
            [
                report_id,
                str(item)
            ]
        )


    workbook.save(
        file_path
    )


    return file_path



# ==========================
# PDF EXPORT
# ==========================

def export_pdf(
    report_id,
    data
):

    file_path = (
        f"{REPORT_FOLDER}/report_{report_id}.pdf"
    )


    document = SimpleDocTemplate(
        file_path
    )


    table_data = [

        [
            "Report ID",
            "Value"
        ]

    ]


    for item in data:

        table_data.append(

            [
                report_id,
                str(item)
            ]

        )


    table = Table(
        table_data
    )


    document.build(
        [
            table
        ]
    )


    return file_path