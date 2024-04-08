# Homework3

Name:

Student ID: 

This assignment is due on **Wednesday, January 03 2024** at 23:59 PM CST.

## Instructions

- [Goals](#goals)
- [Setup](#setup)
- [Q1: Style Transfer (15 points)](#q1-style-transfer-15-points)
- [Q2: Generative Adversarial Networks (15 points)](#q2-generative-adversarial-networks-15-points)
- [Submitting your work](#submitting-your-work)

### Goals

In this assignment, you will implement Style Transfer. Then, you will train a Generative Adversarial Network to generate images that look like a training dataset!

The goals of this assignment are as follows:

- Understand and implement techniques for image style transfer.
- Understand how to train and implement a Generative Adversarial Network (GAN) to produce images that resemble samples from a dataset.

### Setup

You should be able to use your setup from assignments 2.

**Ensure you have followed the [setup instructions](https://cs231n.github.io/setup-instructions/) before proceeding.**

**Install Packages**. Once you have the starter code, activate your environment and run `pip install -r requirements.txt`.

**Download data**. Next, you will need to download the COCO captioning data, a pretrained SqueezeNet model (for TensorFlow), and a few ImageNet validation images. Run the following from the `assignment3` directory:

```bash
cd cs231n/datasets
./get_datasets.sh
```

**Start Jupyter Server**. After you've downloaded the data, you can start the Jupyter server from the `assignment3` directory by executing `jupyter notebook` in your terminal.

Complete each notebook, then once you are done, go to the [submission instructions](#submitting-your-work).

### Q1: Style Transfer (15 points)

In the notebooks `StyleTransfer-PyTorch` you will learn how to create images with the content of one image but the style of another. 

### Q2: Generative Adversarial Networks (15 points)

In the notebooks `Generative_Adversarial_Networks_PyTorch.ipynb` you will learn how to generate images that match a training dataset, and use these models to improve classifier performance when training on a large amount of unlabeled data and a small amount of labeled data.

### Submitting your work

**Important**. Please make sure that the submitted notebooks have been run and the cell outputs are visible.

Once you have completed all notebooks and filled out the necessary code, there are **_two_** steps you must follow to submit your assignment:

**1.** You must have (a) `nbconvert` installed with Pandoc and Tex support and (b) `PyPDF2` installed to successfully convert your notebooks to a PDF file. Please follow these [installation instructions](https://nbconvert.readthedocs.io/en/latest/install.html#installing-nbconvert) to install (a) and run `pip install PyPDF2` to install (b). If you are, for some inexplicable reason, unable to successfully install the above dependencies, you can manually convert each jupyter notebook to HTML (`File -> Download as -> HTML (.html)`), save the HTML page as a PDF.

**2.** Submit the zip file and PDF to [Gradescope](https://www.gradescope.com/): The zip file for code `style_transfer_pytorch.py` and `gan_pytorch.py` to Assignment 3 Source-Code; PDFs for notebooks `StyleTransfer-PyTorch.ipynb` and `Generative_Adversarial_Networks_PyTorch.ipynb` to Assignment 3.
