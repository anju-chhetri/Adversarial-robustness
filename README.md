# Adversarial-robustness

## Abstract

Text-guided diffusion models, particularly latent diffusion models (LDMs), pose a privacy
threat due to their ability to generate highly realistic images conditioned on text prompts.
This raises concerns about malicious image editing. Existing methods leverage adversarial
perturbations to hinder realistic image generation by LDMs, but these methods lack robust-
ness to JPEG compression, a common image compression algorithm. This work proposes
an approach for generating adversarial perturbations that are robust to JPEG compression.
We demonstrate the effectiveness of our method and explore how text prompts influence the
success of adversarial attacks against text-guided diffusion models.

# Proposed Architecture
![](https://github.com/anju-chhetri/Adversarial-robustness/blob/master/Images/prompt-impact.png)

To make adversarial images robust to JPEG compression we combine encoder/diffusion attack with
differentiable JPEG. The input image is first compressed using a differentiable JPEG algorithm. The compressed representation is then fed into the LDM to learn perturbations robust to JPEG compression. By using an ensemble of models running on different QFs, we obtain gradients that capture the effects of compression across a wide range (QFs 25-100).

During the generation of adversarial images, we can provide different types of text prompts to the network. Fusion of text and image information occurs through cross-attention layers, and the generated cross-attention maps influence the spatial layout of the generated image. To investigate the influence of the text prompt on the generated image, we categorize the prompts into four types:

| Prompt Type      | Description |
| ----------- | ----------- |
| Content Prompt      | Provides a description of the image content       |
| Irrelevant prompt    | Text unrelated to the image content.        |
| Random token prompt      | Sequence of tokens randomly sampled from a uniform distribution.       |
| Null prompt   | No text prompt is provided.        |

# Results

![](https://github.com/anju-chhetri/Adversarial-robustness/blob/master/Images/ensemble-diffusion%20.png)
Results for JPEG-resilient diffusion attack.
