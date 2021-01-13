import torch.nn as nn
import cunn
import cudnn.SpatialConvolution as Convolution
import cudnn.SpatialAveragePooling as Avg
import cudnn.ReLU as ReLU
import nn.SpatialMaxPooling as Max
import nn.SpatialBatchNormalization as SBatchNorm

local nn = require 'nn'
require 'cunn'
local Convolution = cudnn.SpatialConvolution
local Avg = cudnn.SpatialAveragePooling
local ReLU = cudnn.ReLU
local Max = nn.SpatialMaxPooling
local SBatchNorm = nn.SpatialBatchNormalization

def createModel(opt):
    depth = opt.depth
    shortcutType = opt.shortcutType or 'B'
    iChannels


local function createModel(opt)
   local depth = opt.depth
   local shortcutType = opt.shortcutType or 'B'
   local iChannels
