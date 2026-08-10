# -*- coding: utf-8 -*-
"""Gera as plantas de luz (planta baixa + corte lateral) como SVG estatico."""
import math

S = 64.0          # px por metro (planta)
CX, CY = 212.0, 236.0
SE = 62.0         # px por metro (corte)
FLOOR = 336.0
EX = 46.0

def pos(az, d):
    a = math.radians(az)
    return CX - math.sin(a) * d * S, CY + math.cos(a) * d * S

def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def light_box(x, y, az, w_cm, col, label, sub):
    """Fonte desenhada com a largura fisica real do modificador."""
    w = max(9.0, (w_cm / 100.0) * S * 0.55)
    h = 7.0
    a = -az  # a face do modificador aponta para o sujeito
    o = []
    o.append(f'<g transform="translate({x:.1f},{y:.1f}) rotate({a:.1f})">')
    o.append(f'<rect x="{-w/2:.1f}" y="{-h/2:.1f}" width="{w:.1f}" height="{h:.1f}" rx="1.5" '
             f'fill="{col}" stroke="var(--plot-line)" stroke-width="0.8"/>')
    o.append(f'<line x1="{-w/2:.1f}" y1="{h/2+1:.1f}" x2="{w/2:.1f}" y2="{h/2+1:.1f}" '
             f'stroke="{col}" stroke-width="1.6" opacity=".55"/>')
    o.append('</g>')
    ta = "start" if x > CX - 6 else "end"
    dx = 11 if ta == "start" else -11
    o.append(f'<text x="{x+dx:.1f}" y="{y-3:.1f}" text-anchor="{ta}" class="lb" fill="{col}">{esc(label)}</text>')
    o.append(f'<text x="{x+dx:.1f}" y="{y+8:.1f}" text-anchor="{ta}" class="ls">{esc(sub)}</text>')
    return "".join(o)

def ray(x, y, dash="3 3", col="var(--plot-dim)"):
    return (f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{CX:.1f}" y2="{CY:.1f}" stroke="{col}" '
            f'stroke-width="1" stroke-dasharray="{dash}"/>')

def arc_label(az, d, txt):
    """Arco cotando o azimute entre o eixo da lente e a fonte."""
    r = 34.0
    x0, y0 = CX, CY + r
    a = math.radians(az)
    x1, y1 = CX - math.sin(a) * r, CY + math.cos(a) * r
    sweep = 0 if az > 0 else 1
    mid = math.radians(az / 2.0)
    mx, my = CX - math.sin(mid) * (r + 13), CY + math.cos(mid) * (r + 13)
    return (f'<path d="M{x0:.1f} {y0:.1f} A{r} {r} 0 0 {sweep} {x1:.1f} {y1:.1f}" fill="none" '
            f'stroke="var(--key)" stroke-width="1.2"/>'
            f'<text x="{mx:.1f}" y="{my:.1f}" text-anchor="middle" class="ls" fill="var(--key)">{txt}</text>')

