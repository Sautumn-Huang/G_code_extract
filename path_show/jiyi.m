
data=textread('G:\ResearchWork\G_extrac\jiyi.txt');

LOCUS=data;
LOCUS(:,1)=LOCUS(:,1)*1.8-200;
LOCUS(:,2)=LOCUS(:,2)*2.5-500;
LOCUS(:,3)=200;
x = LOCUS(:,1);
y = LOCUS(:,2);
angle=45;
angle=pi/180*angle;
%Ðý×ª
for ii=1:length(y)
    x0=(x(ii)-0)*cos(angle)-(y(ii)-0)*sin(angle)+0;
    y0=(x(ii)-0)*sin(angle)+(y(ii)-0)*cos(angle)+0;
    rotate_x(ii)=x0;
    rotate_y(ii)=y0;
end
LOCUS(:,1)=rotate_x;
LOCUS(:,2)=rotate_y;
plot(LOCUS(:,1),LOCUS(:,2),'LineWidth',3);
set(gca,'xlim',[0,500],'xtick',[0:50:500]);
set(gca,'ylim',[0,500],'ytick',[0:50:500]);

fid=fopen('C:\Users\Administrator\Desktop\jiyi1.txt','w');
fprintf(fid,'%.2f %.2f %.2f\n',LOCUS.');
fclose(fid);
