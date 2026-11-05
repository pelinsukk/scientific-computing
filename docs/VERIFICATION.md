# Verification report

[Course index](../README.md) · [Figure gallery](FIGURES.md)

Verified on 5 November 2026 with Python 3.13.1, NumPy 2.4.6, Matplotlib 3.11.2, nbformat 5.11.1, nbclient 0.11.0 and ipykernel 7.4.0.

All **21 notebooks** ran in fresh kernels; all numerical assertions passed. The legacy Turkish state illustration was rerun after replacing its machine-specific output path and adjusting the label position. This report records the final successful run for each notebook.

**17 figures** were generated and visually checked. Notebook format and local Markdown links were also checked.

## Selected results

| Experiment | Measured result |
|---|---|
| Trapezoidal quadrature | Refinement orders 2.003, 2.001, 2.000, 2.000 |
| ODE convergence | Forward Euler 1.010; backward Euler 0.991; Heun 2.017; trapezoidal 2.000; RK4 4.019 |
| Periodic diffusion | Coupled time/space refinement order 2.002 |
| Linear FEM | L2 refinement order 2.000 |
| Tracer capstone | RMS error fell from 0.01938 to 0.003352; max mass drift over all four runs below 1.4e-14 |

## Notebook execution

| Notebook | Result |
|---|---|
| [01_Foundations/01_state.ipynb](../01_Foundations/01_state.ipynb) | PASS |
| [01_Foundations/02_mathematical_functions.ipynb](../01_Foundations/02_mathematical_functions.ipynb) | PASS |
| [01_Foundations/03_taylor_series.ipynb](../01_Foundations/03_taylor_series.ipynb) | PASS |
| [01_Foundations/04_derivatives.ipynb](../01_Foundations/04_derivatives.ipynb) | PASS |
| [02_Dimensional_Analysis/01_workflow.ipynb](../02_Dimensional_Analysis/01_workflow.ipynb) | PASS |
| [02_Dimensional_Analysis/02_dimensions_and_scaling.ipynb](../02_Dimensional_Analysis/02_dimensions_and_scaling.ipynb) | PASS |
| [03_Flow_Modelling/01_diffusion.ipynb](../03_Flow_Modelling/01_diffusion.ipynb) | PASS |
| [03_Flow_Modelling/02_fourier.ipynb](../03_Flow_Modelling/02_fourier.ipynb) | PASS |
| [04_Time_Integration/01_one_step.ipynb](../04_Time_Integration/01_one_step.ipynb) | PASS |
| [04_Time_Integration/02_stability.ipynb](../04_Time_Integration/02_stability.ipynb) | PASS |
| [04_Time_Integration/03_hamiltonian.ipynb](../04_Time_Integration/03_hamiltonian.ipynb) | PASS |
| [04_Time_Integration/ode.linear.decay-growth.systems.ipynb](../04_Time_Integration/ode.linear.decay-growth.systems.ipynb) | PASS |
| [05_Numerical_Errors/01_error_budget.ipynb](../05_Numerical_Errors/01_error_budget.ipynb) | PASS |
| [06_Space_Discretization/01_diffusion_grid.ipynb](../06_Space_Discretization/01_diffusion_grid.ipynb) | PASS |
| [06_Space_Discretization/02_advection_diffusion.ipynb](../06_Space_Discretization/02_advection_diffusion.ipynb) | PASS |
| [07_Stability/01_advection_dispersion.ipynb](../07_Stability/01_advection_dispersion.ipynb) | PASS |
| [08_Finite_Element_Method/01_weak_form.ipynb](../08_Finite_Element_Method/01_weak_form.ipynb) | PASS |
| [09_Exercises/01_exercise.ipynb](../09_Exercises/01_exercise.ipynb) | PASS |
| [09_Exercises/02_tracer_project.ipynb](../09_Exercises/02_tracer_project.ipynb) | PASS |
| [10_Characteristics/01_characteristics.ipynb](../10_Characteristics/01_characteristics.ipynb) | PASS |
| [10_Characteristics/02_burgers.ipynb](../10_Characteristics/02_burgers.ipynb) | PASS |

These are numerical verification cases for the stated models and grids, not validation against field observations.

## Final publication check

After consolidation, all 21 notebooks ran again in fresh kernels, including the seven additional experiments. All assertions passed. The 17 standalone PNGs were reproduced byte for byte, and all 157 local links in that revision resolved. The seven notebooks with added experiments were then rerun to save their additional inline outputs for GitHub; the original cell sources and existing outputs were preserved.
