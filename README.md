

<div align="center">

# Configurable SampleCNN
</div>

A configurable version of the SampleCNN model in ["Sample-level Deep Convolutional Neural Networks for Music Auto-tagging Using Raw Waveforms"](https://arxiv.org/abs/1703.01789), implemented in PyTorch. The SampleCNN class in this repository implements the music encoder part of the SampleCNN model—it excludes the last couple layers of the original model, which are meant for music tagging.



## Project Structure

```
sampleCNN-configurable/
├── model/                      # model directory
│   ├── sample_cnn.py           # model class
├── scripts/                    # scripts directory
│   ├── model_summary.py        # script to create model summary
│   ├── model_tests.py          # script to test model class
```


## Required Packages

* pytorch
* numpy
* torchinfo


## References

* ["Sample-level Deep Convolutional Neural Networks for Music Auto-tagging Using Raw Waveforms"](https://arxiv.org/abs/1703.01789)
* [github.com/kyungyunlee/sampleCNN-pytorch](https://github.com/kyungyunlee/sampleCNN-pytorch)
* [github.com/jongpillee/sampleCNN](https://github.com/jongpillee/sampleCNN)
* [github.com/tae-jun/sample-cnn](https://github.com/tae-jun/sample-cnn)

