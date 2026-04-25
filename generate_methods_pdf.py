from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import Paragraph, Preformatted, SimpleDocTemplate, Spacer


def markdown_to_pdf(md_path: Path, pdf_path: Path) -> None:
    text = md_path.read_text(encoding="utf-8")
    lines = text.splitlines()

    doc = SimpleDocTemplate(
        str(pdf_path),
        pagesize=A4,
        leftMargin=1.7 * cm,
        rightMargin=1.7 * cm,
        topMargin=1.5 * cm,
        bottomMargin=1.5 * cm,
    )

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        "title",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=17,
        leading=21,
        spaceAfter=10,
    )
    h1_style = ParagraphStyle(
        "h1",
        parent=styles["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=13.5,
        leading=17,
        spaceBefore=8,
        spaceAfter=5,
    )
    h2_style = ParagraphStyle(
        "h2",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=11.5,
        leading=15,
        spaceBefore=6,
        spaceAfter=3,
    )
    body_style = ParagraphStyle(
        "body",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=10,
        leading=13.5,
        spaceAfter=3,
    )
    bullet_style = ParagraphStyle(
        "bullet",
        parent=body_style,
        leftIndent=14,
        bulletIndent=6,
        spaceAfter=2,
    )
    code_style = ParagraphStyle(
        "code",
        parent=styles["Code"],
        fontName="Courier",
        fontSize=8.8,
        leading=11.2,
        backColor=colors.whitesmoke,
        borderColor=colors.lightgrey,
        borderWidth=0.4,
        borderPadding=6,
        spaceBefore=3,
        spaceAfter=6,
    )

    story = []
    in_code = False
    code_lines = []

    for raw in lines:
        line = raw.rstrip()

        if line.strip().startswith("```"):
            if not in_code:
                in_code = True
                code_lines = []
            else:
                in_code = False
                code_text = "\n".join(code_lines).replace("\t", "    ")
                if code_text.strip():
                    story.append(Preformatted(code_text, code_style))
                code_lines = []
            continue

        if in_code:
            code_lines.append(line)
            continue

        if not line.strip():
            story.append(Spacer(1, 4))
            continue

        safe = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

        if line.startswith("# "):
            story.append(Paragraph(safe[2:].strip(), title_style))
        elif line.startswith("## "):
            story.append(Paragraph(safe[3:].strip(), h1_style))
        elif line.startswith("### "):
            story.append(Paragraph(safe[4:].strip(), h2_style))
        elif line.startswith("- "):
            story.append(Paragraph(safe[2:].strip(), bullet_style, bulletText="•"))
        else:
            story.append(Paragraph(safe, body_style))

    doc.build(story)


if __name__ == "__main__":
    root = Path(__file__).resolve().parent
    md = root / "TPSM_Methods_Assumptions_Guide.md"
    pdf = root / "TPSM_Methods_Assumptions_Guide.pdf"
    markdown_to_pdf(md, pdf)
    print(f"PDF generated: {pdf}")

