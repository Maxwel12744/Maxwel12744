"""Builds terminal.svg: an animated terminal card for a GitHub profile README.
Edit the text in the CONTENT section, run `python make_terminal.py`, and upload the new terminal.svg."""
from xml.sax.saxutils import escape

# ------------------------------- CONTENT: edit this part -------------------------------
NAME = "MAXWEL"
TAGLINE = "✦ [Full-Stack Developer · BSc CS · Multimedia University of Kenya]"
WINDOW_TITLE = "maxwel@dashboard-core: ~/portfolio (main) ⚡"
CMD = "maxwel"
ROLE_COMMENT = "# specialization & disciplines"
ROLE = '"Full-Stack Web Developer · Django & MySQL"'
STACK = ["Python", "Django", "MySQL", "JavaScript", "HTML", "CSS", "Git"]
LEARNING = ["Machine Learning", "Artificial Intelligence", "Learning by Building"]
STATUS = '"Building full-stack apps · open to internships"'
# ---------------------------------------------------------------------------------------

W, H = 900, 372
CW = 9            # width of one character at font-size 15
FS = 15
RED, CYAN, GREEN, GREY, WHITE, LAV = "#ff4d6d", "#22d3ee", "#4ade80", "#6b7a99", "#e2e8f0", "#a78bfa"
FONT = "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, 'Liberation Mono', 'DejaVu Sans Mono', monospace"

def prompt(flag, tail=None):
    segs = [("➜", RED, True), (" ", None, False), ("~", CYAN, False), (" ", None, False),
            (CMD, CYAN, True), (" ", None, False), (flag, CYAN, True)]
    if tail:
        segs += [(" ", None, False), tail]
    return segs

def stack_segments():
    segs = [("[ ", WHITE, False)]
    for i, s in enumerate(STACK):
        segs.append((f'"{s}"', GREEN, False))
        segs.append((", " if i < len(STACK) - 1 else " ]", WHITE, False))
    return segs

def learning_segments():
    segs = []
    for i, s in enumerate(LEARNING):
        segs.append((s, LAV, False))
        if i < len(LEARNING) - 1:
            segs.append((" | ", GREY, False))
    return segs

# (y, indent_chars, segments)
LINES = [
    (148, 0, prompt("--role", ("  " + ROLE_COMMENT, GREY, False))),
    (172, 2, [(ROLE, GREEN, False)]),
    (210, 0, prompt("--stack")),
    (234, 2, stack_segments()),
    (272, 0, prompt("--learning")),
    (296, 2, learning_segments()),
    (334, 0, prompt("--status", (STATUS, WHITE, False))),
]
X0 = 32

def nchars(segs):
    return sum(len(t) for t, _, _ in segs)

# ---- timeline -------------------------------------------------------------------------
timeline, t = [], 0.5
title_n = len(NAME)
timeline.append(("title", t, 0.12 * title_n)); t += 0.12 * title_n + 0.15
timeline.append(("tag", t - 0.5, 0.025 * len(TAGLINE)))
for i, (_, _, segs) in enumerate(LINES):
    n = nchars(segs)
    d = max(0.5, 0.032 * n)
    timeline.append((f"l{i}", t, d)); t += d + 0.25
END = t
T = round(END + 5.5, 2)  # hold time with the blinking cursor, then the animation restarts

def keyed(start, dur, n, widths):
    """discrete keyframes: char k appears at start + (k-1)*dt"""
    dt = dur / n
    kt = [0.0] + [(start + k * dt) / T for k in range(n)]
    vals = [0] + widths
    return kt, vals

def anim_width(start, dur, n, cw, extra=40):
    widths = [(k + 1) * cw for k in range(n)]
    widths[-1] += extra
    kt, vals = keyed(start, dur, n, widths)
    return (f'<animate attributeName="width" dur="{T}s" repeatCount="indefinite" calcMode="discrete" '
            f'keyTimes="{";".join(f"{k:.4f}" for k in kt)}" values="{";".join(str(v) for v in vals)}"/>')