def plan(cfg):
    o = ['<svg viewBox="0 0 424 398" role="img" aria-label="Planta baixa do setup de luz">']
    o.append('<rect width="424" height="398" fill="var(--plot-bg)" rx="4"/>')
    # aneis de distancia
    for m in (1, 2):
        o.append(f'<circle cx="{CX}" cy="{CY}" r="{m*S:.0f}" fill="none" stroke="var(--plot-grid)" '
                 f'stroke-width="1" stroke-dasharray="2 4"/>')
        o.append(f'<text x="{CX+4:.0f}" y="{CY-m*S+11:.0f}" class="ls">{m} m</text>')
    # eixo da lente
    o.append(f'<line x1="{CX}" y1="{CY}" x2="{CX}" y2="{CY+2.3*S:.0f}" stroke="var(--plot-grid)" stroke-width="1"/>')
    # parede de fundo
    wy = CY - cfg["bg_dist"] * S
    o.append(f'<line x1="26" y1="{wy:.0f}" x2="398" y2="{wy:.0f}" stroke="var(--plot-line)" stroke-width="3"/>')
    for i in range(26, 398, 13):
        o.append(f'<line x1="{i}" y1="{wy:.0f}" x2="{i-7}" y2="{wy-7:.0f}" stroke="var(--plot-line)" stroke-width="1" opacity=".5"/>')
    o.append(f'<text x="30" y="{wy-12:.0f}" class="ls">FUNDO · {cfg["bg_dist"]:.1f} m · −{cfg["bg_stops"]:.1f} stop</text>')
    # fontes
    kx, ky = pos(cfg["key_az"], cfg["key_d"])
    o.append(ray(kx, ky, "4 3", "var(--key)"))
    o.append(arc_label(cfg["key_az"], cfg["key_d"], f'{cfg["key_az"]:.0f}°'))
    o.append(light_box(kx, ky, cfg["key_az"], cfg["key_size"], "var(--key)", "KEY", cfg["key_mod"]))
    if cfg.get("fill_az") is not None:
        fx, fy = pos(cfg["fill_az"], cfg["fill_d"])
        o.append(ray(fx, fy, "3 3", "var(--fill)"))
        o.append(light_box(fx, fy, cfg["fill_az"], cfg["fill_size"], "var(--fill)", "FILL", cfg["fill_mod"]))
    if cfg.get("flag_az") is not None:
        gx, gy = pos(cfg["flag_az"], cfg["flag_d"])
        a = -cfg["flag_az"]
        o.append(f'<g transform="translate({gx:.1f},{gy:.1f}) rotate({a:.1f})">'
                 f'<rect x="-15" y="-2.5" width="30" height="5" fill="var(--plot-flag)"/></g>')
        ta = "start" if gx > CX else "end"
        dx = 19 if ta == "start" else -19
        o.append(f'<text x="{gx+dx:.0f}" y="{gy-2:.0f}" text-anchor="{ta}" class="lb" fill="var(--plot-flagt)">BANDEIRA</text>')
        o.append(f'<text x="{gx+dx:.0f}" y="{gy+9:.0f}" text-anchor="{ta}" class="ls">negativa · {cfg["flag_d"]:.2f} m</text>')
    if cfg.get("rim_az") is not None:
        rx, ry = pos(cfg["rim_az"], cfg["rim_d"])
        o.append(ray(rx, ry, "2 3", "var(--plot-rim)"))
        o.append(light_box(rx, ry, cfg["rim_az"], cfg["rim_size"], "var(--plot-rim)", "RIM", cfg["rim_mod"]))
    if cfg.get("bglight"):
        bx, by = CX + cfg["bglight"][0] * S, wy + 16
        o.append(f'<circle cx="{bx:.0f}" cy="{by:.0f}" r="6" fill="var(--plot-bgl)"/>')
        o.append(f'<text x="{bx+11:.0f}" y="{by+4:.0f}" class="ls" fill="var(--plot-bgl)">{esc(cfg["bglight"][1])}</text>')
    # sujeito
    o.append(f'<circle cx="{CX}" cy="{CY}" r="10" fill="var(--plot-sub)" stroke="var(--plot-line)" stroke-width="2"/>')
    o.append(f'<path d="M{CX-4:.0f} {CY+9:.0f} L{CX:.0f} {CY+15:.0f} L{CX+4:.0f} {CY+9:.0f} Z" fill="var(--plot-line)"/>')
    o.append(f'<text x="{CX+15:.0f}" y="{CY+4:.0f}" class="lb">SUJEITO</text>')
    # camera
    cy2 = CY + cfg["cam_d"] * S
    o.append(f'<path d="M{CX-10:.0f} {cy2:.0f} L{CX+10:.0f} {cy2:.0f} L{CX:.0f} {cy2-13:.0f} Z" fill="var(--plot-line)"/>')
    o.append(f'<text x="{CX+15:.0f}" y="{cy2+4:.0f}" class="lb">CÂMERA · {cfg["cam_d"]:.1f} m · {cfg["lens"]}</text>')
    o.append('</svg>')
    return "".join(o)

