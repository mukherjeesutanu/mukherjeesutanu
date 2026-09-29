import math, random
random.seed(11)
W, H, DUR = 960, 320, 16
CX, CY = 480, 175
out = []; A = out.append
A(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="Fira Code, monospace">')
A('''<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0b1622"/><stop offset=".55" stop-color="#14283a"/><stop offset="1" stop-color="#1d3b50"/></linearGradient>
<radialGradient id="prot" cx=".42" cy=".38" r=".75"><stop offset="0" stop-color="#8fb3ff"/><stop offset=".55" stop-color="#4a64c9"/><stop offset="1" stop-color="#2a347a"/></radialGradient>
<radialGradient id="hot" cx=".5" cy=".5"><stop offset="0" stop-color="#ff5d8f" stop-opacity=".95"/><stop offset=".6" stop-color="#ff5d8f" stop-opacity=".35"/><stop offset="1" stop-color="#ff5d8f" stop-opacity="0"/></radialGradient>
<radialGradient id="cryp" cx=".5" cy=".5"><stop offset="0" stop-color="#ffd166" stop-opacity=".95"/><stop offset=".6" stop-color="#ffd166" stop-opacity=".3"/><stop offset="1" stop-color="#ffd166" stop-opacity="0"/></radialGradient>
<radialGradient id="gO" cx=".35" cy=".35"><stop offset="0" stop-color="#ff9d9d"/><stop offset="1" stop-color="#c62f2f"/></radialGradient>
<radialGradient id="gH" cx=".35" cy=".35"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#b9c4cc"/></radialGradient>
<filter id="glow"><feGaussianBlur stdDeviation="2.4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<filter id="soft"><feGaussianBlur stdDeviation="6"/></filter>
<pattern id="dots" width="14" height="14" patternUnits="userSpaceOnUse"><circle cx="3" cy="3" r="1.1" fill="#ffffff" fill-opacity=".10"/></pattern>
</defs>''')
A(f'<rect width="{W}" height="{H}" rx="14" fill="url(#bg)"/>')

# --- protein surface: polar blob; cryptic pocket at angle PK opens mid-loop
PK = math.radians(-35)  # upper-right
def radius(th, phase, pocket):
    r = 112 + 10*math.sin(3*th + phase) + 6*math.sin(5*th - 1.3*phase) + 4*math.cos(7*th + 0.5)
    d = math.atan2(math.sin(th-PK), math.cos(th-PK))
    r -= pocket * 52 * math.exp(-(d/0.2)**2)
    return r * (1.35 if abs(math.cos(th)) > 0 else 1) ** 0 * (1 + 0.35*math.cos(th)**2)
def blob(phase, pocket, n=90):
    pts = [(CX + radius(t, phase, pocket)*math.cos(t), CY + 0.78*radius(t, phase, pocket)*math.sin(t)) for t in (2*math.pi*i/n for i in range(n))]
    d = f'M{pts[0][0]:.1f},{pts[0][1]:.1f}'
    for i in range(n):  # Catmull-Rom -> Bezier
        p0, p1, p2, p3 = pts[i-1], pts[i], pts[(i+1)%n], pts[(i+2)%n]
        c1 = (p1[0]+(p2[0]-p0[0])/6, p1[1]+(p2[1]-p0[1])/6); c2 = (p2[0]-(p3[0]-p1[0])/6, p2[1]-(p3[1]-p1[1])/6)
        d += f' C{c1[0]:.1f},{c1[1]:.1f} {c2[0]:.1f},{c2[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}'
    return d + 'Z'
def surf(th, phase=0, pocket=0, out=10):
    r = radius(th, phase, pocket) + out
    return CX + r*math.cos(th), CY + 0.78*r*math.sin(th)
frames = [(0,0),(0.7,0),(1.4,0.55),(2.1,1),(2.8,1),(3.5,0.5),(4.2,0),(0,0)]
kt = '0;.14;.3;.42;.62;.78;.9;1'
paths = ';'.join(blob(p, k) for p, k in frames)
A(f'<path d="{blob(0,0)}" fill="#6f8cff" opacity=".35" filter="url(#soft)"><animate attributeName="d" dur="{DUR}s" repeatCount="indefinite" keyTimes="{kt}" values="{paths}"/></path>')
A(f'<path d="{blob(0,0)}" fill="url(#prot)" stroke="#a9c1ff" stroke-width="1.5" stroke-opacity=".6"><animate attributeName="d" dur="{DUR}s" repeatCount="indefinite" keyTimes="{kt}" values="{paths}"/></path>')
A(f'<path d="{blob(0,0)}" fill="url(#dots)"><animate attributeName="d" dur="{DUR}s" repeatCount="indefinite" keyTimes="{kt}" values="{paths}"/></path>')
# faint secondary-structure hints inside
for i, (dx, dy, rot) in enumerate([(-60,-20,20),(30,30,-15),(-10,-45,70),(70,-5,40)]):
    A(f'<path d="M{CX+dx-30},{CY+dy} q7.5,-12 15,0 t15,0 t15,0 t15,0" fill="none" stroke="#c9d6ff" stroke-opacity=".28" stroke-width="3" stroke-linecap="round" transform="rotate({rot} {CX+dx} {CY+dy})"/>')

# --- hotspots on surface (angle, color id)
hot = [(math.radians(200), 'hot'), (math.radians(115), 'hot'), (math.radians(265), 'hot'), (PK, 'cryp')]
hpos = []
for th, g in hot:
    x, y = surf(th, 2.1, 1, out=6) if g == 'cryp' else surf(th, 0, 0, out=2)
    hpos.append((x, y))
    A(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="0" fill="url(#{g})"><animate attributeName="r" dur="{DUR}s" repeatCount="indefinite" keyTimes="0;.25;.5;.75;1" values="{ "10;18;24;28;10" if g=="hot" else "0;0;16;30;0" }"/></circle>')

# --- probes: benzene (orange), isopropanol (green), acetonitrile (cyan), acetamide (violet)
def benzene(c):
    ring = [(8*math.cos(math.pi/3*i), 8*math.sin(math.pi/3*i)) for i in range(6)]
    s = ''.join(f'<line x1="{ring[i][0]:.1f}" y1="{ring[i][1]:.1f}" x2="{ring[(i+1)%6][0]:.1f}" y2="{ring[(i+1)%6][1]:.1f}" stroke="{c}" stroke-width="2"/>' for i in range(6))
    return s + ''.join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3" fill="{c}"/>' for x, y in ring)
def ipa(c):
    return f'<line x1="-9" y1="4" x2="0" y2="-1" stroke="{c}" stroke-width="2"/><line x1="9" y1="4" x2="0" y2="-1" stroke="{c}" stroke-width="2"/><line x1="0" y1="-1" x2="0" y2="-10" stroke="{c}" stroke-width="2"/><circle cx="-9" cy="4" r="3.6" fill="{c}"/><circle cx="9" cy="4" r="3.6" fill="{c}"/><circle cy="-1" r="3.6" fill="{c}"/><circle cy="-10" r="3.6" fill="#ff6b6b"/>'
def acn(c):
    return f'<line x1="-10" y1="0" x2="10" y2="0" stroke="{c}" stroke-width="2.4"/><circle cx="-10" r="3.6" fill="{c}"/><circle r="3.6" fill="{c}"/><circle cx="10" r="3.6" fill="#6b8cff"/>'
def acm(c):
    return f'<line x1="-9" y1="3" x2="0" y2="-2" stroke="{c}" stroke-width="2"/><line x1="0" y1="-2" x2="0" y2="-11" stroke="{c}" stroke-width="2"/><line x1="0" y1="-2" x2="9" y2="3" stroke="{c}" stroke-width="2"/><circle cx="-9" cy="3" r="3.4" fill="{c}"/><circle cy="-2" r="3.4" fill="{c}"/><circle cy="-11" r="3.4" fill="#ff6b6b"/><circle cx="9" cy="3" r="3.4" fill="#6b8cff"/>'
kinds = [(benzene, '#ffa94d', 'benzene'), (ipa, '#63e6be', 'isopropanol'), (acn, '#66d9e8', 'acetonitrile'), (acm, '#b197fc', 'acetamide')]

def bulk_point():
    while True:
        x, y = random.uniform(40, W-40), random.uniform(50, H-40)
        if ((x-CX)/175)**2 + ((y-CY)/115)**2 > 1.25 and not (y > H-55 and (x < 330 or x > 640)): return x, y

probes = [  # (kind, target hotspot, dwell start frac, dwell end frac)
    (0, 3, .40, .72), (0, 0, .10, .32), (1, 1, .20, .45), (2, 2, .55, .80),
    (3, 1, .62, .88), (1, 0, .50, .70), (2, 3, .48, .66), (3, 2, .05, .25),
    (0, 2, .80, .96), (1, 3, .70, .80),
]
for kind, hs, t0, t1 in probes:
    fn, col, _ = kinds[kind]
    hx, hy = hpos[hs]
    jx, jy = random.uniform(-6, 6), random.uniform(-6, 6)
    b1, b2, b3, b4 = bulk_point(), bulk_point(), bulk_point(), bulk_point()
    a = max(t0 - .12, .001); z = min(t1 + .12, .999)
    pts = [(0, b1), (a, b2), (t0, (hx+jx, hy+jy)), (t1, (hx+jx, hy+jy)), (z, b3), (1, b1)]
    kts = ';'.join(f'{t:.3f}' for t, _ in pts); vals = ';'.join(f'{p[0]:.0f} {p[1]:.0f}' for _, p in pts)
    rot = random.uniform(0, 360)
    A(f'<g filter="url(#glow)"><animateTransform attributeName="transform" type="translate" dur="{DUR}s" repeatCount="indefinite" keyTimes="{kts}" values="{vals}" calcMode="spline" keySplines="{";".join([".45 0 .55 1"]*5)}"/>')
    A(f'<g><animateTransform attributeName="transform" type="rotate" dur="{DUR}s" repeatCount="indefinite" keyTimes="0;{t0:.3f};{t1:.3f};1" values="{rot:.0f};{rot+170:.0f};{rot+185:.0f};{rot+360:.0f}"/>{fn(col)}</g></g>')
    # binding flash ring
    A(f'<circle cx="{hx+jx:.1f}" cy="{hy+jy:.1f}" r="6" fill="none" stroke="{col}" stroke-width="1.5" opacity="0"><animate attributeName="r" dur="{DUR}s" repeatCount="indefinite" keyTimes="0;{t0:.3f};{t0+.04:.3f};1" values="6;6;22;22"/><animate attributeName="opacity" dur="{DUR}s" repeatCount="indefinite" keyTimes="0;{t0:.3f};{t0+.005:.3f};{t0+.04:.3f};1" values="0;0;.9;0;0"/></circle>')

# --- water background
for i in range(30):
    x, y = bulk_point()
    A(f'<g transform="translate({x:.0f} {y:.0f})" opacity=".35"><g><animateTransform attributeName="transform" type="translate" dur="{random.uniform(4,8):.1f}s" repeatCount="indefinite" values="0 0;{random.uniform(-8,8):.1f} {random.uniform(-8,8):.1f};{random.uniform(-8,8):.1f} {random.uniform(-8,8):.1f};0 0"/><line x1="0" y1="0" x2="-5" y2="4" stroke="#cfd8dc" stroke-width="1.2"/><line x1="0" y1="0" x2="5" y2="4" stroke="#cfd8dc" stroke-width="1.2"/><circle r="3.3" fill="url(#gO)"/><circle cx="-5" cy="4" r="2" fill="url(#gH)"/><circle cx="5" cy="4" r="2" fill="url(#gH)"/></g></g>')

# --- labels
cx_, cy_ = surf(PK, 0, 1, out=40)
A(f'<text x="{cx_+10:.0f}" y="{cy_-6:.0f}" fill="#ffd166" font-size="12" opacity="0">cryptic pocket opens<animate attributeName="opacity" dur="{DUR}s" repeatCount="indefinite" keyTimes="0;.36;.42;.66;.74;1" values="0;0;1;1;0;0"/></text>')
hx, hy = hpos[1]
A(f'<text x="{hx-14:.0f}" y="{hy+34:.0f}" fill="#ff8fab" font-size="12" text-anchor="middle">PPI hotspot</text>')
A('<g font-size="12" fill="#cfe9e6"><text x="22" y="28">▶ mixed-solvent MD · cosolvent probe mapping</text>')
A(f'<text x="{W-22}" y="28" text-anchor="end" fill="#8fb8b3">protein + 5% v/v probes in explicit water</text>')
x0 = 22
for i, (_, col, name) in enumerate(kinds):
    A(f'<circle cx="{x0+6}" cy="{H-22}" r="5" fill="{col}"/><text x="{x0+16}" y="{H-18}" fill="#cfe9e6" font-size="11">{name}</text>')
    x0 += 24 + 7.2*len(name)
A(f'<circle cx="{W-230}" cy="{H-22}" r="6" fill="url(#hot)"/><text x="{W-220}" y="{H-18}" font-size="11" fill="#cfe9e6">hotspot</text>')
A(f'<circle cx="{W-150}" cy="{H-22}" r="6" fill="url(#cryp)"/><text x="{W-140}" y="{H-18}" font-size="11" fill="#cfe9e6">cryptic site</text>')
A('</g></svg>')
open('mukherjeesutanu/assets/mixed-solvent-md.svg', 'w').write('\n'.join(out))
