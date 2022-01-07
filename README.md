# Tree Cluster States
For more information on quantum tree cluster states, refer to:
* [Phys. Rev. Lett. 125, 223601](https://doi.org/10.1103/PhysRevLett.125.223601)
* [Phys. Rev. X 10, 021071](https://doi.org/10.1103/PhysRevX.10.021071)

## How to generate the animation?
Make sure you install [`python`](https://python.org) and [`manim` (Community edition)](https://docs.manim.community/). You also should have a `LaTeX` distribution installed. I recommend using [`texlive`](https://www.tug.org/texlive/) as it is easy to install on Windows. Then, run the following command from your terminal with the `tree_cluster_state.py` file in your current directory:
```python
manim -qh tree_cluster_states.py TreeClusterStates
```
The resulting animation would then look like:

<img src="https://github.com/bernwo/tree-cluster-states-manim/blob/main/assets/TreeClusterStates.gif" height="300">
