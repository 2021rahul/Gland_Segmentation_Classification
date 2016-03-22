nstains=2;
lambda=0.02;
for i = 1:60
    img = strcat('testA_', int2str(i));
    img = strcat(img,'.bmp');
    I = imread(img);    
    [Wi, Hi,Hiv,sepstains]=stainsep(I,nstains,lambda);
    H = Hi(:,:,1);
    E = Hi(:,:,2);
    file = strcat('testA_', int2str(i));
    file = strcat(file, '_H.mat');
    save(file,'H');
    file = strcat('testA_', int2str(i));
    file = strcat(file, '_E.mat');
    save(file,'E');
end