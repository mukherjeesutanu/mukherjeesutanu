<!-- Header -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f2027,50:203a43,100:2c5364&height=200&section=header&text=Sutanu%20Mukhopadhyay&fontSize=46&fontColor=ffffff&fontAlignY=36&desc=Computational%20Biophysics%20%C2%B7%20Allostery%20%C2%B7%20Drug%20Discovery&descAlignY=58&descSize=18&animation=fadeIn" alt="header"/>
</p>

<p align="center">
  <a href="https://github.com/mukherjeesutanu">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=20&duration=3500&pause=900&color=2EC4B6&center=true&vCenter=true&width=720&lines=Senior+Research+Fellow+%40+S.+N.+Bose+National+Centre%2C+Kolkata;Mixed-solvent+MD+%E2%86%92+cryptic+%26+allosteric+pockets;Protein%E2%80%93protein+interaction+hotspot+mapping;Free+energy+%C2%B7+ML+potentials+%C2%B7+docking+%26+rescoring;Open+to+postdoctoral+opportunities+%F0%9F%A7%AC" alt="typing"/>
  </a>
</p>

<p align="center">
  <a href="https://scholar.google.com/citations?user=9pwowmcAAAAJ&hl=en"><img src="https://img.shields.io/badge/Google%20Scholar-4285F4?style=for-the-badge&logo=googlescholar&logoColor=white" alt="Google Scholar"/></a>
  <a href="https://www.researchgate.net/profile/Sutanu-Mukhopadhyay-2"><img src="https://img.shields.io/badge/ResearchGate-00CCBB?style=for-the-badge&logo=researchgate&logoColor=white" alt="ResearchGate"/></a>
  <a href="https://orcid.org/0000-0001-8243-2138"><img src="https://img.shields.io/badge/ORCID-A6CE39?style=for-the-badge&logo=orcid&logoColor=white" alt="ORCID"/></a>
  <a href="https://www.linkedin.com/in/sutanu-mukhopadhyay-3681851aa/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
  <a href="mailto:sutanu.mukhopadhyay@bose.res.in"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/></a>
</p>

<p align="center">
  <img src="assets/md-simulation.svg" width="100%" alt="Animated molecular dynamics: a ligand diffuses through explicit water, binds a protein pocket and unbinds"/>
</p>

---

## 🧬 About me

I'm a PhD researcher (Senior Research Fellow) in the **Department of Chemical and Biological Sciences, S. N. Bose National Centre for Basic Sciences, Kolkata**. I use molecular simulation and data-driven methods to find **allosteric and cryptic binding sites** and to **modulate protein–protein interactions (PPIs)** for drug discovery.

- 🔬 **Current focus:** mixed-solvent / mixed amino-acid MD for PPI hotspot and cryptic-pocket mapping (PLK1 PBD, PCSK9)
- ⚗️ **Methods:** all-atom MD, enhanced sampling, alchemical free energy, neural-network potentials (ANI-2x in GROMACS), docking and ML rescoring, structural-ensemble generation (BioEmu)
- 🎯 **Looking for:** postdoctoral positions in computational biophysics, allostery and structure-based drug design

## 🧪 Mixed-solvent MD in action

<p align="center">
  <img src="assets/mixed-solvent-md.svg" width="100%" alt="Animated mixed-solvent MD: cosolvent probes (benzene, isopropanol, acetonitrile, acetamide) bind and unbind protein-surface hotspots while a cryptic pocket opens"/>
</p>

<p align="center"><sub>Cosolvent probes sample the protein surface, residing longer at PPI hotspots and seeding a transient cryptic pocket, the idea behind <a href="https://doi.org/10.1007/s12039-025-02449-9">PPIscout</a> and my PLK1 / PCSK9 allosteric-pocket work.</sub></p>