out = []
a = out.append
a(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Terminal card introducing Maxwel">')
a('<defs>')
a('<linearGradient id="border" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#12d7ff"/><stop offset="0.55" stop-color="#6b4eff"/><stop offset="1" stop-color="#f5a623"/></linearGradient>')
a('<linearGradient id="body" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0c1631"/><stop offset="1" stop-color="#091024"/></linearGradient>')
a('<linearGradient id="name" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#22e5ff"/><stop offset="1" stop-color="#ffd27a"/></linearGradient>')
a('<filter id="glow" x="-20%" y="-40%" width="140%" height="180%"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>')
# clip paths (typing effect)
tl = {k: (s, d) for k, s, d in timeline}
s, d = tl["title"]
a(f'<clipPath id="ct"><rect x="{X0}" y="62" height="52" width="0">{anim_width(s, d, title_n, 24)}</rect></clipPath>')
tag_n = len(TAGLINE); s, d = tl["tag"]
tag_x = W - 32 - tag_n * 7.2
a(f'<clipPath id="cg"><rect x="{tag_x:.1f}" y="74" height="28" width="0">{anim_width(s, d, tag_n, 7.2)}</rect></clipPath>')
for i, (y, ind, segs) in enumerate(LINES):
    s, d = tl[f"l{i}"]; n = nchars(segs)
    a(f'<clipPath id="c{i}"><rect x="{X0 + ind * CW}" y="{y - 18}" height="26" width="0">{anim_width(s, d, n, CW)}</rect></clipPath>')
a('</defs>')

# card
a(f'<rect x="2" y="2" width="{W - 4}" height="{H - 4}" rx="20" fill="url(#body)" stroke="url(#border)" stroke-width="2.5"/>')
# window bar
for cx, col in ((30, "#ff5f56"), (52, "#ffbd2e"), (74, "#27c93f")):
    a(f'<circle cx="{cx}" cy="28" r="6.5" fill="{col}"/>')
a(f'<text x="{W / 2}" y="33" text-anchor="middle" font-family="{FONT}" font-size="12.5" fill="#9fb0c8">{escape(WINDOW_TITLE)}</text>')
a(f'<rect x="{W - 138}" y="14" width="112" height="27" rx="13.5" fill="#0d2a33" stroke="#1fb5a8" stroke-width="1.2"/>')
a(f'<circle cx="{W - 118}" cy="27.5" r="4" fill="#2de2d0"><animate attributeName="opacity" values="1;0.3;1" dur="1.8s" repeatCount="indefinite"/></circle>')
a(f'<text x="{W - 106}" y="32" font-family="{FONT}" font-size="11" font-weight="bold" letter-spacing="1" fill="#5eead4">ONLINE</text>')
a(f'<line x1="2" y1="54" x2="{W - 2}" y2="54" stroke="#1b2a47" stroke-width="1"/>')

# title + tagline
a(f'<g clip-path="url(#ct)"><text x="{X0}" y="104" font-family="{FONT}" font-size="38" font-weight="bold" fill="url(#name)" filter="url(#glow)" textLength="{title_n * 24}" lengthAdjust="spacing" xml:space="preserve">{escape(NAME)}</text></g>')
a(f'<g clip-path="url(#cg)"><text x="{tag_x:.1f}" y="94" font-family="{FONT}" font-size="12" fill="#f4c46a" textLength="{tag_n * 7.2:.1f}" lengthAdjust="spacing" xml:space="preserve">{escape(TAGLINE)}</text></g>')

# command lines
for i, (y, ind, segs) in enumerate(LINES):
    a(f'<g clip-path="url(#c{i})" font-family="{FONT}" font-size="{FS}">')
    x = X0 + ind * CW
    for text, color, bold in segs:
        if color is not None and text.strip():
            lead = len(text) - len(text.lstrip())
            body = text.strip()
            tx = x + lead * CW
            wgt = ' font-weight="bold"' if bold else ""
            tlen = f' textLength="{len(body) * CW}" lengthAdjust="spacing"' if len(body) > 1 else ""
            a(f'<text x="{tx}" y="{y}" fill="{color}"{wgt}{tlen} xml:space="preserve">{escape(body)}</text>')
        x += len(text) * CW
    a('</g>')

# blinking cursor after the last line
y_last, ind_last, segs_last = LINES[-1]
cur_x = X0 + (ind_last + nchars(segs_last)) * CW + 6
last_end = tl[f"l{len(LINES) - 1}"][0] + tl[f"l{len(LINES) - 1}"][1]
m = int((T - last_end) / 0.5)
kt = [0.0] + [(last_end + j * 0.5) / T for j in range(m)]
vals = [0] + [1 if j % 2 == 0 else 0 for j in range(m)]
a(f'<rect x="{cur_x}" y="{y_last - 15}" width="10" height="19" fill="#22d3ee" opacity="0"><animate attributeName="opacity" dur="{T}s" repeatCount="indefinite" calcMode="discrete" keyTimes="{";".join(f"{k:.4f}" for k in kt)}" values="{";".join(str(v) for v in vals)}"/></rect>')
a('</svg>')
svg = "\n".join(out)
open("terminal.svg", "w", encoding="utf-8").write(svg)

# static preview (final frame) so the design can be checked without animation
import re
prev = re.sub(r'<animate [^>]*/>', '', svg)
prev = re.sub(r'(<clipPath id="[^"]+"><rect [^>]*?)width="0"', r'\1width="900"', prev)
prev = prev.replace('opacity="0"', 'opacity="1"')
open("preview.svg", "w", encoding="utf-8").write(prev)
print(f"terminal.svg written: {len(svg)/1024:.1f} KB, cycle {T}s")
