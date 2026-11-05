# Source coverage and attribution

[Course index](../README.md)

The primary sources are Nikki Vercauteren, *Simulation and Modelling 2 – Lecture Notes*, M.Sc. Computational Sciences, University of Cologne, summer semester 2025 (9 July 2025, 61 pages; supplied as `CompSci_Vercauteren.pdf`), and *SIMMOD2: Simulation and Modelling 2 — Introduction*, summer semester 2026 (19 slides; supplied as `SIMMOD2_Introduction.pdf`). Page numbers refer to the supplied PDFs. The sources are credited here and are not redistributed. The repository contains original study material and original plots; the repository licence does not grant rights to the lecture files.

| Lecture sections | Pages | Companion |
|---|---:|---|
| Preface and contents | 1–3 | [Course index and scope](../README.md) |
| §§1.1–1.3: formulation, choice of method, scientific goals and errors | 4–6 | [Model workflow](../02_Dimensional_Analysis/01_workflow.ipynb) |
| §§2–2.3: pendulum, dimensional matrix and Pi groups, driven oscillator, scaling | 7–14 | [Dimensions and scaling](../02_Dimensional_Analysis/02_dimensions_and_scaling.ipynb) |
| §§3.1–3.2.1: random walks, flux, conservation, Gaussian similarity | 15–18 | [Diffusion](../03_Flow_Modelling/01_diffusion.ipynb) |
| §§3.3–3.3.2: advection–diffusion, Pe, Fourier modes | 18–21 | [Fourier transport](../03_Flow_Modelling/02_fourier.ipynb) |
| §§4.1–4.3: IVPs, one-step schemes, implicit iteration, consistency and convergence | 22–27 | [One-step methods](../04_Time_Integration/01_one_step.ipynb), [error budget](../05_Numerical_Errors/01_error_budget.ipynb) |
| §4.4.1: absolute, A- and L-stability, stiff systems | 27–30 | [Stiffness](../04_Time_Integration/02_stability.ipynb) |
| §4.4.2: Hamiltonian flow, phase volume, symplectic splitting | 30–36 | [Hamiltonian integration](../04_Time_Integration/03_hamiltonian.ipynb) |
| §§5.1–5.2.1: method of lines, stencils, matrix forms and truncation | 37–42 | [Grid diffusion](../06_Space_Discretization/01_diffusion_grid.ipynb), [error budget](../05_Numerical_Errors/01_error_budget.ipynb) |
| §§5.3.1–5.3.3: matrix and Fourier stability, explicit diffusion bound | 42–45 | [Grid diffusion](../06_Space_Discretization/01_diffusion_grid.ipynb) |
| §5.3.4: advection CFL, phase and amplitude | 45–48 | [Advection stability](../07_Stability/01_advection_dispersion.ipynb) |
| §5.3.5: advection–diffusion stability | 48 | [Tracer method comparison](../06_Space_Discretization/02_advection_diffusion.ipynb) |
| §§5.4–5.4.4: weak form, Ritz–Galerkin, hats, assembly | 49–58 | [Finite element method](../08_Finite_Element_Method/01_weak_form.ipynb) |
| §6.1: constant and variable characteristic velocity | 59–61 | [Characteristics](../10_Characteristics/01_characteristics.ipynb) |
| §6.2: Burgers heading, no exposition | 60–61 | [Supplementary Burgers lesson](../10_Characteristics/02_burgers.ipynb) |
| References | 61 | Original reference list remains in the supplied notes |

| Introductory slides | Slides | Companion |
|---|---:|---|
| Context, simulation motivation and examples | 1–7 | [Course index](../README.md), [model workflow](../02_Dimensional_Analysis/01_workflow.ipynb) |
| Course logistics | 8 | Refer to the original slides and the official course platform for scheduling |
| Project workflow | 9 | [Tracer capstone](../09_Exercises/02_tracer_project.ipynb) |
| Modelling stages, method selection, implementation, error sources | 10–18 | [Model workflow](../02_Dimensional_Analysis/01_workflow.ipynb) |
| Overview of course methods | 19 | [Learning path](../README.md#learning-path) and lecture crosswalk above |

## Notation and corrections

- The scaled oscillator forcing in Eq. (2.23) is `sin(t*)`: the definition `t* = ωt` already incorporates the frequency.
- The Gaussian profile in Eq. (3.24) needs a **negative** exponent, consistent with Eq. (3.25), decay at infinity, and integrability.
- The dimension count uses the rank of the actual dimensional matrix. A dimensionless initial angle can still affect a pendulum period.
- The Fourier coefficient modulus is the amplitude and its argument is the phase. The real and imaginary parts are not individually amplitude and phase.
- For `y' = λy` with `λ < 0`, forward Euler **decays** for `0 < h < 2/|λ|`; at equality it alternates without decay.
- The periodic mesh uses distinct nodes without a duplicated endpoint. The `j-1` and `j+1` neighbours wrap around.
- The implicit upwind matrix is `I - hA` with `A = -u D_up + D D_2`; this sign gives the positive real contribution to the amplification denominator.
- The linear-oscillator plots distinguish exact energy preservation (midpoint for this quadratic example) from bounded energy error (symplectic Euler and Verlet at the tested step).

Throughout, `h` is a time step in ODE/PDE time integration and an element size in FEM; `Δx` denotes finite-difference spacing, `ν` the Courant number and `r` the diffusion ratio. Each notebook states its own notation and assumptions.
