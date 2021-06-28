# ML-GAN
This repository contains a modified version of the GAN presented in the paper [Which Training Methods for GANs do actually Converge?].
- configs for experiments can be found in /configs
- yaml filed can be modified for further experiments

# GAN stability
This repository contains the experiments in the supplementary material for the paper [Which Training Methods for GANs do actually Converge?](https://avg.is.tuebingen.mpg.de/publications/meschedericml2018).

To cite this work, please use
```
@INPROCEEDINGS{Mescheder2018ICML,
  author = {Lars Mescheder and Sebastian Nowozin and Andreas Geiger},
  title = {Which Training Methods for GANs do actually Converge?},
  booktitle = {International Conference on Machine Learning (ICML)},
  year = {2018}
}
```
You can find further details on [our project page](https://avg.is.tuebingen.mpg.de/research_projects/convergence-and-stability-of-gan-training).

# Usage
First download your data and put it into the `./data` folder.

To train a new model, first create a config script similar to the ones provided in the `./configs` folder.  You can then train you model using
```
python train.py PATH_TO_CONFIG
```

To compute the inception score for your model and generate samples, use
```
python test.py PATH_TO_CONFIG
```

Finally, you can create nice latent space interpolations using
```
python interpolate.py PATH_TO_CONFIG
```
or
```
python interpolate_class.py PATH_TO_CONFIG
```

