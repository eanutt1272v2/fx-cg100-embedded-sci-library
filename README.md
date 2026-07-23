# fx-cg100-embedded-sci-library

An open-source MicroPython library for the Casio fx-CG100 calculator, and currently includes specialised scripts for fractal rendering and the plotting of hydrogenic orbital probability densities.

---

## Running Scripts

### On calculator (Casio fx-CG100)

**Requirements:**

- A **Casio fx-CG100** with MicroPython support and the latest official firmware installed.
- A **desktop computer** (either a laptop or PC).
- A standard **USB-C data-transfer cable** (avoid charging-only cables).


#### 1. One-time setup

1. If the calculator is not already on, do so by pressing the **[ON]** key. Check that your calculator's system firmware is up to date.
2. Connect the calculator to a **desktop computer** using a standard **USB-C data-transfer cable** (avoid charging-only cables).
3. When the **Select Connection Mode** dialogue box opens on the calculator screen, select the **[1] USB Flash** option and press the **[OK]** or **[EXE]** key to confirm.
4. Wait for the display to indicate **"Preparing USB"**. The calculator will then mount on your desktop environment as a generic USB external storage device. It should be visible in your preferred file browsing interface.

#### 2. Selecting a script

1. Every script in this repository is explicitly designed for the Casio fx-CG100. They are not guaranteed to function correctly on the Casio fx-CG50 or any other graphing calculcator.
2. Select your script by topic and expected runtime, and keep in mind that certain more advanced scripts may bring a longer runtime than others.
3. Note that larger-scale programs (such as the hydrogen atomic orbital visualiser `psi_fx.py`) require their companion dependency files (`psi_fx_lib.py`) to be transferred to the exact same folder to execute successfully.
4. When testing a script on-device for the first time, accept the default parameters by pressing the **[OK]** or **[EXE]** key on empty input prompts, and only increase complexity once the script produces any successful result.

#### 3. Transferring files

Copy the chosen `.py` script file (and its required `_lib.py` dependency file, if applicable) from this repository into the main root directory or a designated sub-directory located within the calculator's mounted storage memory.

#### 4. Execution

1. Safely eject the USB-C cable from your desktop computer to return the calculator to its normal operating system mode.
> [!CAUTION]
> **Never** pull the cable out without safely ejecting the drive volume first. Improper disconnection can corrupt the calculator's storage memory filesystem or cause unforseen consequences and may result in data loss.
2. Select the **Python** application from the calculator's main home icon grid either by arrow keys or the **[ALPHA] + [D]** shortcut and press the **[OK]** or **[EXE]** key to launch it.
3. Press the **[⋯] (TOOLS)** key to open the **Tools** menu, select **[2] File >**, and then **[2] Open** to navigate to the **Load** menu to browse directories within the calculator's storage memory for your preferred script.
4. Press the **[⟶|] (RIGHT TAB)** key to switch the active view from the **Editor** to the **Shell** tab, which will execute your script immediately. Alternatively, press the **[⋯] (TOOLS)** key to open the **Tools** menu, and select **[4] Run** to execute your script via the **Shell** tab.
5. Input chosen configuration values at the on-screen shell input prompts. The script will wait upon completion to keep the output pinned to your screen until you press the **[AC]** or **[⏎] (RETURN)** key to exit.

### On desktop (for development and/or testing)

**Requirements:**

- Installation of Python 3.13, a newer version, or the latest stable one.
- Installation of the `casioplot` stub python package (use `pip install casioplot`), which emulates the calculator's native graphics API.

Run any script directly from the repository root:

```bash
python3 fractals_chaos/mandelbrot_set.py
python3 phsyics/psi_fx.py
```

If working inside a virtual environment:

```bash
./your_env/bin/python fractals_chaos/barnsley_fern.py
```

---

## Licence

This repository is released under the [MIT Licence](LICENSE).

You are free to use, copy, modify, merge, publish, distribute, sublicense,
and sell copies of the scripts, provided the original copyright notice and
this licence notice are retained in all copies or substantial portions of the
software.

See the [LICENSE](LICENSE) file in the repository root for the complete licence text.
