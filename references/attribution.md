# Attribution and license boundaries

## Original research inspiration

This independently authored skill draws methodological inspiration from
[Video2GUI](https://github.com/WeiminXiong/Video2GUI), by Weimin Xiong,
Shuhao Gu, Bowen Ye, Zihao Yue, Lei Li, Feifan Song, Sujian Li, and Hao Tian:

> Video2GUI: Synthesizing Large-Scale Interaction Trajectories for Generalized
> GUI Agent Pretraining (ICML 2026).

[Paper](https://arxiv.org/abs/2605.14747) ·
[Original repository](https://github.com/WeiminXiong/Video2GUI) ·
[Original license](https://github.com/WeiminXiong/Video2GUI/blob/main/LICENSE)

Related ideas include chronological short windows, compact historical context,
coarse-to-fine visual analysis, and before/during/after screenshot triplets.
The research project's focus is GUI trajectories for agent pretraining; this
skill's output is a reproducible tutorial with continuity and artifact checks.
Do not attribute this skill's runtime or packaging rules to the paper.

This is not an official Video2GUI release, affiliation, fork, or claim to have
implemented or reproduced that research system. This repository does not bundle
its source code, website assets, datasets, model weights, or benchmark results.
The original project retains its own Apache-2.0 license. MIT here applies to our
own skill instructions and tests, not to third-party materials. If future
contributions import third-party material, preserve its original notices and
license terms; adding a credit alone does not relicense copied material.

```bibtex
@inproceedings{xiong2026video2gui,
  title     = {Video2GUI: Synthesizing Large-Scale Interaction Trajectories for Generalized GUI Agent Pretraining},
  author    = {Xiong, Weimin and Gu, Shuhao and Ye, Bowen and Yue, Zihao and Li, Lei and Song, Feifan and Li, Sujian and Tian, Hao},
  booktitle = {International Conference on Machine Learning (ICML)},
  year      = {2026},
  url       = {https://arxiv.org/abs/2605.14747}
}
```

## Tutorials and project assets

A video's public availability is not permission to redistribute the video,
screenshots, instructor code, or bundled assets. Verify source permissions and
licenses before sharing a reconstructed article or downloadable project. This
repository ships the method, not tutorial footage or third-party project files.

## Skill license

The notice below is included in the installable reference bundle so a native
Hermes installation retains the skill's license even without repository-root
files:

```text
MIT License

Copyright (c) 2026 Warlock Su

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
