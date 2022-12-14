# ------------------------------------------------------------------------------
# Quantized AlexNet Module
# ------------------------------------------------------------------------------

import torch
import torch.nn as nn

class QuantizedModel(nn.Module):
  def __init__(self, model_fp32):
    super(QuantizedModel, self).__init__()
    # QuantStub converts tensors from floating point to quantized.
    # This will only be used for inputs.
    self.quant = torch.quantization.QuantStub()
    # DeQuantStub converts tensors from quantized to floating point.
    # This will only be used for outputs.
    self.dequant = torch.quantization.DeQuantStub()
    # FP32 model
    self.model_fp32 = model_fp32

  def forward(self, x):
    # manually specify where tensors will be converted from floating
    # point to quantized in the quantized model
    x = self.quant(x)
    x = self.model_fp32(x)
    # manually specify where tensors will be converted from quantized
    # to floating point in the quantized model
    x = self.dequant(x)
    return x