def elev(cfg):
    o = ['<svg viewBox="0 0 300 372" role="img" aria-label="Corte lateral com alturas das fontes">']
    o.append('<rect width="300" height="372" fill="var(--plot-bg)" rx="4"/>')
    o.append(f'<line x1="18" y1="{FLOOR}" x2="284" y2="{FLOOR}" stroke="var(--plot-line)" stroke-width="2"/>')
    for i in range(18, 284, 11):
        o.append(f'<line x1="{i}" y1="{FLOOR}" x2="{i-6}" y2="{FLOOR+6}" stroke="var(--plot-line)" stroke-width="1" opacity=".45"/>')
    # escala vertical
    for m in (1, 2):
        y = FLOOR - m * SE
        o.append(f'<line x1="18" y1="{y:.0f}" x2="284" y2="{y:.0f}" stroke="var(--plot-grid)" stroke-width="1" stroke-dasharray="2 5"/>')
        o.append(f'<text x="20" y="{y-4:.0f}" class="ls">{m},0 m</text>')
    # sujeito sentado/em pe
    eye = FLOOR - cfg["eye_h"] * SE
    o.append(f'<ellipse cx="{EX+94}" cy="{eye-8:.0f}" rx="13" ry="16" fill="var(--plot-sub2)"/>')
    o.append(f'<path d="M{EX+72} {FLOOR:.0f} L{EX+78} {eye+16:.0f} Q{EX+94} {eye+7:.0f} {EX+110} {eye+16:.0f} L{EX+116} {FLOOR:.0f} Z" fill="var(--plot-sub2)"/>')
    o.append(f'<circle cx="{EX+89}" cy="{eye:.0f}" r="2.4" fill="var(--key)"/>')
    o.append(f'<circle cx="{EX+99}" cy="{eye:.0f}" r="2.4" fill="var(--key)"/>')
    o.append(f'<line x1="18" y1="{eye:.0f}" x2="284" y2="{eye:.0f}" stroke="var(--key)" stroke-width="1" stroke-dasharray="4 3" opacity=".6"/>')
    o.append(f'<text x="248" y="{eye-7:.0f}" text-anchor="end" class="ls" fill="var(--key)">olhos · {cfg["eye_h"]:.2f} m</text>')
    # key em pedestal
    ky = FLOOR - cfg["key_h"] * SE
    kx = EX + 16
    o.append(f'<line x1="{kx}" y1="{FLOOR:.0f}" x2="{kx}" y2="{ky:.0f}" stroke="var(--plot-line)" stroke-width="2"/>')
    o.append(f'<line x1="{kx-11}" y1="{FLOOR:.0f}" x2="{kx+11}" y2="{FLOOR:.0f}" stroke="var(--plot-line)" stroke-width="3"/>')
    t = cfg["key_tilt"]
    o.append(f'<g transform="translate({kx},{ky:.0f}) rotate({t})">'
             f'<rect x="-4" y="-17" width="8" height="34" rx="2" fill="var(--key)"/></g>')
    o.append(f'<text x="20" y="26" class="lb" fill="var(--key)">KEY</text>')
    o.append(f'<text x="20" y="39" class="ls">{cfg["key_h"]:.2f} m · inclinação {abs(t)}°</text>')
    # feixe
    o.append(f'<path d="M{kx+6} {ky-10:.0f} L{EX+82} {eye-16:.0f} L{EX+82} {eye+12:.0f} Z" fill="var(--key)" opacity=".14"/>')
    if cfg.get("rim_az") is not None:
        ry = FLOOR - cfg["rim_h"] * SE
        rx = EX + 166
        o.append(f'<line x1="{rx}" y1="{FLOOR:.0f}" x2="{rx}" y2="{ry:.0f}" stroke="var(--plot-line)" stroke-width="2"/>')
        o.append(f'<line x1="{rx-11}" y1="{FLOOR:.0f}" x2="{rx+11}" y2="{FLOOR:.0f}" stroke="var(--plot-line)" stroke-width="3"/>')
        o.append(f'<g transform="translate({rx},{ry:.0f}) rotate({cfg["rim_tilt"]})">'
                 f'<rect x="-3" y="-11" width="6" height="22" rx="2" fill="var(--plot-rim)"/></g>')
        o.append(f'<text x="280" y="26" text-anchor="end" class="lb" fill="var(--plot-rim)">RIM</text>')
        o.append(f'<text x="280" y="39" text-anchor="end" class="ls">{cfg["rim_h"]:.2f} m</text>')
    # camera
    cy2 = FLOOR - cfg["cam_h"] * SE
    o.append(f'<line x1="266" y1="{FLOOR:.0f}" x2="266" y2="{cy2:.0f}" stroke="var(--plot-line)" stroke-width="2"/>')
    o.append(f'<rect x="256" y="{cy2-7:.0f}" width="20" height="13" rx="2" fill="var(--plot-line)"/>')
    o.append(f'<text x="282" y="{cy2+22:.0f}" text-anchor="end" class="ls">câmera</text>')
    o.append(f'<text x="282" y="{cy2+34:.0f}" text-anchor="end" class="ls">{cfg["cam_h"]:.2f} m</text>')
    o.append('</svg>')
    return "".join(o)

