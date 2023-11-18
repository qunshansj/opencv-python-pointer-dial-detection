python
x0, y0,xlen,ylen = farpoint(point_k,point_k[-1]),x0 - point_k[-1][0],y0 - point_k[-1][1]
deg = math.degrees(rad)
image_center = tuple(np.array(img_copy.shape)[:2] / 2)
rot_mat = cv.getRotationMatrix2D(image_center, deg, 1)
dst_copy = cv.warpAffine(img_copy, rot_mat, img_copy.shape[:2], flags=cv.INTER_LINEAR)
output = cv.warpAffine(output, rot_mat, output.shape[:2], flags=cv.INTER_LINEAR)
