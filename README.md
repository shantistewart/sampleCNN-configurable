

<div align="center">

# Configurable SampleCNN
</div>

A configurable version of the SampleCNN model ("Sample-level Deep Convolutional Neural Networks for Music Auto-tagging Using Raw Waveforms"), implemented in PyTorch. The SampleCNN class in this repository implements the music encoder part of the SampleCNN model—it excludes the last couple layers of the original SampleCNN model, which are meant for music tagging.



## Project Structure

```
sampleCNN-configurable/
├── model/                      # model directory
│   ├── sample_cnn.py           # model class
├── scripts/                    # scripts directory
│   ├── model_summary.py        # script to create model summary
│   ├── model_tests.py          # script to test model class
```

