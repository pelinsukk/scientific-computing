# Scientific Computing — Simulation and Modelling 2

Personal study repository for Nikki Vercauteren’s University of Cologne lecture notes (9 July 2025, 61 pages). The supplied PDF stays outside this repository. This is an independent learning companion, not an official course release.

## Learning order

Start with the existing `01_Foundations` notebooks: state, functions, Taylor series. They are retained as prerequisite material. Then work through:

- [From a question to a verified model](02_Modelling/01_model_and_errors.ipynb) — §1, pp. 4–6
- [Dimensions, Buckingham groups and scaling](02_Modelling/02_dimensions_scaling.ipynb) — §2, pp. 7–14
- [Random motion, conservation and diffusion](03_Flow_Models/01_diffusion.ipynb) — §3.1–3.2, pp. 15–18
- [Advection–diffusion, Peclet number and Fourier modes](03_Flow_Models/02_transport_fourier.ipynb) — §3.3, pp. 18–21
- [Initial-value problems and one-step convergence](04_Time_Integration/01_one_step_convergence.ipynb) — §4.1–4.3, pp. 22–26
- [Implicit methods, absolute stability and stiffness](04_Time_Integration/02_stability_stiffness.ipynb) — §4.2 and §4.4.1, pp. 24, 27–30
- [Hamiltonian dynamics and geometric integration](04_Time_Integration/03_hamiltonian.ipynb) — §4.4.2, pp. 30–36
- [Finite differences and spatial truncation error](05_Finite_Differences/01_derivatives.ipynb) — §5.1–5.2, pp. 37–41
- [Diffusion: direct and von Neumann stability](05_Finite_Differences/02_diffusion_stability.ipynb) — §5.3.1–5.3.3, pp. 42–45
- [Upwinding, CFL, dissipation and dispersion](05_Finite_Differences/03_advection.ipynb) — §5.3.4, pp. 45–48
- [Implicit advection–diffusion verification](05_Finite_Differences/04_combined_transport.ipynb) — §5.3.5, p. 48
- [Weak form, Ritz–Galerkin and finite elements](06_Finite_Elements/01_weak_form_assembly.ipynb) — §5.4, pp. 49–58
- [Characteristic curves for linear transport](07_Characteristics/01_linear_transport.ipynb) — §6.1, pp. 59–60
- [Burgers equation and the first crossing](07_Characteristics/02_burgers_extension.ipynb) — §6.2, p. 60 — supplementary material; the supplied notes contain only the heading

## Working through each notebook
Read the model → predict the outcome → run the experiment → inspect the labelled plots and checks → answer the exercise in your own words. Completing a generated notebook is not evidence that you have learned it. Keep exercise answers and personal conclusions in your own commits.

## Setup
Use Python 3.11 or newer. From the repository directory:
```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m jupyterlab
```
Select the environment's Python kernel. All new examples use generated data and run offline after installation. Dense matrices are deliberately small teaching examples.

## Verification
New notebooks include analytical comparisons, conservation checks or convergence experiments. The run report records actual execution; requirements specify compatible ranges rather than an exact environment lock. Existing foundation notebooks are not represented as newly authored course material.

## Git workflow
Use one branch for a coherent learning unit. Commit explanations and working examples together; commit verified outputs after checks. Open a pull request stating the mathematical question, changes, observed results and limits. Merge only after review. Do not create one branch per cell. The initial course series is prepared on `course/simmod2-vercauteren`.

## AI workflow
1. Ask the agent to derive the model, assumptions and a known reference solution before coding.
2. Ask for one small experiment with explicit initial/boundary conditions, units and expected behaviour.
3. Run it and inspect errors, conservation and refinement; ask the agent to explain discrepancies.
4. Review the diff and record what you independently verified. Never describe unexecuted code as tested.

## Source caveats
The source preface explicitly disclaims completeness and accuracy. Equation 2.23 must have sin(t*) after t*=omega*t. Explicit Euler's stability boundary allows bounded oscillation, not strict asymptotic decay. Burgers §6.2 is only a heading in the supplied PDF; the final notebook is labelled supplementary. The companion gives practical experiments and key derivations, not a replacement for all lecture proofs or class attendance.
