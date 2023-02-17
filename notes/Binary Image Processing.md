## Region
**A region** is a subset of an image. 
**Segmentation** is the process of grouping pixels into regions such that
- Each region satisfies some property, i.e. some property is common to all pixels
- Regions next to each other (pixels from adjacent regions) do not satisfy said property
- 2 kinds of segmentation
	- **Exhaustive partitioning/segmentation:** Union of all regions in the image will give the entire image
	- **Exclusive partitioning/segmentation**: $P_i \cap p_j = \emptyset, \forall i,j$

## Representation
**Zeroeth Order moment**: $\sum_{i=1}^{n}\sum_{ij=1}^{m}\text{img}[i][j]$
**Orientation** can be signified using 
- Axis of Second Order Moment: This is defined as the line where the squares of the distance of all the points is the least. 
- To minimize issues as distances get big, express in polar coordinates as $\rho=y\text{sin}\theta + x\text{cos}\theta$