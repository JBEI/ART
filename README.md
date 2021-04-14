# Automated Recommendation Tool (ART)

ART is a tool that leverages machine learning and probabilistic modeling techniques to guide metabolic engineering in a systematic fashion, without the need for a full mechanistic understanding of the biological system. Using sampling-based optimization, ART provides a set of recommended strains to be built in the next engineering cycle in order to achieve the given objective, alongside probabilistic predictions of their production levels.

Please note that this repository does not contain ART source code. For information on how to access the library see the [License](#license) section.

Please find more details about ART at the [ART website](https://sites.google.com/lbl.gov/art)



<!-- - [Documentation](#documentation) -->
- [System Requirements](#system-requirements)
- [Examples](#example)
- [Reference](#reference)
- [License](#license)

## System Requirements

### Hardware requirements
`ART` package requires only a standard computer with enough RAM to support the in-memory operations.

### Software requirements
#### OS Requirements
This package is supported for *macOS* and *Linux*. The package has been tested on the following systems:
+ macOS: Mojave (10.14.1), Catalina (10.15.1)
+ Linux: Debian 9

## Examples

An example is provided in the [`Limonene_Example.html`](https://htmlpreview.github.io/?https://github.com/JBEI/ART/blob/master/Limonene_Example.html) file.
Generating this output in a jupyter notebook should take ~5 mins on a MacBook Pro, CPU: 3.5GHz Intel Core i7, RAM: 16GB (2133MHz LPDDR3).

Additional tutorials, including real and simulated data sets, are provided in the [`notebooks`](https://github.com/JBEI/ART/tree/master/notebooks) directory.


## Reference

[Radivojević T., Costello Z., Workman K., Garcia Martin H., A machine learning Automated Recommendation Tool for synthetic biology, Nat Commun 11, 4879 (2020).](https://www.nature.com/articles/s41467-020-18008-4)


## License

ART code is distributed under the license specified in the [`Noncomercial_Academic_LA.pdf`](https://github.com/JBEI/ART/blob/master/Noncomercial_Academic_LA.pdf) file and is *Patent Pending*.

This license allows for free **non-commercial** use for **academic institutions**. Modification should be fed back to the original repository to benefit all users. If interested in an academic license of this type, please email tradivojevic@lbl.gov using the email address from your academic institution, and provide your github handle.  

A separate **commercial** use license is available from Berkeley Lab @ ipo@lbl.gov. The license terms (perpetual) are $10,000 for small businesses (less than 250 employees) and $25,000 for large businesses (more than 250 employees). Once the license is signed, interested parties will receive the information for accessing the private github repository containing the `ART` source code.

An **evaluation license** for commercial use can be obtained for 45 days of testing by filling the [`Evaluation_LA.pdf`](https://github.com/JBEI/ART/blob/master/Evaluation_LA.pdf) file and sending back to Jean Haemmerle, LBNL Licensing Analyst @ jhaemmerle@lbl.gov. Once the license is signed, interested parties will receive the information for accessing the private github repository containing the `ART` source code.

