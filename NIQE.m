clc
clear
close all

path = 'F:\Lan\CAAE\AM\train1\test_all\';
img_list = dir(strcat(path,'*.png'));
img_num = length(img_list);
niqea=0;

for j = 1:img_num
    img_name = img_list(j).name;
    img = imread(strcat(path,img_name));
    n_niqe = niqe(img);
   
    fprintf('img: %s\n' ,img_name);
    fprintf('\n')
    fprintf('NIQE score for original image is  %0.4f \n',n_niqe);
    niqea = niqea + n_niqe;
    
end
Total_niqe = niqea/img_num; 

fprintf('  Average niqe  = %0.4f\n', Total_niqe);



