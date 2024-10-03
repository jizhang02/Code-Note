# Workflow of training a deep learning model
### Table of contents
* [Prepare dataset](#prepare-dataset)
* [Architechture](#architecture)   
* [Set up environment](#set-up-environment)
* [Training](#training)    
* [Testing](#testing)   
* [Evaluation](#evaluation)
* [Common errors](#commen-errors) 

### Prepare dataset
### Architecture
☑️ CNN    
☑️ GAN    
☑️ Transformer        
☑️ SSL    
☑️ USL        
### Set up environment
☑️ CPU or GPU    
☑️ Epochs    
☑️ Learning rate    
☑️ Batch size    
☑️ Optimizer     
☑️ Scheduler         
☑️ Log save for loss metric curves.    

### Training
☑️ Strategy 1: Two-step pipeline. For instance, coarse segmentation (ROI detection) --> fine segmentation.    
☑️ Strategy 2: Compound loss functions. Main loss and auxiliary loss with weights. For instance, Dice+CE, Dice+Focal.    
☑️ Strategy 3: Think if a gradient is needed in some parts.    
☑️ Strategy 4: Training time augmentation (TTA).

### Testing
☑️ test-time-training (TTT) if necessary
### Evaluation
☑️ Metrics  
### Common errors
⁉️ **RuntimeError**: Trying to backward through the graph a second time (or directly access saved tensors after they have already been freed). Saved intermediate values of the graph are freed when you call .backward() or autograd.grad(). Specify retain_graph=True if you need to backward through the graph a second time or if you need to access saved tensors after calling backward.        
💠 Solution1: `retain_graph=True`    
💠 Solution2: check `torch.no_grad()` and `var.detach()`    
⁉️ **AttributeError**: 'float' object has no attribute 'backward'    
💠 Solution: `object.ToTensor()`    
⁉️ RuntimeError: one of the variables needed for gradient computation has been modified by an inplace operation: [torch.cuda.FloatTensor [1024, 27648]], which is output 0 of AsStridedBackward0, is at version 3; expected version 1 instead. Hint: enable anomaly detection to find the operation that failed to compute its gradient, with torch.autograd.set_detect_anomaly(True).    
💠 Solution: `output_copy = output.clone()      # avoid in-place opration`    
⁉️ **IndexError**: Dimension out of range (expected to be in range of [-2, 1], but got 2)    
💠 Solution: check data shape    
⁉️ AttributeError: 'tuple' object has no attribute 'shape'    
💠 Solution: check data shape convert to `a_array = np.array(a); print(a_array.shape)  # (3,)`   
⁉️ RuntimeError: element 0 of tensors does not require grad and does not have a grad_fn in `total_loss.backward()`    
💠 Solution: check the loss definition, it should have a gradient.    
⁉️ **IndentationError**: unindent does not match any outer indentation level
💠 Solution: check indent    

⁉️ **TypeError**: `logits = torch.squeeze(logits,dim=1)` squeeze() received an invalid combination of arguments - got (tuple, dim=int), but expected one of:
 * (Tensor input)
 * (Tensor input, int dim)
      didn't match because some of the arguments have invalid types: (!tuple of (Tensor, Tensor)!, dim=int)
 * (Tensor input, tuple of ints dim)
      didn't match because some of the arguments have invalid types: (!tuple of (Tensor, Tensor)!, !dim=int!)
 * (Tensor input, name dim)
      didn't match because some of the arguments have invalid types: (!tuple of (Tensor, Tensor)!, !dim=int!)

💠 Solution: check datatype and dimension    

