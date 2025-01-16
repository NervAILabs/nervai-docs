================================================
Support Matrix
================================================

The profiler support matrix lists down the supported `torch.nn.Module` objects for each metric. The metrics include:

- MAdds (Multiply-Adds)
- FLOPs (Floating Point Operations, ~2x MAdds)
- Parameters (Weights and Biases)
- Memory (Reads and Writes in Bytes)

.. toctree::
    :maxdepth: 1
    
    linear
    convolution
    pooling
    normalization
    activation
    recurrent
    transformer
    misc
    custom