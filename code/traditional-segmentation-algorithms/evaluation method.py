# Auther:ZHANG Jing
# Email address:jing.zhang@insa-rouen.fr
# Date:2018-12-7
# Title:using DICE function to evaluate results and ground truth image
# Usage:input segmented and ground truth
import SimpleITK as sitk
import numpy as np

gt = sitk.ReadImage("/home/jing/Desktop/imgseg/data/gt1.png")
seg = sitk.ReadImage("/home/jing/Desktop/imgseg/chan-vese.png")
seg.CopyInformation(gt)

dicefilter=sitk.LabelOverlapMeasuresImageFilter()
dicefilter.Execute(image1=gt, image2=seg)
out=dicefilter.GetDiceCoefficient()
print("The Dice Coefficient is: ",out)

distfilter= sitk.HausdorffDistanceImageFilter()
distfilter.Execute(image1=gt, image2=seg)
out2=distfilter.GetAverageHausdorffDistance()
print("The AverageHausdorffDistance is: ",out2)

results = np.zeros((5,2))
dicefilter=sitk.LabelOverlapMeasuresImageFilter()
distfilter= sitk.HausdorffDistanceImageFilter()

for i in range(5):
    dicefilter.Execute(gt == i, seg ==i)
    results[i,0] = dicefilter.GetDiceCoefficient()
    distfilter.Execute(gt == i, seg ==i)
    results[i,1] = distfilter.GetAverageHausdorffDistance()

print(results)

import pandas as pd
from enum import Enum
from IPython.display import display, HTML

class Label(Enum):
    background, esophagus, heart, trachea, aorta = range(5)

class Metrics(Enum):
    dice, hausdorff = range(2)

# Graft our results matrix into pandas data frames
results_df = pd.DataFrame(data=results, index = [name for name, _ in Label.__members__.items()],
                                  columns=[name for name, _ in Metrics.__members__.items()])

# Display the data as HTML tables and graphs
display(HTML(results_df.to_html(float_format=lambda x: '%.3f' % x)))