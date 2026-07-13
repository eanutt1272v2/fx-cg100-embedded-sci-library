# Casio fx-CG100 MicroPython Scripts

An open-source library of standalone MicroPython scripts designed specifically for the Casio fx-CG100 calculator, covering mathematical visualisation, fractal rendering, number theory, physics simulation and modelling, utilities, and other topics of study.

---

## Quick Start

1. Turn on the fx-CG100, connect it to a **desktop computer** via a standard USB-C data cable, and select **[USB Flash]** using the **[OK / EXE]** key when prompted.
2. Open the mounted volume on your computer and copy the desired `.py` script from this repository directly into the storage root or a subfolder.
3. Disconnect the cable safely, open the **Python** app from the calculator's main menu, and navigate to your script using the onboard file browser.
4. Press **[Run]** (or **[EXE]**) and follow the on-screen prompts within the shell. Execution automatically pauses before exit to keep your output visible.

For full setup instructions and desktop testing, see [Running Scripts](#running-scripts).

---

## Repository Structure

| Folder                    | Scripts | Theme                                         | Example scripts                                               |
| ------------------------- | ------: | --------------------------------------------- | ------------------------------------------------------------- |
| `fractals_chaos/`         |       8 | Fractals and chaotic systems                  | `mandelbrot_set.py`, `julia_set.py`, `burning_ship.py`        |
| `number_theory/`          |       9 | Primes, modular arithmetic, integer functions | `prime_sieve_eratosthenes.py`                                  |
| `geometry_visual/`        |       8 | Geometry calculators and curve visualisation  | `shapes.py`, `triangle_trig_solver.py`, `lissajous_curves.py` |
| `calculus_numerical/`     |       5 | Calculus and numerical methods                | `newton_raphson.py`, `numerical_integration.py`               |
| `physics/`                |       7 | Classical physics models                      | `projectile_motion.py`, `simple_harmonic_motion.py`, `psi_pico.py` |
| `probability_statistics/` |       4 | Random processes and distributions            | `dice_roll_distribution.py`, `monte_carlo_pi.py`              |
| `cellular_automata/`      |       3 | Cellular and agent automata                   | `conway_gol.py`, `langton_ant.py`                             |
| `sequences_series/`      |       3 | Integer sequences and series                  | `collatz_sequence.py`, `fibonacci_golden_ratio.py`            |
| `signal_processing/`      |       1 | Fourier synthesis                             | `fourier_synth.py`                                            |
| `algorithms_visual/`      |       1 | Algorithm visualisation                       | `sorting_visual.py`                                           |

---

## Running Scripts

### On-calculator (fx-CG100)

**Requirements:**

- A Casio fx-CG100 with MicroPython support and the latest official OS installed.

#### 1. One-time setup

1. Power on the calculator and verify that the firmware and Python application are up to date.
2. Connect the calculator to a **desktop computer** using a standard USB-C data-transfer cable (avoid charging-only cables).
3. When the **Select Connection Mode** dialogue box automatically populates on the calculator screen, highlight **[USB Flash]** and press the **[OK / EXE]** key.
4. Wait for the screen to display **"Preparing USB"**; the calculator will soon mount directly on your desktop as an external storage drive.

#### 2. Selecting a script

- Every core application in this repository targets the fx-CG100.
- Select by topic and expected runtime. Heavy mathematical visualizers (like fractal renderers or orbital simulation paths) carry significantly longer computation loops than algebraic scripts.
- Note that advanced scripts (such as the quantum orbital visualizer `psi_pico.py`) require their companion dependency files (`psi_pico_lib.py`) to be transferred to the same folder to execute successfully.
- When testing on-device for the first time, accept the default parameters by pressing **[EXE]** on empty prompts, and increase complexity only once the base script runs successfully.

#### 3. Transferring files

- Copy the chosen `.py` file (and its required `_lib.py` backend file, if applicable) from this repository into the main root storage directory or designated folders of the mounted calculator drive volume.
- Keep a local backup of your calculator's storage files before performing any major bulk file transfers.

#### 4. Execution

1. Safely eject the USB-C cable from your computer to return the calculator to its native operating system mode.
2. Select the **Python** app icon from the calculator's main home icon grid and press **[EXE]**.
3. Use the arrow pad to navigate to the transferred script from the on-screen directory list.
4. Press the **[F6]** function key (**RUN**) or the **[EXE]** key to boot the script engine.
5. Provide your values at the on-screen shell input prompts. The environment will pause upon completion to keep the generated result pinned to your screen.

#### 5. Troubleshooting

| Symptom                | Likely cause                                      | Resolution                                                                       |
| ---------------------- | ------------------------------------------------- | -------------------------------------------------------------------------------- |
| `Module not found`     | Script imports a desktop-only package             | Choose a `casioplot`-based script instead                                        |
| `AttributeError` or crash when executing a script using `matplotlib.pyplot` | The script is attempting to call desktop-exclusive functions like `bar()`, `grid()`, or `text()` which do not exist within Casio's embedded OEM subset | Rewrite the graph logic to map coordinates using only the calculator-supported primitives: `plot()`, `axis()`, and `show()` |
| Slow render or timeout | Parameter values too large for on-device hardware | Reduce grid size, iteration count, or step resolution — or simply wait patiently |
| Input or value error   | Value outside the range expected by the script    | Re-run and supply values within the ranges shown by shell prompts                |

### On desktop (for testing)

**Requirements:** Python 3.13 or later and the `casioplot` stub package, which emulates the calculator's native graphics API.

Run any script directly from the repository root:

```bash
python3 fractals_chaos/mandelbrot_set.py
python3 geometry_visual/complex_visualiser.py
python3 number_theory/prime_sieve_eratosthenes.py
```

If working inside a virtual environment:

```bash
./casio_env/bin/python geometry_visual/shapes_lib.py
```

---

## Licence

This repository is released under the [MIT Licence](LICENSE).

You are free to use, copy, modify, merge, publish, distribute, sublicense,
and sell copies of the scripts, provided the original copyright notice and
this licence notice are retained in all copies or substantial portions of the
software.

See the [LICENSE](LICENSE) file in the repository root for the complete licence text.
