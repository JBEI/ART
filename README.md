# Automated Recommendation Tool (ART)

ART is a tool that leverages machine learning and probabilistic modeling techniques to guide metabolic engineering in a systematic fashion, without the need for a full mechanistic understanding of the biological system. Using sampling-based optimization, ART provides a set of recommended strains to be built in the next engineering cycle in order to achieve the given objective, alongside probabilistic predictions of their production levels.

Please note that this repository does not contain ART source code. For information on how to access the library see the [License](#license) section.

Please find more details about ART at the [ART website](https://sites.google.com/lbl.gov/art).



<!-- - [Documentation](#documentation) -->
- [System Requirements](#system-requirements)
- [Examples](#example)
- [Reference](#reference)
- [License](#license)

## System Requirements

### Hardware requirements

The `ART` package requires only a standard computer with enough RAM to support the in-memory
operations. While slimmer installs may be possible, at the time of writing, ART developers
typically dedicate 8GB RAM and 80GB of disk to the Docker Desktop instance used to develop and
test the code on MacOS.

ART requires a minimum of 2 physical processor cores to run Markov Chain Monte Carlo (MCMC)
sampling. For more complex problems, ART's results will improve on systems with many processor
cores to dedicate to MCMC sampling (see the `max_mcmc_cores` parameter).

### Software requirements

#### OS Requirements

The ART Docker image will run on any OS that Docker supports (e.g. macOS, Linux, Windows).

Direct install of ART into your system Python is not the recommended or supported
workflow. Please use the included Docker image for reproducible builds, and as a reference for any
direct installs you attempt on your own. While there are valid reasons to use ART externally to
the included Docker image, unfortunately the ART team is not resourced to support
non-Docker workflows.

In the past, direct installs of ART had been tested on _macOS_ and _Linux_:

-   macOS: Mojave (10.14.1), Catalina (10.15.1)
-   Linux: Debian 9 & 10

#### Docker

Docker is the preferred / supported environment for running ART. Docker creates reproducible
runs in a tested runtime environment. Docker also avoids the installation headaches and potential
pitfalls of directly installing ART into your system Python.

## Examples

An example is provided in the [`Limonene_Example.html`](https://htmlpreview.github.io/?https://github.com/JBEI/ART/blob/master/Limonene_Example.html) file.
Generating this output in a jupyter notebook should take ~5 mins on a MacBook Pro, CPU: 3.5GHz Intel Core i7, RAM: 16GB (2133MHz LPDDR3).

Additional tutorials, including real and simulated data sets, are provided in the [`notebooks`](https://github.com/JBEI/ART/tree/master/notebooks) directory.


## Reference

[Radivojević T., Costello Z., Workman K., Garcia Martin H., A machine learning Automated Recommendation Tool for synthetic biology, Nat Commun 11, 4879 (2020).](https://www.nature.com/articles/s41467-020-18008-4)


## License

ART code is distributed under the license specified in the [`Noncomercial_Academic_LA.pdf`](https://github.com/JBEI/ART/blob/master/Noncomercial_Academic_LA.pdf) file and is *Patent Pending*.

This license allows for free **non-commercial** use for **academic institutions**. Modification should be fed back to the original repository to benefit all users. If interested in an academic license of this type, please email azournas@lbl.gov using the email address from your academic institution, and provide your github handle. You will then be added to the private github repository containing the `ART` source code.

A separate **commercial** use license is available from Berkeley Lab @ ipo@lbl.gov. The license terms (10 years) are $10,000 for small businesses (less than 250 employees) and $25,000 for large businesses (more than 250 employees). Once the license is signed, interested parties will receive the information for accessing the private github repository containing the `ART` source code.

An **evaluation license** for commercial users can be obtained for 90 days of testing by filling the [`Evaluation_LA.pdf`](https://github.com/JBEI/ART/blob/master/Evaluation_LA.pdf) file and sending back to Jean Haemmerle, LBNL Licensing Associate @ jhaemmerle@lbl.gov. Once the license is signed, interested parties will receive the information for accessing the private github repository containing the `ART` source code.