SETUPS = [
 dict(id="autoridade", name="Autoridade frontal", tag="O padrão VSL", ratio="2:1", temp="4300 K", ire="67 IRE",
      use="O setup de trabalho. Frontal o bastante para o espectador ler microexpressão — que é como o cérebro decide se confia — e com desenho suficiente para o rosto não chapar. Serve o corpo inteiro do argumento.",
      key_az=20, key_d=1.20, key_size=120, key_h=1.95, key_tilt=-25, key_mod="softbox 90×120",
      fill_az=-50, fill_d=1.30, fill_size=100, fill_mod="rebatedor branco",
      rim_az=-140, rim_d=1.40, rim_size=60, rim_h=2.10, rim_tilt=22, rim_mod="strip 30×120",
      flag_az=None, bg_dist=2.2, bg_stops=1.5, bglight=(0.7, "grid 4300 K"),
      cam_d=2.0, cam_h=1.55, eye_h=1.55, lens="50 mm",
      note="Se o rosto chapar, não gire a key — puxe o rebatedor 30 cm para trás. Você ganha modelagem sem perder frontalidade."),
 dict(id="borboleta", name="Borboleta / clamshell", tag="CTA e oferta", ratio="1,5:1", temp="3900 K", ire="70 IRE",
      use="Máxima abertura facial, sombra mínima e simétrica sob o nariz. Nada parece escondido — por isso é o setup do CTA, da garantia e da quebra de objeção. Use por pouco tempo: sustentado, vira propaganda de creme.",
      key_az=0, key_d=1.00, key_size=120, key_h=2.15, key_tilt=-48, key_mod="octabox 120",
      fill_az=-14, fill_d=0.75, fill_size=100, fill_mod="rebatedor no colo",
      rim_az=None, rim_d=0, rim_size=0, rim_h=0, rim_tilt=0, rim_mod="",
      flag_az=None, bg_dist=2.0, bg_stops=1.2, bglight=(0.0, "wash suave"),
      cam_d=1.9, cam_h=1.57, eye_h=1.55, lens="85 mm",
      note="O rebatedor no colo é o que fecha a 'concha'. Sem ele o queixo e o pescoço afundam e o setup vira só uma key alta."),
 dict(id="rembrandt", name="Rembrandt", tag="Virada e narrativa", ratio="4:1", temp="3600 K", ire="62 IRE",
      use="O triângulo de luz na bochecha sombreada. Marca a mudança de temperatura do argumento — história de origem, mecanismo único, revelação. Não é para o VSL inteiro.",
      key_az=45, key_d=1.50, key_size=60, key_h=2.20, key_tilt=-42, key_mod="softbox 60×90 + grid",
      fill_az=None, fill_d=0, fill_size=0, fill_mod="",
      rim_az=-135, rim_d=1.30, rim_size=30, rim_h=2.10, rim_tilt=26, rim_mod="strip 3200 K",
      flag_az=-60, flag_d=0.80, bg_dist=2.6, bg_stops=2.2, bglight=(-0.9, "prática 2700 K"),
      cam_d=2.1, cam_h=1.55, eye_h=1.55, lens="85 mm",
      note="O triângulo só fecha se a key estiver acima da linha dos olhos e o nariz apontar para a sombra. Se ele vazar até a orelha, a key está baixa demais."),
 dict(id="split", name="Split", tag="Dor e conflito", ratio="8:1", temp="5200 K", ire="58 IRE",
      use="Metade do rosto na luz, metade na sombra. Leitura de conflito puro — seção de dor, inimigo comum. Custa confiança a cada segundo, então entra em inserts curtos e sai.",
      key_az=82, key_d=1.40, key_size=45, key_h=1.72, key_tilt=-14, key_mod="fonte dura 45 cm",
      fill_az=None, fill_d=0, fill_size=0, fill_mod="",
      rim_az=-150, rim_d=1.20, rim_size=30, rim_h=2.00, rim_tilt=30, rim_mod="strip fraco",
      flag_az=-45, flag_d=0.70, bg_dist=3.0, bg_stops=3.4, bglight=None,
      cam_d=2.2, cam_h=1.53, eye_h=1.55, lens="85 mm",
      note="Fundo a 3 m e −3,4 stops: sem isso a sombra do rosto encosta numa parede visível e o efeito desmonta."),
 dict(id="studio", name="Estúdio internet", tag="Gancho e prova", ratio="2:1", temp="4600 K", ire="68 IRE",
      use="O visual de canal de YouTube: contorno forte, fundo com profundidade e cor. Alta leitura no feed, boa para o gancho e para as seções de prova. É o setup que mais parece caro pelo que custa.",
      key_az=28, key_d=1.10, key_size=100, key_h=2.00, key_tilt=-26, key_mod="octabox 100",
      fill_az=-55, fill_d=1.60, fill_size=60, fill_mod="painel LED difuso",
      rim_az=-138, rim_d=1.25, rim_size=120, rim_h=2.05, rim_tilt=24, rim_mod="tubo LED 3000 K",
      flag_az=None, bg_dist=2.4, bg_stops=1.1, bglight=(-1.1, "painel 7200 K + prática"),
      cam_d=2.0, cam_h=1.56, eye_h=1.55, lens="50 mm",
      note="O fundo a apenas −1,1 stop é intencional: aqui o cenário trabalha. Mas nada no fundo pode ser mais saturado que o rosto."),
 dict(id="janela", name="Janela + rebatedor", tag="Custo zero", ratio="3:1", temp="5600 K", ire="64 IRE",
      use="Sem equipamento nenhum. A janela é a key — enorme e suave. Um isopor branco do lado oposto fecha o ratio. Bate a maioria dos sets de três pontos mal balanceados.",
      key_az=38, key_d=0.95, key_size=150, key_h=1.60, key_tilt=0, key_mod="janela ~150 cm",
      fill_az=-55, fill_d=1.10, fill_size=100, fill_mod="isopor 100×70",
      rim_az=None, rim_d=0, rim_size=0, rim_h=0, rim_tilt=0, rim_mod="",
      flag_az=None, bg_dist=2.0, bg_stops=1.8, bglight=None,
      cam_d=1.9, cam_h=1.55, eye_h=1.55, lens="50 mm",
      note="Grave sempre no mesmo horário. A janela muda de intensidade e de temperatura ao longo do dia — é a única fonte deste setup que você não controla."),
]

