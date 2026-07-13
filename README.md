# Casio fx-CG100 MicroPython Scripts

An open-source library of standalone MicroPython scripts designed specifically for the Casio fx-CG100 calculator, covering mathematical visualisation, fractal rendering, number theory, physics simulation and modelling, utilities, and other topics of study.

---

## Quick Start

1. Connect your fx-CG100 calculator to a computer via USB and select **USB Flash** (storage mode).
2. Copy a `.py` script from this repository to the calculator volume.
3. Open the Python app on the calculator, navigate to the script, and run it.
4. Follow the on-screen prompts within the shell. Execution pauses smartly before exit so output stays visible to the user.

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

1. Verify the calculator firmware and Python app are installed and up to date.
2. Connect the calculator to a **computer** via appropriate USB data cable (mobile phones or tablets are highly advised against).
3. Select **USB Flash** (storage mode) so the calculator appears as a mounted volume.

#### 2. Selecting a script

- Every script in this repository targets the fx-CG100 and is self-contained.
- Select by topic and expected runtime. Fractal renderers and dense simulations
  carry significantly longer render times than algebraic or statistical scripts.
- When testing on-device for the first time, we recommend you accept the default
  parameters and increase complexity only once the script runs successfully.

#### 3. Transferring files

- Copy the chosen `.py` file from this repository to the calculator volume.
- Because scripts are standalone, only one file is typically required at a time.
- Keep a local backup of calculator storage before any large file transfer.

#### 4. Execution

1. Open the Python app on the calculator.
2. Navigate to the transferred script and run it.
3. Follow the on-screen input prompts.
4. The script will pause smartly before exiting so the output remains on screen for the user.

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
