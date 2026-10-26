"""make_workbook.py - build templates/standard-data-workbook.xlsx (Excel version of the course model).

    python tools/make_workbook.py

The workbook uses only built-in worksheet functions (LINEST, INDEX, IF), so it recalculates in
Excel or LibreOffice without the Data Analysis ToolPak. Sheet "ToolPak steps" explains how to
get the same results with the ToolPak's Regression tool.

License: MIT
"""
import os
import sys

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.worksheet.formula import ArrayFormula

sys.path.insert(0, os.path.dirname(__file__))
import sdskit as sk  # noqa: E402

OUT = os.path.join(os.path.dirname(__file__), "..", "templates", "standard-data-workbook.xlsx")
B = Font(bold=True)
IN = PatternFill("solid", fgColor="FFF2CC")
HEAD = PatternFill("solid", fgColor="DDEBF7")


def header(ws, cols, row=1):
    for j, c in enumerate(cols, 1):
        cell = ws.cell(row=row, column=j, value=c)
        cell.font, cell.fill = B, HEAD


def main():
    wb = Workbook()

    # ---- Studies (corrected)
    ws = wb.active
    ws.title = "RunStudies"
    b = sk.brake(corrected=True)
    cols = ["study", "bends", "flips", "weight_kg", "length_mm", "thickness_mm", "normal_min", "note"]
    header(ws, cols)
    for i, r in enumerate(b.itertuples(), 2):
        ws.cell(row=i, column=1, value=r.study)
        ws.cell(row=i, column=2, value=int(r.bends))
        ws.cell(row=i, column=3, value=int(r.flips))
        ws.cell(row=i, column=4, value=float(r.weight_kg))
        ws.cell(row=i, column=5, value=float(r.length_mm))
        ws.cell(row=i, column=6, value=float(r.thickness_mm))
        ws.cell(row=i, column=7, value=float(r.normal_min))
        if r.study in sk.CORRECTIONS:
            ws.cell(row=i, column=8, value="bends corrected 3 -> 8 from study file (Module 08)")
    n = len(b) + 1                       # last data row
    ws.column_dimensions["H"].width = 48

    # ---- Run model: LINEST(y, X) with X = bends..length (columns B:E)
    m = wb.create_sheet("RunModel")
    m["A1"], m["A1"].font = "Run model: normal min/piece = b0 + b1*bends + b2*flips + b3*weight_kg + b4*length_mm", B
    m["A3"] = "LINEST output (rows: coefficients, std errors, R2 & SE, F & df, SS reg & SS resid). Columns run in REVERSE order of X."
    for j, lab in enumerate(["length_mm", "weight_kg", "flips", "bends", "Intercept"], 2):
        cell = m.cell(row=4, column=j, value=lab)
        cell.font, cell.fill = B, HEAD
    rng_y, rng_x = f"RunStudies!G2:G{n}", f"RunStudies!B2:E{n}"
    m["B5"] = ArrayFormula("B5:F9", f"=LINEST({rng_y},{rng_x},TRUE,TRUE)")
    for i, lab in enumerate(["coefficient", "std error", "R2 | SE", "F | df", "SS reg | SS resid"], 5):
        m.cell(row=i, column=1, value=lab)
    header(m, ["Term", "Coefficient", "Std error", "t"], row=12)
    terms = [("Intercept", "F"), ("bends", "E"), ("flips", "D"), ("weight_kg", "C"), ("length_mm", "B")]
    for i, (t, c) in enumerate(terms, 13):
        m.cell(row=i, column=1, value=t)
        m.cell(row=i, column=2, value=f"={c}5")
        m.cell(row=i, column=3, value=f"={c}6")
        m.cell(row=i, column=4, value=f"=B{i}/C{i}")
    m["A19"], m["B19"] = "R2", "=B7"
    m["A20"], m["B20"] = "Std error of estimate (min)", "=C7"
    m["A21"], m["B21"] = "Observations", f"=COUNT({rng_y})"
    m["A22"], m["B22"] = "Residual df", "=C8"
    for col in "ABCDEF":
        m.column_dimensions[col].width = 18
    m.column_dimensions["A"].width = 30

    # ---- Setup studies + model
    s = wb.create_sheet("SetupStudies")
    su = sk.load("brake_setup_studies")
    header(s, ["study", "tool_segments", "new_program", "normal_min"])
    for i, r in enumerate(su.itertuples(), 2):
        s.cell(row=i, column=1, value=r.study)
        s.cell(row=i, column=2, value=int(r.tool_segments))
        s.cell(row=i, column=3, value=int(r.new_program))
        s.cell(row=i, column=4, value=float(r.normal_min))
    ns = len(su) + 1
    s["F1"], s["F1"].font = "Setup model LINEST (reverse order: new_program, tool_segments, Intercept)", B
    for j, lab in zip((7, 8, 9), ["new_program", "tool_segments", "Intercept"]):
        cell = s.cell(row=2, column=j, value=lab)
        cell.font, cell.fill = B, HEAD
    s["G3"] = ArrayFormula("G3:I7", f"=LINEST(D2:D{ns},B2:C{ns},TRUE,TRUE)")
    for i, lab in enumerate(["coefficient", "std error", "R2 | SE", "F | df", "SS reg | SS resid"], 3):
        s.cell(row=i, column=6, value=lab)
    s.column_dimensions["F"].width = 18

    # ---- Job calculator
    c = wb.create_sheet("JobStandard")
    c["A1"], c["A1"].font = "Press-brake job standard (yellow cells are inputs)", B
    inputs = [("Bends", 5), ("Flips", 1), ("Weight (kg)", 3.85), ("Length (mm)", 2230), ("Tool segments changed", 7),
              ("New backgauge program? (1 = yes)", 0), ("Lot quantity", 25), ("PF&D allowance", sk.PFD),
              ("Rate ($/standard hour)", sk.RATE)]
    for i, (lab, v) in enumerate(inputs, 3):
        c.cell(row=i, column=1, value=lab)
        cell = c.cell(row=i, column=2, value=v)
        cell.fill = IN
    c["A13"], c["A13"].font = "Results", B
    c["A14"], c["B14"] = "Run, normal min/piece", ("=RunModel!B13+RunModel!B14*B3+RunModel!B15*B4"
                                                   "+RunModel!B16*B5+RunModel!B17*B6")
    c["A15"], c["B15"] = "Setup, normal min/lot", "=SetupStudies!I3+SetupStudies!H3*B7+SetupStudies!G3*B8"
    c["A16"], c["B16"] = "Standard hours for the lot", "=(B15+B9*B14)*(1+B10)/60"
    c["A17"], c["B17"] = "Standard min/piece (incl. setup share)", "=B16*60/B9"
    c["A18"], c["B18"] = "Labor + machine cost for the lot ($)", "=B16*B11"
    c["A19"], c["B19"] = "Range check", (
        f'=IF(OR(B3<MIN(RunStudies!B2:B{n}),B3>MAX(RunStudies!B2:B{n}),B4>MAX(RunStudies!C2:C{n}),'
        f'B5<MIN(RunStudies!D2:D{n}),B5>MAX(RunStudies!D2:D{n}),B6<MIN(RunStudies!E2:E{n}),B6>MAX(RunStudies!E2:E{n}),'
        f'B7>MAX(SetupStudies!B2:B{ns})),"OUTSIDE study range - spot-check with a time study","inside study range")')
    c.column_dimensions["A"].width = 40
    c.column_dimensions["B"].width = 52

    # ---- ToolPak steps
    t = wb.create_sheet("ToolPak steps")
    steps = [
        "Same model with the Analysis ToolPak (Excel for Windows or Mac):",
        "1. Enable it once: File > Options > Add-ins > Manage Excel Add-ins > Go > tick Analysis ToolPak.",
        "   (Mac: Tools > Excel Add-ins.) Menu names can differ between Excel versions.",
        "2. Data > Data Analysis > Regression.",
        "3. Input Y Range: RunStudies!G1:G41. Input X Range: RunStudies!B1:E41 (X columns must be adjacent).",
        "4. Tick Labels, Residuals, Standardized Residuals, Residual Plots, Line Fit Plots. Output to a new sheet.",
        "5. Compare: coefficients should match RunModel!B13:B17; R Square should match RunModel!B19.",
        "6. Read: Significance F (whole model), P-value per coefficient, Standard Error (= SE of estimate).",
        "7. Scan Standardized Residuals: |value| > 3 means check that study (Module 08).",
        "To test the uncorrected data, change RunStudies!B28 (S27) back to 3 and watch R2 and SE change.",
        "The ToolPak output is static: re-run it after any data change. LINEST updates live.",
    ]
    for i, line in enumerate(steps, 1):
        t.cell(row=i, column=1, value=line).alignment = Alignment(wrap_text=False)
    t.column_dimensions["A"].width = 110

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    wb.save(OUT)
    print("wrote", os.path.normpath(OUT))


if __name__ == "__main__":
    main()
