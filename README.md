<h1>Motion Heatmap

<h3>This is one of the initial ways of tracking an object. The main concepts/operations to achieve this are:
- Background Substraction
- Application of a Threshold
- Accumulation of the changed pixels over time
- Add a color/heatmap<h3>


<h1>References to learn the concepts
  
<h3>Background Substraction: https://www.youtube.com/watch?v=nRt2LPRz704
https://docs.opencv.org/3.4/d1/dc5/tutorial_background_subtraction.html


Application of a Threshold: https://www.youtube.com/watch?v=lQdg-TJfL7Q
https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html


Accumulation of the changed pixels over time: Basically we need will create an empty numpy array using the image's resolution and accumulate all the pixel changes of the frames on this empty array.


Add a color/heatmap: https://docs.opencv.org/3.4/d3/d50/group__imgproc__colormap.html<h3>


<h1>OUTPUT:<h1>


![heatmap_video-ezgif com-optimize](https://github.com/Itachi-6/motion-heatmap/assets/150267189/93369688-81a1-4a9d-8b1f-aba245da4ffc)
