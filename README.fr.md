# Smode StreamDiffusion Control

*[English version](README.md)*

> **Expérimental, pas un outil officiel Smode.** Construit par essais et erreurs sur l'API Oil (voir [smode-oil-reference](https://github.com/gyomh/smode-oil-reference)). Testé sur Smode Compose R15.

Un Script qui **pilote le modifier *Stream Diffusion*** d'une Compo via des menus déroulants, pour contourner l'UI
native où *Model Name* n'a pas de preset pour certains modèles (ex. `IDKiro/sdxs-512-0.9`) et où *Mode* /
*Acceleration* sont verrouillés une fois le process StreamDiffusion connecté. L'API Oil permet quand même de les
changer.

- **Model Name** : presets (`stabilityai/sd-turbo`, `IDKiro/sdxs-512-0.9`) ou *Custom...* avec un champ texte libre ;
- **Mode** : Image To Image / Text To Image ;
- **Acceleration** : None / TorchCompile / TensorRT.

## Installation

1. Glissez `streamdiff_ctrl.py` dans un projet Smode contenant un modifier *Stream Diffusion*, **Launch Mode =
   Manual**.
2. Choisissez le modèle, le mode et l'accélération, puis exécutez : le Script retrouve le modifier par son nom et les
   applique.

## Licence

MIT — voir [LICENSE](LICENSE).
