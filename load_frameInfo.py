import scipy.io as sio

def loadInfo(filename, option=2):
  mat_contents = sio.loadmat('frameInfo.mat')
  frameInfo = mat_contents['frameInfo'][0]
  frameInfoList = []
  for i in range(len(frameInfo)):
    if len(frameInfo[i]) == 0:
      frameInfoList.append(None)
    else:
      frameInfoList.append(frameInfo[i][1])
  return frameInfoList