def card(c):
    spec = f'''<div class="plot-spec">
<dl class="dl">
<dt>Key</dt><dd>{esc(c["key_mod"])}</dd>
<dt>Azimute / altura</dt><dd>{c["key_az"]:.0f}° · {c["key_h"]:.2f} m</dd>
<dt>Distância / inclin.</dt><dd>{c["key_d"]:.2f} m · {abs(c["key_tilt"])}°</dd>
<dt>Fill</dt><dd>{esc(c["fill_mod"]) if c["fill_mod"] else "— bandeira negativa"}</dd>
<dt>Rim</dt><dd>{esc(c["rim_mod"]) if c["rim_mod"] else "—"}</dd>
<dt>Fundo</dt><dd>{c["bg_dist"]:.1f} m · −{c["bg_stops"]:.1f} st</dd>
<dt>Ratio alvo</dt><dd>{c["ratio"]}</dd>
<dt>Temperatura</dt><dd>{c["temp"]}</dd>
<dt>Pele</dt><dd>{c["ire"]}</dd>
<dt>Lente / distância</dt><dd>{c["lens"]} · {c["cam_d"]:.1f} m</dd>
</dl></div>'''
    return f'''<figure class="plot-card" id="setup-{c["id"]}">
<div class="plot-head">
<div><span class="plot-name">{esc(c["name"])}</span><span class="tag k">{esc(c["tag"])}</span></div>
<span class="plot-ratio">{c["ratio"]}</span>
</div>
<p class="plot-use">{esc(c["use"])}</p>
<div class="plot-grid">
<div class="plot-pane"><div class="plot-lab">Planta baixa · vista superior</div>{plan(c)}</div>
<div class="plot-pane"><div class="plot-lab">Corte lateral · alturas</div>{elev(c)}</div>
{spec}
</div>
<figcaption class="plot-note"><b>No set:</b> {esc(c["note"])}</figcaption>
</figure>'''

open("plots.html", "w", encoding="utf-8").write("\n".join(card(c) for c in SETUPS))
print("plantas geradas:", len(SETUPS))