## 🛠️ Toolbox

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,bash,linux,git,pytorch,sklearn,latex&theme=dark" alt="skills"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/GROMACS-1f6feb?style=flat-square" />
  <img src="https://img.shields.io/badge/AMBER-e36209?style=flat-square" />
  <img src="https://img.shields.io/badge/MDAnalysis-f4a261?style=flat-square" />
  <img src="https://img.shields.io/badge/RDKit-cc3366?style=flat-square" />
  <img src="https://img.shields.io/badge/AutoDock%20Vina-8957e5?style=flat-square" />
  <img src="https://img.shields.io/badge/ProLIF-0e8a16?style=flat-square" />
  <img src="https://img.shields.io/badge/PyMOL-2c5364?style=flat-square" />
  <img src="https://img.shields.io/badge/VMD-5a6b7b?style=flat-square" />
  <img src="https://img.shields.io/badge/HPC%20(PBS%2FSLURM)-444d56?style=flat-square" />
</p>

## 🚀 Featured project

<table>
<tr>
<td width="100%">

### [vina-rescore](https://github.com/mukherjeesutanu/vina-rescore)
Interaction-fingerprint (PLIF) rescoring of AutoDock Vina poses for **early enrichment** in virtual screening. It uses scaffold-aware cross-validation, LightGBM on ProLIF bitvectors, and BEDROC/EF with bootstrap confidence intervals. It removes Vina's ligand-size bias and recovers the canonical CDK2 hinge Leu83 H-bond as the top discriminative feature.

`Python` · `RDKit` · `ProLIF` · `MDAnalysis` · `LightGBM` · `AutoDock Vina`

</td>
</tr>
</table>

## 📄 Selected publications

| Year | Publication |
|:---:|---|
| 2026 | **Mapping PPI hotspots and unveiling a cryptic allosteric pocket in PLK1 PBD via mixed-solvent MD** — *ChemPhysChem* · [doi](https://doi.org/10.1002/cphc.202500907) |
| 2026 | **Computational strategies for allosteric drug discovery: from cryptic pocket detection to rational design** — *Chem. Commun.* · [doi](https://doi.org/10.1039/d5cc06159h) |
| 2025 | **Mixed-solvent MD reveals a druggable allosteric pocket in the PCSK9 C-terminal domain** — *J. Phys. Chem. B* · [doi](https://doi.org/10.1021/acs.jpcb.5c05530) |
| 2025 | **PPIscout: PPI hotspot mapping using mixed amino acid–water MD** — *J. Chem. Sci.* · [doi](https://doi.org/10.1007/s12039-025-02449-9) |
| 2025 | **Harnessing allostery to modulate protein–protein interactions: from function to therapeutic innovations** — *J. Mol. Biol.* · [doi](https://doi.org/10.1016/j.jmb.2025.169382) |
| 2024 | **Conformational and binding behaviour of human serum albumin induced by surface-active ionic liquids** — *J. Phys. Chem. B* · [doi](https://doi.org/10.1021/acs.jpcb.4c01915) |
| 2024 | **Allosteric hotspots and cryptic sites to modulate PPIs: a molecular thermodynamic approach** — *Biophys. J.* · [doi](https://doi.org/10.1016/j.bpj.2023.11.458) |
| 2022 | **A multidrug efflux protein in *M. tuberculosis*: Tap as a drug-repurposing target** — *Comput. Biol. Med.* · [doi](https://doi.org/10.1016/j.compbiomed.2022.105607) |

<sub>Full list on <a href="https://scholar.google.com/citations?user=9pwowmcAAAAJ&hl=en">Google Scholar</a>.</sub>

## 📊 GitHub activity

<p align="center">
  <img height="165" src="https://github-readme-stats.vercel.app/api?username=mukherjeesutanu&show_icons=true&hide_border=true&theme=tokyonight&include_all_commits=true&count_private=true" alt="stats"/>
  <img height="165" src="https://streak-stats.demolab.com?user=mukherjeesutanu&theme=tokyonight&hide_border=true" alt="streak"/>
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/mukherjeesutanu/mukherjeesutanu/output/github-snake-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/mukherjeesutanu/mukherjeesutanu/output/github-snake.svg" />
    <img alt="contribution snake" src="https://raw.githubusercontent.com/mukherjeesutanu/mukherjeesutanu/output/github-snake.svg" />
  </picture>
</p>

<!-- Footer -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:2c5364,50:203a43,100:0f2027&height=110&section=footer" alt="footer"/>
</p>
