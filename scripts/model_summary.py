"""Script to create model summary of SampleCNN encoder."""


import os
from torchinfo import summary
from model.sample_cnn import SampleCNN


# model summaries directory and file name (summary file path = /summaries_dir/summary_file_name):
summaries_dir = "model_summaries"
summary_file_name = "sample_cnn_summary.txt"

# model architecture hyperparameters:
n_blocks = 9
n_channels = [128, 128, 256, 256, 256, 256, 256, 256, 512]
output_size = 512
conv_kernel_size = 3
pool_size = 3
activation = "relu"
first_block_params = {
    "out_channels": 128,
    "conv_size": 3
}
input_size = 59049

# model summary options:
batch_size = 1
summary_depth = 3
summary_info = ["input_size", "output_size", "num_params"]


if __name__ == "__main__":
    print("\n")

    # create SampleCNN:
    model = SampleCNN(
        n_blocks=n_blocks,
        n_channels=n_channels,
        output_size=output_size,
        conv_kernel_size=conv_kernel_size,
        pool_size=pool_size,
        activation=activation,
        first_block_params=first_block_params,
        input_size=input_size,
    )

    # create model summary:
    model_summary = str(summary(
        model,
        input_size=(batch_size, 1, input_size),
        col_names=summary_info,
        depth=summary_depth,
        verbose=0
    ))

    # save model summary to output file:
    os.makedirs(summaries_dir, exist_ok=True)
    summary_file = os.path.join(summaries_dir, summary_file_name)
    with open(summary_file, "w") as text_file:
        text_file.write(model_summary)
    # display model summary:
    print("MODEL SUMMARY:\n")
    print(model_summary)
    print("\n")

