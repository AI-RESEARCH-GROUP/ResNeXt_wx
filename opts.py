# -*- coding: UTF-8 -*-

import argparse
parser = argparse.ArgumentParser(description='Torch-7 ResNet Training script')
#------------ General options --------------------
parser.add_argument('data', type=str, help='Path to dataset')
parser.add_argument('dataset', type=str, choices=['imagenet','cifar10', 'cifar100'], help='Choose between Cifar10,100 and imagenet')
parser.add_argument('manualSeed', type=int, default=0, help='Manually set RNG seed')
parser.add_argument('nGPU', type=int, default=1, help='Number of GPUs to use by default')
parser.add_argument('backend', type=str, choices=['cudnn','cunn'], help='Choose between cudnn/cunn')
parser.add_argument('cudnn', type=str,choices=['fastest' ,'default ','deterministic'], help='Choose between fastest,default and deterministic')
parser.add_argument('gen', type=str, help='Path to save generated files')
parser.add_argument('precision', type=str,choices=['single' ,'double ','half'],help='Choose between single,double and half')
# ------------- Data options ------------------------
parser.add_argument('nThreads',type=int,default=2,help='number of data loading threads')
#------------- Training options --------------------
parser.add_argument('-nEpochs',type=int,default=0,help='Number of total epochs to run')
parser.add_argument('epochNumber',type=int,default=1,help='Manual epoch number (useful on restarts)')
parser.add_argument('batchSize',type=int,default=32,help='mini-batch size (1 = pure stochastic)')
parser.add_argument('testOnly',type=str,help='Run on validation set only')
parser.add_argument('tenCrop',type=str,help='Ten-crop testing')
#------------- Checkpointing options ---------------
parser.add_argument('save',type=str,help='Directory in which to save checkpoints')
parser.add_argument('resume',type=str,help='Resume from the latest checkpoint in this directory')
#---------- Optimization options ----------------------
parser.add_argument('LR',type=float,default=0.1,help='initial learning rate')
parser.add_argument('momentum',type=float,default=0.9,help='momentum')
parser.add_argument('weightDecay',type=float,default=1e-4,help='weight decay')
#---------- Model options ----------------------------------
parser.add_argument('netType',type=str,choices=['resnext'],help='Choose resnext')
parser.add_argument('bottleneckType',type=str,choices=['resnet','resnext_B','resnext_C'],help='choose resnet, resnext_B ,resnext_C')
parser.add_argument('depth',type=int,default=34,help='choose number between 18,34,50,101,...')
parser.add_argument('baseWidth',type=int,default=64,help='ResNet base width')
parser.add_argument('cardinality',type=int,default=1,help='ResNet cardinality')
parser.add_argument('shortcutType',type=str,choices=['A','B','C'],help='choose between A,B,C')
parser.add_argument('retrain',type=str,help='Path to model to retrain with')
parser.add_argument('optimState',type=str,help='Path to an optimState to reload from')
#---------- Model options ----------------------------------
parser.add_argument('shareGradInput',type=str,help='Share gradInput tensors to reduce memory usage')
parser.add_argument('optnet',type=str,help='Use optnet to reduce memory usage')
parser.add_argument('resetClassifier',type=str,help='Reset the fully connected layer for fine-tuning')
parser.add_argument('nClasses',type=int,default=0,help='Number of classes in the dataset')


args = parser.parse_args()