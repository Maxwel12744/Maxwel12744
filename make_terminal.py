"""Builds terminal.svg matching the dark cyan/neon theme card."""
from xml.sax.saxutils import escape

# --- CONTENT: edit this part ---
NAME = "MAXWEL"
TAGLINE = "✦ [Full-Stack Developer · BSc CS · Multimedia University of Kenya]"
WINDOW_TITLE = "maxwel@dashboard-core: ~/portfolio (main) ⚡"
CMD = "maxwel"
ROLE_COMMENT = "# specialization & disciplines"
ROLE = '"Full-Stack Web Developer · Django & MySQL"'
STACK = ["Python", "Django", "MySQL", "JavaScript", "HTML", "CSS", "Git"]
LEARNING = ["Machine Learning", "Artificial Intelligence", "Learning by Building"]
STATUS = '"Building full-stack apps · open to internships"'

# --- COLOR PALETTE MATCHING THE REFERENCE ---
BG_COLOR = "#0b0f19"         # Dark navy background
BORDER_COLOR = "#ffa726"     # Subtle gold/orange bottom outline
TEXT_CYAN = "#00e5ff"        # Bright cyan name & prompt text
TEXT_ORANGE = "#ffb74d"      # Warm orange taglines & command flags
TEXT_GREEN = "#00e676"       # Neon green quotes & strings
TEXT_PURPLE = "#b388ff"      # Soft lavender array text
TEXT_MUTED = "#546e7a"       # Muted gray comments & brackets
WHITE = "#ffffff"

svg_content = f"""<svg fill="none" viewBox="0 0 900 372" width="900" height="372" xmlns="http://www.w3.org/2000/svg">
  <foreignObject width="100%" height="100%">
    <div xmlns="http://www.w3.org/1999/xhtml">
      <style>
        .container {{
          font-family: "Courier New", Consolas, monospace;
          background-color: {BG_COLOR};
          color: {WHITE};
          padding: 20px;
          border-radius: 16px;
          height: 372px;
          box-sizing: border-box;
          border: 1px solid rgba(255, 255, 255, 0.1);
          box-shadow: 0 0 20px rgba(0, 0, 0, 0.8), inset 0 -3px 0 {BORDER_COLOR};
        }}
        .header {{
          display: flex;
          align-items: center;
          justify-content: space-between;
          margin-bottom: 20px;
          padding-bottom: 10px;
          border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        }}
        .dots {{
          display: flex;
          gap: 8px;
        }}
        .dot {{
          height: 12px;
          width: 12px;
          border-radius: 50%;
        }}
        .dot-red {{ background-color: #ff5252; }}
        .dot-yellow {{ background-color: #ffb74d; }}
        .dot-green {{ background-color: #69f0ae; }}
        .title {{
          color: {TEXT_MUTED};
          font-size: 13px;
        }}
        .status-badge {{
          border: 1px solid {TEXT_CYAN};
          color: {TEXT_CYAN};
          padding: 2px 10px;
          border-radius: 12px;
          font-size: 11px;
          font-weight: bold;
        }}
        .body {{
          font-size: 14px;
          line-height: 1.8;
        }}
        .hero-name {{
          color: {TEXT_CYAN};
          font-size: 26px;
          font-weight: 900;
          letter-spacing: 2px;
          text-shadow: 0 0 10px rgba(0, 229, 255, 0.5);
          margin-right: 15px;
        }}
        .tagline {{ color: {TEXT_ORANGE}; font-size: 13px; }}
        .prompt-arrow {{ color: #ff5252; margin-right: 6px; }}
        .prompt-tilde {{ color: {TEXT_CYAN}; margin-right: 6px; }}
        .cmd {{ color: {TEXT_CYAN}; font-weight: bold; }}
        .flag {{ color: {TEXT_ORANGE}; }}
        .comment {{ color: {TEXT_MUTED}; }}
        .string {{ color: {TEXT_GREEN}; }}
        .array {{ color: {TEXT_PURPLE}; }}
      </style>
      <div class="container">
        <div class="header">
          <div class="dots">
            <span class="dot dot-red"></span>
            <span class="dot dot-yellow"></span>
            <span class="dot dot-green"></span>
          </div>
          <span class="title">{escape(WINDOW_TITLE)}</span>
          <span class="status-badge">● ONLINE</span>
        </div>
        <div class="body">
          <div style="margin-bottom: 15px;">
            <span class="hero-name">{escape(NAME)}</span>
            <span class="tagline">{escape(TAGLINE)}</span>
          </div>

          <p>
            <span class="prompt-arrow">➔</span><span class="prompt-tilde">~</span>
            <span class="cmd">{escape(CMD)}</span> <span class="flag">--role</span>
            <span class="comment">{escape(ROLE_COMMENT)}</span><br/>
            <span class="string">&nbsp;&nbsp;{escape(ROLE)}</span>
          </p>

          <p>
            <span class="prompt-arrow">➔</span><span class="prompt-tilde">~</span>
            <span class="cmd">{escape(CMD)}</span> <span class="flag">--stack</span><br/>
            <span class="array">&nbsp;&nbsp;[ {", ".join([f'"{s}"' for s in STACK])} ]</span>
          </p>

          <p>
            <span class="prompt-arrow">➔</span><span class="prompt-tilde">~</span>
            <span class="cmd">{escape(CMD)}</span> <span class="flag">--learning</span><br/>
            <span class="string">&nbsp;&nbsp;{" | ".join(LEARNING)}</span>
          </p>

          <p>
            <span class="prompt-arrow">➔</span><span class="prompt-tilde">~</span>
            <span class="cmd">{escape(CMD)}</span> <span class="flag">--status</span>
            <span class="string">{escape(STATUS)}</span> █
          </p>
        </div>
      </div>
    </div>
  </foreignObject>
</svg>
"""

with open("terminal.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)

print("terminal.svg updated with dark cyan color scheme!")
```[cite: 1, 10]

---

### Step 2: Regenerate and Push
Run these commands in your VS Code terminal to generate the new SVG file and push it live[cite: 1, 5]:

```bash
python make_terminal.py
git add make_terminal.py terminal.svg
git commit -m "Update terminal card to exact color theme"
git push origin main
```[cite: 1, 5]
