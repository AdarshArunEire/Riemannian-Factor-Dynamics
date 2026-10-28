# Parent implementation

The synthetic comparison runs the parent Riemannian factor model from its
authors' R code, which is not redistributed here. Clone it into this folder at
the commit the results were produced with:

```bash
git clone https://github.com/shuochieh/Riemannian_factor_model.git reference/Riemannian_factor_model-main
git -C reference/Riemannian_factor_model-main checkout c07d49c257d489e00b7e15bdd432954946a2a694
```

`experiments/parent_rfm_bw_worker.R` sources `BWS_util.R` from that clone
unchanged.

Paper: S.-C. Huang, R. Chen and Y. Chen, "A Riemannian Factor Model for
Manifold-Valued Time Series", [arXiv:2607.28385](https://arxiv.org/abs/2607.28385).
