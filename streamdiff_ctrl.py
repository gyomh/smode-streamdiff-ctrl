#    #########      ###         ###      #########      #########         ###############
# ###               ######   ######   ###         ###   ###      ###      ###
# ###               ###   ###   ###   ###         ###   ###         ###   ###
#    #########      ###   ###   ###   ###         ###   ###         ###   ############
#             ###   ###         ###   ###         ###   ###         ###   ###
#             ###   ###         ###   ###         ###   ###      ###      ###
# ############      ###         ###      #########      #########         ###############
#
# -------------------- "Guillaume Henrion aka [GYOMH]" "08/09/2026" --------------------
# __________________________________________ ___________________________________________
# |                                       | |                                         |
# |    STREAMDIFF CTRL                    | | Pilote le modifier "Stream Diffusion"   |
# |       V1.0                            | | d'une Compo : Model Name / Mode /       |
# |                                       | | Acceleration, via menus deroulants.     |
# |_______________________________________| |_________________________________________|
# |    Instructions :                     | | - Model Name : presets (sd-turbo,       |
# | 1- Choisir Model / Mode / Acceleration| |   sdxs-512-0.9) + "Custom..." (texte     |
# |    (menus CustomEnumeration)          | |   libre dans Custom Model Name)         |
# | 2- Si "Custom..." : remplir           | | - Mode : Image To Image / Text To Image |
# |    Custom Model Name                  | | - Acceleration : None / TorchCompile /  |
# | 3- Execute (Launch Mode = Manual)     | |   TensorRT                              |
# |_______________________________________| |_________________________________________|
#
# HISTORIQUE
# V1.0 - 08/09/2026 - Version initiale. Contourne les menus Model Name (pas de preset
#                      pour sdxs dans l'UI native) et Mode/Acceleration (verrouilles
#                      dans l'UI native une fois le process StreamDiffusion connecte),
#                      qui restent modifiables via l'API Oil/scripting.

# =============== OPTIONS (visibles/modifiables dans le panneau du Script) ===============
modelPreset: Oil.createObject("CustomEnumeration")   # preset de modele (ou "Custom...")
customModelName: Oil.String("")                       # utilise si modelPreset = "Custom..."
modeChoice: Oil.createObject("CustomEnumeration")     # Image To Image / Text To Image
accelerationChoice: Oil.createObject("CustomEnumeration")  # None / TorchCompile / TensorRT
# ==========================================================================================

# --- Peuplement des menus (une seule fois, sinon ils restent vides dans le panneau) ---
if len(script.modelPreset.elements) == 0:
    for label in ("stabilityai/sd-turbo", "IDKiro/sdxs-512-0.9", "Custom..."):
        el = Oil.createObject("CustomEnumerationElement")
        el.label.set(label)
        el.value.set(0)
        script.modelPreset.elements.append(el)
    script.modelPreset.set("stabilityai/sd-turbo")

if len(script.modeChoice.elements) == 0:
    for label, value in (("Image To Image", 1), ("Text To Image", 2)):
        el = Oil.createObject("CustomEnumerationElement")
        el.label.set(label)
        el.value.set(value)
        script.modeChoice.elements.append(el)
    script.modeChoice.set("Image To Image")

if len(script.accelerationChoice.elements) == 0:
    for label, value in (("None", 0), ("TorchCompile", 1), ("TensorRT", 2)):
        el = Oil.createObject("CustomEnumerationElement")
        el.label.set(label)
        el.value.set(value)
        script.accelerationChoice.elements.append(el)
    script.accelerationChoice.set("None")

# CustomEnumeration.get() renvoie le label (string), pas la valeur -> mapping manuel
# (doit rester synchronise avec les .value peuples ci-dessus).
MODE_VALUES = {"Image To Image": 1, "Text To Image": 2}
ACCELERATION_VALUES = {"None": 0, "TorchCompile": 1, "TensorRT": 2}


def find_streamdiffusion_modifier(node, depth=0):
    """Cherche recursivement un modifier nomme "Stream Diffusion" dans les layers/generators.

    Recherche par nom plutot que par chemin fixe (layers[1].modifiers[...]) : l'index du
    modifier/layer peut changer si d'autres modifiers/layers sont ajoutes ou reordonnes.
    """
    if depth > 8:
        return None
    if hasattr(node, "modifiers"):
        for m in node.modifiers:
            try:
                if m.getFriendlyName() == "Stream Diffusion":
                    return m
            except Exception:
                pass
    if hasattr(node, "layers"):
        for child in node.layers:
            found = find_streamdiffusion_modifier(child, depth + 1)
            if found is not None:
                return found
            generator = getattr(child, "generator", None)
            if generator is not None and hasattr(generator, "layers"):
                found = find_streamdiffusion_modifier(generator, depth + 1)
                if found is not None:
                    return found
    return None


chosenModel = script.modelPreset.get()
if chosenModel == "Custom...":
    chosenModel = script.customModelName.get().strip()

target = find_streamdiffusion_modifier(script.project.masterScene)

if target is None:
    print("[ERREUR] Modifier 'Stream Diffusion' introuvable dans ce projet.")
elif not chosenModel:
    print("[ERREUR] Model Name vide - renseigne 'Custom Model Name' si tu as choisi Custom...")
else:
    inst = target.streamDiffusionInstance
    inst.modelName.set(chosenModel)
    inst.mode.set(MODE_VALUES[script.modeChoice.get()])
    inst.acceleration.set(ACCELERATION_VALUES[script.accelerationChoice.get()])
    print(
        f"[OK] modelName={inst.modelName.get()} "
        f"mode={inst.mode.toString()} "
        f"acceleration={inst.acceleration.toString()}"
    )
