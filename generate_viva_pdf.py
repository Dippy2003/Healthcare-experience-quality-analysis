from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import Paragraph, Preformatted, SimpleDocTemplate, Spacer


def build_pdf_from_markdown(md_path: Path, pdf_path: Path) -> None:
    text = md_path.read_text(encoding="utf-8")
    lines = text.splitlines()

    doc = SimpleDocTemplate(
        str(pdf_path),
        pagesize=A4,
        leftMargin=1.7 * cm,
        rightMargin=1.7 * cm,
        topMargin=1.5 * cm,
        bottomMargin=1.5 * cm,
        title="TPSM Viva Guide with Code",
        author="Cursor Assistant",
    )

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        "TitleStyle",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=18,
        leading=22,
        spaceAfter=12,
    )
    h1_style = ParagraphStyle(
        "H1Style",
        parent=styles["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=14,
        leading=18,
        spaceBefore=10,
        spaceAfter=6,
    )
    h2_style = ParagraphStyle(
        "H2Style",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=12,
        leading=16,
        spaceBefore=8,
        spaceAfter=4,
    )
    body_style = ParagraphStyle(
        "BodyStyle",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=10,
        leading=14,
        spaceAfter=4,
    )
    bullet_style = ParagraphStyle(
        "BulletStyle",
        parent=body_style,
        leftIndent=14,
        bulletIndent=6,
        spaceAfter=2,
    )
    code_style = ParagraphStyle(
        "CodeStyle",
        parent=styles["Code"],
        fontName="Courier",
        fontSize=8.8,
        leading=11.2,
        backColor=colors.whitesmoke,
        borderColor=colors.lightgrey,
        borderWidth=0.5,
        borderPadding=6,
        borderRadius=2,
        spaceBefore=3,
        spaceAfter=6,
    )

    story = []
    in_code = False
    code_lines = []

    for raw_line in lines:
        line = raw_line.rstrip()

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

        safe_line = (
            line.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
        )

        if line.startswith("# "):
            story.append(Paragraph(safe_line[2:].strip(), title_style))
            continue
        if line.startswith("## "):
            story.append(Paragraph(safe_line[3:].strip(), h1_style))
            continue
        if line.startswith("### "):
            story.append(Paragraph(safe_line[4:].strip(), h2_style))
            continue
        if line.startswith("- "):
            story.append(Paragraph(safe_line[2:].strip(), bullet_style, bulletText="•"))
            continue

        story.append(Paragraph(safe_line, body_style))

    doc.build(story)


if __name__ == "__main__":
    root = Path(__file__).resolve().parent
    md_file = root / "TPSM_Viva_Guide_With_Code.md"
    pdf_file = root / "TPSM_Viva_Guide_With_Code.pdf"
    build_pdf_from_markdown(md_file, pdf_file)
    print(f"PDF generated: {pdf_file}")

