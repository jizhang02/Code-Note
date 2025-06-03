# Practice on medical imaging processing software

### Table of contents
* [Medical Image Analysis Using FIJI software](#medical-image-analysis-using-fiji-software)
* [Medical Image Analysis Using Slicer software](#medical-image-analysis-using-slicer-software)   
* [Medical Image Analysis Using ITK-SNAP software](#medical-image-analysis-using-itk-snap-software)

#### Medical Image Analysis Using FIJI software
* open/import a specific file in different formats
* zoom in/out an image: +/- key
* browse a slice: left/right key
* see 3D image in 3 directions
  * stacks->orthogonal views  
  * stacks->reslice '/' key
* compute mean/std value: 'm' key
  * results/analyse->set measurements
  * the whole slice
  * the selected area 
* Image->Lookup Tables, set different show ways
* Analyse->Plot profile, make a plot of selected area
* Image->Stacks->Statistics, statistics of a image
* Image->Show Info, save image info to a file
* Color bar: Analyze > Tools > Calibration Bar
* View 3D imagein 3 directions: Ctrl+Shift+H
* Image > Stacks > Make Montage: show all slices in a table
* Image > Stacks > Images to Stack: make multiple images into a stack
* Image > Stacks > Z Project (Max intensity): make all the max value of slices into one slice
* Image > Stacks > Z Project (Average intensity): make all the average value of slices into one slice
* Image > Stacks > Z Project (Sum slices): make all the slices into one slice
* Process > Enhance Contrast: show pet image more clearly
* Image > Overlay: add another image on the current image
* Export GIF: Image > Stacks > 3D Project, then click File > Save as > GIF
* Copy a ROI (line or square) to another window, select Analize > Tools > ROI manager, add current ROI, then on another window, select 'show all' from ROI manager

#### Medical Image Analysis Using Slicer software
* generate a gif 
  * Modules-> Utilities->ScreenCapture
  * Output type: video, image series, lightbox image
* show : click left-up corner buttons on three views respectively
* Color bar: Volume > Color Legend. Or right-click the image to show the color legent
* Overlay: Left upper corner of show panel > F > B 
* MIP: Lookup tables > PET-Maximum Intensity Projection
* Isodose: In radiotherapy, set threshold value of each line
* Adjust image contrast by right-clicking 'Adjust window/level'

#### Medical Image Analysis Using ITK-SNAP software
* It is easy to open a CT and PET image in one window or both two windows, the position is the same.
* Adjust the contrast by clicking auto mode.
* Load segmentation masks on the CT images and segmentation organs in 3D mode.
* When mask and CT are loaded, the left side will show CT value and mask value of a point.
* PaintBrush Mode on masks->Right click, remove label; Left click, add label.
* Polygon Mode -> Draw line on current label -> accept -> move to next slide -> paste last polygon -> drag the line to fine tune.
* LabelEditor -> Hide certain labels in all windows to only show one label.
* LabelEditor -> Actions -> Import/Export Label Descriptions.
* Export dcm data to nii.gz file
