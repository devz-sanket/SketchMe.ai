import torch
import torch.nn as nn


def conv_block(in_channels, out_channels):
    return nn.Sequential(
        nn.Conv2d(in_channels, out_channels, 3, 1, 1),
        nn.InstanceNorm2d(out_channels),
        nn.ReLU(inplace=True)
    )


class Generator(nn.Module):
    def __init__(self):
        super().__init__()

        self.block_a = nn.Sequential(
            conv_block(3, 32),
            conv_block(32, 32),
        )

        self.block_b = nn.Sequential(
            conv_block(32, 64),
            conv_block(64, 64),
        )

        self.block_c = nn.Sequential(
            conv_block(64, 128),
            nn.Sequential(
                nn.Sequential(
                    conv_block(128, 128),
                    conv_block(128, 128)
                ),
                nn.Sequential(
                    conv_block(128, 128),
                    conv_block(128, 128)
                ),
                nn.Conv2d(128, 128, 3, 1, 1),
                nn.Conv2d(128, 128, 3, 1, 1),
            ),
            nn.Sequential(
                nn.Sequential(
                    conv_block(128, 128),
                    conv_block(128, 128)
                ),
                nn.Sequential(
                    conv_block(128, 128),
                    conv_block(128, 128)
                ),
                nn.Conv2d(128, 128, 3, 1, 1),
                nn.Conv2d(128, 128, 3, 1, 1),
            ),
            nn.Sequential(
                nn.Sequential(
                    conv_block(128, 128),
                    conv_block(128, 128)
                ),
                nn.Sequential(
                    conv_block(128, 128),
                    conv_block(128, 128)
                ),
                nn.Conv2d(128, 128, 3, 1, 1),
                nn.Conv2d(128, 128, 3, 1, 1),
            ),
            nn.Sequential(
                nn.Sequential(
                    conv_block(128, 128),
                    conv_block(128, 128)
                ),
                nn.Sequential(
                    conv_block(128, 128),
                    conv_block(128, 128)
                ),
                nn.Conv2d(128, 128, 3, 1, 1),
                nn.Conv2d(128, 128, 3, 1, 1),
            ),
            nn.Sequential(
                conv_block(128, 64),
                conv_block(64, 64)
            )
        )

        self.block_d = nn.Sequential(
            conv_block(64, 32),
            conv_block(32, 32)
        )

        self.block_e = nn.Sequential(
            conv_block(32, 32),
            conv_block(32, 32),
            conv_block(32, 32)
        )

        self.out_layer = nn.Sequential(
            nn.Conv2d(32, 3, 1)
        )

    def forward(self, x):
        x = self.block_a(x)
        x = self.block_b(x)
        x = self.block_c(x)
        x = self.block_d(x)
        x = self.block_e(x)
        return self.out_layer(x)
