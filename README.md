# Automated Recommendation Tool (ART)

ART is a tool that leverages machine learning and probabilistic modeling techniques to guide metabolic engineering in a systematic fashion, without the need for a full mechanistic understanding of the biological system. Using sampling-based optimization, ART provides a set of recommended strains to be built in the next engineering cycle in order to achieve the given objective, alongside probabilistic predictions of their production levels.

<!-- - [Documentation](#documentation) -->
- [System Requirements](#system-requirements)
- [Example](#example)
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

## Example

An example is provided in the `Limonene_Example.html` file.
Generating this output in a jupyter notebook should take ~5 mins on a MacBook Pro, CPU: 3.5GHz Intel Core i7, RAM: 16GB (2133MHz LPDDR3).


## Reference

Radivojević T., Costello Z., Workman K., Garcia Martin H., ART: A machine learning Automated Recommendation Tool for synthetic biology, [arXiv:1911.11091](https://arxiv.org/abs/1911.11091)


## License

This code is distributed under the license specified in the `License.pdf` file and is *Patent Pending*.

This license allows for free **non-commercial** use for **academic institutions**. Modification should be fed back to the original repository to benefit all users.

A separate **commercial** use license is available from Berkeley Lab @ ipo@lbl.gov. The license terms are $10,000 for small businesses (less than 250 employees) and $25,000 for large businesses (more than 250 employees). An **evaluation license** for commercial use can be obtained for 45 days of testing.

Once the license is signed via DocuSign, interested parties will receive the information for accessing the private github repository containing the `ART` source code.

