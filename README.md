# Smode StreamDiffusion Control

*[Version française](README.fr.md)*

> **Experimental, not an official Smode tool.** Built by trial and error against the Oil API (see [smode-oil-reference](https://github.com/gyomh/smode-oil-reference)). Tested on Smode Compose R15.

A Script that **drives the *Stream Diffusion* modifier** of a Compo through drop-down menus, working around the
native UI where the *Model Name* has no preset for some models (e.g. `IDKiro/sdxs-512-0.9`) and *Mode* /
*Acceleration* are locked once the StreamDiffusion process is connected. The Oil API still lets you change them.

- **Model Name**: presets (`stabilityai/sd-turbo`, `IDKiro/sdxs-512-0.9`) or *Custom...* with a free text field;
- **Mode**: Image To Image / Text To Image;
- **Acceleration**: None / TorchCompile / TensorRT.

## Install

1. Drag `streamdiff_ctrl.py` into a Smode project that contains a *Stream Diffusion* modifier, **Launch Mode =
   Manual**.
2. Choose the model, mode and acceleration, then execute: the Script finds the modifier by name and applies them.

## License

MIT — see [LICENSE](LICENSE).
