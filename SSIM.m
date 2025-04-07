clc
clear
close all

pathori = 'F:\Lan\classification\test_dataset_class2\BM\';
img_ori_list = dir(strcat(pathori,'*.jpg'));

pathG = 'F:\Lan\FS-D2AAE\BM\train_noD2_noloss\test_all_same';
img_G_list = dir(strcat(pathG,'*.jpg'));

img_num1 = length(img_ori_list);
img_num2 = length(img_G_list);

for j = 1:img_num1
    ori_name = img_ori_list(j).name;
    fprintf('ori: %s\n' ,ori_name);
    %new=ori_name(1:end-4);
    %fprintf('new: %s\n' ,new);
    
    for i=1:img_num2
        G_name = img_G_list(i).name;
        new=G_name(1:end-6);
        fprintf('G: %s\n' ,new);
    end
        
    
end
fprintf('Finsh!');