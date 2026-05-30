from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet

pdf_file = "reports/churn_report.pdf"

doc = SimpleDocTemplate(pdf_file)

styles = getSampleStyleSheet()

elements = []

elements.append(
    Paragraph(
        "Customer Churn Analysis Report",
        styles["Title"]
    )
)

elements.append(Spacer(1, 20))

elements.append(
    Paragraph(
        "This report summarizes customer churn insights and recommendations.",
        styles["BodyText"]
    )
)

elements.append(Spacer(1, 10))

elements.append(
    Paragraph(
        "Key Findings:",
        styles["Heading2"]
    )
)

elements.append(
    Paragraph(
        """
        • Month-to-Month customers have the highest churn rate.<br/>
        • Customers with high monthly charges churn more frequently.<br/>
        • Long-term contracts significantly reduce churn.<br/>
        • Automatic payment methods improve retention.
        """,
        styles["BodyText"]
    )
)

doc.build(elements)

print("PDF report generated successfully!")