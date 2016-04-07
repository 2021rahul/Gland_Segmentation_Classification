clear;
P=1000;
% close all
for i=0:71    
            img = strcat(int2str(i),'.bmp');
            aimg = strcat(int2str(i),'_bin.bmp');
            oimg = strcat(int2str(i),'_post.bmp');
            binary_image=imread(img);
            binary_image=im2bw(binary_image);
            %figure;imshow(binary_image)
            %figure; imshow(aimg);
            se = strel('disk', 4, 0);
            %image2=imopen(binary_image,se);
            %figure;imshow(binary_image);
            %figure;imshow(image2)
%             image2=imfill(binary_image,'holes');
            image3=imopen(binary_image,se);
            image3 = imfill(image3,'holes');
            
%         figure;imshow(image3)
        
        
        % Remove smaller connected components with less than P pixels
%         image3_new=imread(['C:\Users\eee\Downloads\Processed_data-2016-03-23\Processed data\',num2str(i),'_post.bmp']);
        image4=bwareaopen(image3,P);
%         se2 = strel('disk', 3, 0);
%         image5=imdilate(image4,se2);
        imwrite(image4, oimg);    
end