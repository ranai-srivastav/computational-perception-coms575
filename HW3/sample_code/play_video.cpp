// Headers
#include <opencv2/core/core.hpp> 
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/opencv.hpp>
#include <iostream>

using namespace cv;
using namespace std;

// compile command
// cl /EHsc play_vid_test.cpp /I D:\installs\opencv\opencv\build\include /link /LIBPATH:D:\installs\opencv\opencv\build\x64\vc15\lib opencv_world451.lib


int main(int argc, char* argv[]) {
	
	// Load input video
	//  If your video is in a different source folder than your code, 
	//  make sure you specify the directory correctly!
	VideoCapture input_cap("short_clip_v5.avi");   
	
	// Check validity of target file
	if(!input_cap.isOpened()) {
		std::cout << "Input video not found." << std::endl;
		return -1;
	}
	
	namedWindow("output", WINDOW_AUTOSIZE);
	
	// Loop to read from input one frame at a time
	Mat frame;
	int count = 0;
	while(input_cap.read(frame)) {
		
		Mat gray;
		cvtColor(frame, gray, COLOR_BGR2GRAY);
		medianBlur(gray, gray, 5);
		vector<Vec3f> circles;
		HoughCircles(gray, circles, HOUGH_GRADIENT, 1,
		gray.rows/32,
		100, 30, 20, 40
		);
		for(size_t num=0; num < circles.size(); num++){
			Vec3i c = circles[num];
			Point center = Point(c[0], c[1]);
			circle(frame, center, 1, Scalar(0,100,100), 3, LINE_AA);
			int radius = c[2];
			circle(frame, center, radius, Scalar(0,255,0), 3, LINE_AA);
		}
			
		imshow("output", frame);

		// wait for ESC key to be pressed
		if(waitKey(30) == 27)
		{
			break;
		}
	}
	
	// free the capture objects from memory
	input_cap.release();
	
	return 1;
	
}