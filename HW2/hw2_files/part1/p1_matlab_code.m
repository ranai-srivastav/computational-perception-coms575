% Insert your code in part1/p1_matlab_code.m

clear;
clc;

raw_img = imread("image_part1a.png");
raw_img = rgb2gray(raw_img);
raw_img = im2bw(raw_img, 0.85);
raw_img = ~raw_img;
% imshow(raw_img)
struct_elem = ones(1,5);
struct_elem = struct_elem;
erode = imerode(raw_img, struct_elem);
horz = imdilate(erode, struct_elem);
figure, imshow(horz)
struct_elem = ones(5,1);
erode = imerode(raw_img, struct_elem);
vert = imdilate(erode, struct_elem);
figure, imshow(vert)
