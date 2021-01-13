import torch


M = []
def isvalid(opt,cachePath):
    imageInfo = torch.load(cachePath)
    if imageInfo.basedir and imageInfo.basedir != opt.data:
       return False
    else:
       return True

def M.create(opt, split):
   cachePath = paths.concat(opt.gen, opt.dataset .. '.t7')

function M.create(opt, split)
   local cachePath = paths.concat(opt.gen, opt.dataset .. '.t7')
   if not paths.filep(cachePath) or not isvalid(opt, cachePath) then
      paths.mkdir('gen')

      local script = paths.dofile(opt.dataset .. '-gen.lua')
      script.exec(opt, cachePath)
   end
   local imageInfo = torch.load(cachePath)

   local Dataset = require('datasets/' .. opt.dataset)
   return Dataset(imageInfo, opt, split)
end

return M
