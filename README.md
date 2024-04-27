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
