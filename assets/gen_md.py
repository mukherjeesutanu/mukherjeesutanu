import math, random
random.seed(7)
W, H, DUR = 960, 260, 12  # seconds per loop
out = []
A = out.append
A(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="Fira Code, monospace">')
A('''<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0f2027"/><stop offset=".5" stop-color="#203a43"/><stop offset="1" stop-color="#2c5364"/></linearGradient>
<radialGradient id="gC" cx=".35" cy=".35"><stop offset="0" stop-color="#9fe7df"/><stop offset="1" stop-color="#1b8a80"/></radialGradient>
<radialGradient id="gN" cx=".35" cy=".35"><stop offset="0" stop-color="#9db8ff"/><stop offset="1" stop-color="#3355cc"/></radialGradient>
<radialGradient id="gO" cx=".35" cy=".35"><stop offset="0" stop-color="#ff9d9d"/><stop offset="1" stop-color="#c62f2f"/></radialGradient>
<radialGradient id="gH" cx=".35" cy=".35"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#b9c4cc"/></radialGradient>
<radialGradient id="gL" cx=".35" cy=".35"><stop offset="0" stop-color="#ffe29a"/><stop offset="1" stop-color="#e09b12"/></radialGradient>
<radialGradient id="pocket" cx=".5" cy=".5"><stop offset="0" stop-color="#2ec4b6" stop-opacity=".45"/><stop offset="1" stop-color="#2ec4b6" stop-opacity="0"/></radialGradient>
<filter id="glow"><feGaussianBlur stdDeviation="2.2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" fill="none" stroke="#ffffff" stroke-opacity=".04"/></pattern>
</defs>''')
A(f'<rect width="{W}" height="{H}" rx="14" fill="url(#bg)"/><rect width="{W}" height="{H}" rx="14" fill="url(#grid)"/>')

def jitter(n, amp):
    pts = [(random.uniform(-amp, amp), random.uniform(-amp, amp)) for _ in range(n)]
    pts.append(pts[0])
    return ';'.join(f'{x:.1f} {y:.1f}' for x, y in pts)

# --- water molecules (Brownian jiggle + slow drift + rotation)
for i in range(38):
    x, y = random.uniform(20, W-20), random.uniform(20, H-20)
    if 330 < x < 700 and 60 < y < 200: continue
    if y < 42 or (y > 195 and (x < 260 or x > 660)): continue
    rot0 = random.uniform(0, 360)
    A(f'<g transform="translate({x:.0f} {y:.0f})" opacity=".55"><g>')
    A(f'<animateTransform attributeName="transform" type="translate" dur="{random.uniform(5,9):.1f}s" repeatCount="indefinite" values="{jitter(6, 9)}"/>')
    A(f'<g><animateTransform attributeName="transform" type="rotate" dur="{random.uniform(4,10):.1f}s" repeatCount="indefinite" values="{rot0:.0f};{rot0+random.choice([-1,1])*360:.0f}"/>')
    A('<line x1="0" y1="0" x2="-6" y2="4.5" stroke="#cfd8dc" stroke-width="1.4"/><line x1="0" y1="0" x2="6" y2="4.5" stroke="#cfd8dc" stroke-width="1.4"/>')
    A('<circle r="4" fill="url(#gO)"/><circle cx="-6" cy="4.5" r="2.4" fill="url(#gH)"/><circle cx="6" cy="4.5" r="2.4" fill="url(#gH)"/>')
    A('</g></g></g>')

# --- protein backbone: helix-like chain whose atoms thermally fluctuate
cx0, cy0 = 360, 130
nres = 26
atoms = []
for k in range(nres):
    t = k / (nres - 1)
    x = cx0 + t * 330
    y = cy0 + 38 * math.sin(k * 0.95) + (18 if 9 < k < 17 else 0) * math.sin(math.pi * (k-9)/8)
    atoms.append((x, y, 'N' if k % 3 == 0 else ('O' if k % 7 == 3 else 'C')))
# pocket glow around residues 10-16
px, py = (atoms[13][0], atoms[13][1] - 46)
A(f'<circle cx="{px:.0f}" cy="{py:.0f}" r="46" fill="url(#pocket)"><animate attributeName="r" values="38;50;38" dur="3s" repeatCount="indefinite"/></circle>')
# per-atom displacement trajectories (shared frames so bonds follow atoms)
F = 7
disp = [[(random.uniform(-4, 4), random.uniform(-4, 4)) for _ in range(F)] for _ in atoms]
for d in disp: d.append(d[0])
kt = ';'.join(f'{i/F:.3f}' for i in range(F+1))
for k in range(nres - 1):
    (x1, y1, _), (x2, y2, _) = atoms[k], atoms[k+1]
    xs1 = ';'.join(f'{x1+dx:.1f}' for dx, _ in disp[k]); ys1 = ';'.join(f'{y1+dy:.1f}' for _, dy in disp[k])
    xs2 = ';'.join(f'{x2+dx:.1f}' for dx, _ in disp[k+1]); ys2 = ';'.join(f'{y2+dy:.1f}' for _, dy in disp[k+1])
    A(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#7fd8ce" stroke-width="4" stroke-linecap="round" opacity=".85" filter="url(#glow)">')
    for a, v in (('x1', xs1), ('y1', ys1), ('x2', xs2), ('y2', ys2)):
        A(f'<animate attributeName="{a}" dur="2.4s" repeatCount="indefinite" keyTimes="{kt}" values="{v}" calcMode="spline" keySplines="{";".join([".45 0 .55 1"]*F)}"/>')
    A('</line>')
for k, (x, y, el) in enumerate(atoms):
    r = 7 if el != 'O' else 6.5
    xs = ';'.join(f'{x+dx:.1f}' for dx, _ in disp[k]); ys = ';'.join(f'{y+dy:.1f}' for _, dy in disp[k])
    A(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="url(#g{el})">')
    A(f'<animate attributeName="cx" dur="2.4s" repeatCount="indefinite" keyTimes="{kt}" values="{xs}" calcMode="spline" keySplines="{";".join([".45 0 .55 1"]*F)}"/>')
    A(f'<animate attributeName="cy" dur="2.4s" repeatCount="indefinite" keyTimes="{kt}" values="{ys}" calcMode="spline" keySplines="{";".join([".45 0 .55 1"]*F)}"/>')
    A('</circle>')

# --- ligand (benzene-like ring with substituent) diffusing in, binding, unbinding
ring = [(11*math.cos(math.pi/3*i + math.pi/6), 11*math.sin(math.pi/3*i + math.pi/6)) for i in range(6)]
lig = ['<g>']
for i in range(6):
    (a, b), (c, d) = ring[i], ring[(i+1) % 6]
    lig.append(f'<line x1="{a:.1f}" y1="{b:.1f}" x2="{c:.1f}" y2="{d:.1f}" stroke="#ffd166" stroke-width="2.4"/>')
lig.append(f'<line x1="{ring[0][0]:.1f}" y1="{ring[0][1]:.1f}" x2="22" y2="11" stroke="#ffd166" stroke-width="2.4"/>')
lig += [f'<circle cx="{a:.1f}" cy="{b:.1f}" r="4.2" fill="url(#gL)"/>' for a, b in ring]
lig.append('<circle cx="22" cy="11" r="4.6" fill="url(#gO)"/><circle cx="-2" cy="-24" r="0"/>')
lig.append('</g>')
wp = [(150,70),(230,40),(300,170),(px-40,py+20),(px,py),(px,py),(px,py),(px+70,py-40),(820,60),(880,180),(640,235),(330,225),(120,160),(150,70)]
kts = [0,.08,.17,.25,.3,.45,.58,.63,.7,.78,.85,.92,.97,1]
A(f'<g filter="url(#glow)"><animateTransform attributeName="transform" type="translate" dur="{DUR}s" repeatCount="indefinite" keyTimes="{";".join(map(str,kts))}" values="{";".join(f"{x:.0f} {y:.0f}" for x,y in wp)}" calcMode="spline" keySplines="{";".join([".4 0 .6 1"]*(len(wp)-1))}"/>')
A(f'<g><animateTransform attributeName="transform" type="rotate" dur="{DUR}s" repeatCount="indefinite" values="0;160;170;175;175;400" keyTimes="0;.25;.3;.45;.58;1"/>{"".join(lig)}</g></g>')
# H-bond flashes while bound
for k in (12, 14):
    x, y, _ = atoms[k]
    A(f'<line x1="{x:.0f}" y1="{y-7:.0f}" x2="{px:.0f}" y2="{py+8:.0f}" stroke="#ffd166" stroke-width="1.6" stroke-dasharray="3 4" opacity="0">')
    A(f'<animate attributeName="opacity" dur="{DUR}s" repeatCount="indefinite" values="0;0;.95;.95;0;0" keyTimes="0;0.3;0.33;0.55;0.58;1"/></line>')
A(f'<text x="{px:.0f}" y="{py-50:.0f}" fill="#ffd166" font-size="12" text-anchor="middle" opacity="0">bound · ΔG &lt; 0<animate attributeName="opacity" dur="{DUR}s" repeatCount="indefinite" values="0;0;1;1;0;0" keyTimes="0;0.31;0.35;0.54;0.58;1"/></text>')

# --- HUD: simulation clock + energy trace
A('<g font-size="12" fill="#cfe9e6" opacity=".9">')
A('<text x="22" y="28">▶ gmx mdrun -deffnm prod</text>')
steps = 12
vals = ';'.join(str(i) for i in range(steps + 1))
for i in range(steps):
    a, b = i/steps, (i+1)/steps
    ks, vs = ([0], [1]) if i == 0 else ([0, a], [0, 1])
    if b < 1: ks.append(b); vs.append(0)
    kt_ = ";".join(f"{k:.4f}" for k in ks); vals_ = ";".join(map(str, vs))
    A(f'<text x="{W-22}" y="28" text-anchor="end" opacity="0">t = {(i+1)*25:>3} ns<animate attributeName="opacity" dur="{DUR}s" repeatCount="indefinite" calcMode="discrete" keyTimes="{kt_}" values="{vals_}"/></text>')
# energy trace
pts = []
for i in range(121):
    x = 22 + i * 1.7
    y = H - 30 - 14*math.exp(-i/25) - 3*math.sin(i*0.9) - random.uniform(-2, 2)
    pts.append(f'{x:.1f},{y:.1f}')
A(f'<polyline points="{" ".join(pts)}" fill="none" stroke="#2ec4b6" stroke-width="1.6" stroke-dasharray="400" stroke-dashoffset="400"><animate attributeName="stroke-dashoffset" values="400;0" dur="{DUR}s" repeatCount="indefinite"/></polyline>')
A(f'<text x="22" y="{H-12}" font-size="11" fill="#8fb8b3">potential energy</text>')
A(f'<text x="{W-22}" y="{H-12}" font-size="11" fill="#8fb8b3" text-anchor="end">NPT · 300 K · 1 bar · explicit water</text>')
A('</g></svg>')
open('mukherjeesutanu/assets/md-simulation.svg', 'w').write('\n'.join(out))
